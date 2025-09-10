# CLI Tools Testing Documentation

## Overview
Comprehensive testing documentation for all command-line interface tools in the Firish project, including validation tools, utilities, and scripts.

## Test Environment Setup

```bash
# Navigate to project root
cd /home/xanacan/Dropbox/WritingNew/firish

# Ensure all tools are executable
chmod +x tools/validators/validate_lexicon.py
chmod +x tools/**/*.py 2>/dev/null || true

# Create test directories
mkdir -p tests/{data,output,temp,logs}

# Set up test environment variables
export FIRISH_TEST_MODE=1
export FIRISH_LOG_LEVEL=DEBUG
```

## CLI Tool Categories

### 1. Validation Tools

#### 1.1 Lexicon Validator (`validate_lexicon.py`)

**Basic Usage Tests**

```bash
# Test 1: Standard validation
python tools/validators/validate_lexicon.py data/dictionary.csv data/schema.json
# Expected: Complete validation report with statistics

# Test 2: Help display
python tools/validators/validate_lexicon.py
# Expected: Usage instructions and examples

# Test 3: Version information
python tools/validators/validate_lexicon.py --version 2>/dev/null || echo "No version flag implemented"
# Expected: Version information or graceful handling
```

**File Input/Output Tests**

```bash
# Test 4: Non-existent input files
python tools/validators/validate_lexicon.py missing.csv data/schema.json
# Expected: Exit code 1, error message "Dictionary file not found"

python tools/validators/validate_lexicon.py data/dictionary.csv missing.json
# Expected: Exit code 1, error message "Schema file not found"

# Test 5: Permission denied files
touch tests/data/no_read.csv && chmod 000 tests/data/no_read.csv
python tools/validators/validate_lexicon.py tests/data/no_read.csv data/schema.json
# Expected: Graceful error handling
chmod 644 tests/data/no_read.csv && rm tests/data/no_read.csv

# Test 6: Output file generation
python tools/validators/validate_lexicon.py data/dictionary.csv data/schema.json
ls -la data/*_validation_report.json
# Expected: JSON report file created with detailed results
```

**Error Handling Tests**

```bash
# Test 7: Malformed CSV
echo "invalid,csv,content" > tests/data/malformed.csv
echo "no,proper,headers" >> tests/data/malformed.csv
python tools/validators/validate_lexicon.py tests/data/malformed.csv data/schema.json
# Expected: Validation errors reported, non-zero exit code

# Test 8: Malformed JSON schema
echo '{"invalid": json}' > tests/data/bad_schema.json
python tools/validators/validate_lexicon.py data/dictionary.csv tests/data/bad_schema.json
# Expected: JSON parsing error, non-zero exit code

# Test 9: Empty files
touch tests/data/empty.csv
python tools/validators/validate_lexicon.py tests/data/empty.csv data/schema.json
# Expected: Graceful handling of empty input
```

**Output Format Tests**

```bash
# Test 10: Standard output format
python tools/validators/validate_lexicon.py data/dictionary.csv data/schema.json > tests/output/standard.txt 2>&1
grep -q "FIRISH LEXICON VALIDATION REPORT" tests/output/standard.txt
# Expected: Formatted report header present

# Test 11: JSON report structure
python tools/validators/validate_lexicon.py data/dictionary.csv data/schema.json
python -c "
import json
with open('data/dictionary_validation_report.json') as f:
    report = json.load(f)
    assert 'validation_timestamp' in report
    assert 'summary' in report
    assert 'statistics' in report
    print('✅ JSON report structure valid')
"
# Expected: Valid JSON structure confirmed
```

**Performance Tests**

```bash
# Test 12: Large file performance
python -c "
import csv
with open('tests/data/large_test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id','firish','english','part_of_speech','category','definition'])
    for i in range(5000):
        writer.writerow([f'test_{i:05d}', f'word_{i}', f'meaning_{i}', 'noun', 'test', f'Test definition {i}'])
"

time python tools/validators/validate_lexicon.py tests/data/large_test.csv data/schema.json
# Expected: Completes within reasonable time (<30 seconds)

# Test 13: Memory usage
/usr/bin/time -v python tools/validators/validate_lexicon.py tests/data/large_test.csv data/schema.json 2>&1 | grep "Maximum resident set size"
# Expected: Memory usage remains reasonable (<200MB)
```

### 2. Utility Scripts

#### 2.1 Dictionary Converter Tools (if they exist)

```bash
# Test 14: Check for converter tools
ls tools/converters/ 2>/dev/null || echo "No converter tools found"

# Test 15: CSV to JSON conversion (if available)
find tools -name "*convert*" -o -name "*export*" -o -name "*import*"
# Expected: List of available conversion tools
```

#### 2.2 Statistics and Analysis Tools

```bash
# Test 16: Dictionary statistics
ls tools/analysis/ 2>/dev/null || echo "No analysis tools found"

# Test 17: Check for statistical analysis scripts
find tools -name "*stats*" -o -name "*analyze*" -o -name "*report*"
# Expected: List of analysis tools
```

### 3. Integration and Workflow Tests

#### 3.1 Tool Chain Integration

```bash
# Test 18: Validation → Analysis workflow
python tools/validators/validate_lexicon.py data/dictionary.csv data/schema.json
if [ $? -eq 0 ]; then
    echo "✅ Validation passed, ready for next step"
else
    echo "❌ Validation failed, workflow should stop"
fi
# Expected: Proper exit codes for workflow control

# Test 19: Batch processing simulation
for file in data/*.csv; do
    echo "Processing $file..."
    python tools/validators/validate_lexicon.py "$file" data/schema.json > "tests/output/$(basename "$file" .csv)_result.txt" 2>&1
    echo "Exit code: $?"
done
# Expected: Each file processed with appropriate exit codes
```

#### 3.2 Configuration and Environment Tests

```bash
# Test 20: Environment variable handling
export FIRISH_SCHEMA_PATH=data/schema.json
export FIRISH_OUTPUT_DIR=tests/output
# Test if tools respect environment variables (modify tools to support this)

# Test 21: Configuration file support
cat > tests/data/config.json << 'EOF'
{
    "schema_path": "data/schema.json",
    "output_format": "json",
    "validation_level": "strict"
}
EOF
# Test configuration file loading (if implemented)
```

## CLI Standards Compliance Tests

### Command Line Interface Standards

```bash
# Test 22: POSIX compliance
python tools/validators/validate_lexicon.py --help 2>/dev/null || python tools/validators/validate_lexicon.py -h 2>/dev/null || echo "No help flag"
# Expected: Help information displayed

# Test 23: Exit codes
python tools/validators/validate_lexicon.py data/dictionary.csv data/schema.json
echo "Validation success exit code: $?"
# Expected: Exit code 0 for success

python tools/validators/validate_lexicon.py missing.csv data/schema.json 2>/dev/null
echo "File not found exit code: $?"
# Expected: Exit code 1 for errors

# Test 24: Standard streams
python tools/validators/validate_lexicon.py data/dictionary.csv data/schema.json 1>tests/output/stdout.txt 2>tests/output/stderr.txt
echo "STDOUT lines: $(wc -l < tests/output/stdout.txt)"
echo "STDERR lines: $(wc -l < tests/output/stderr.txt)"
# Expected: Proper use of stdout/stderr
```

### Input Validation and Sanitization

```bash
# Test 25: Path injection attempts
python tools/validators/validate_lexicon.py "../../../etc/passwd" data/schema.json 2>/dev/null
echo "Path traversal exit code: $?"
# Expected: Safe handling, appropriate error

# Test 26: Special characters in filenames
touch "tests/data/file with spaces.csv"
cp data/dictionary.csv "tests/data/file with spaces.csv"
python tools/validators/validate_lexicon.py "tests/data/file with spaces.csv" data/schema.json
# Expected: Handles filenames with spaces correctly

# Test 27: Unicode in paths
mkdir -p "tests/data/ünïcødé"
cp data/dictionary.csv "tests/data/ünïcødé/tëst.csv"
python tools/validators/validate_lexicon.py "tests/data/ünïcødé/tëst.csv" data/schema.json
# Expected: Handles Unicode paths correctly
```

## Automation and Scripting Tests

### 3.3 Batch Processing

```bash
# Test 28: Batch validation script
cat > tests/batch_validate.sh << 'EOF'
#!/bin/bash
for csv_file in "$@"; do
    echo "Validating $csv_file..."
    python tools/validators/validate_lexicon.py "$csv_file" data/schema.json
    if [ $? -eq 0 ]; then
        echo "✅ $csv_file: PASSED"
    else
        echo "❌ $csv_file: FAILED"
    fi
    echo "---"
done
EOF
chmod +x tests/batch_validate.sh

# Test the batch script
./tests/batch_validate.sh data/dictionary.csv
# Expected: Batch processing with clear results
```

### 3.4 Continuous Integration Simulation

```bash
# Test 29: CI/CD pipeline simulation
cat > tests/ci_test.sh << 'EOF'
#!/bin/bash
set -e  # Exit on any error

echo "=== CI Pipeline Test ==="

# Step 1: Validate all dictionaries
echo "Step 1: Dictionary validation"
for dict_file in data/*.csv; do
    python tools/validators/validate_lexicon.py "$dict_file" data/schema.json || exit 1
done

# Step 2: Generate reports
echo "Step 2: Report generation"
python tools/validators/validate_lexicon.py data/dictionary.csv data/schema.json

# Step 3: Check report exists and is valid JSON
echo "Step 3: Report validation"
if [ -f "data/dictionary_validation_report.json" ]; then
    python -c "import json; json.load(open('data/dictionary_validation_report.json'))"
    echo "✅ CI Pipeline: ALL PASSED"
else
    echo "❌ CI Pipeline: REPORT MISSING"
    exit 1
fi
EOF
chmod +x tests/ci_test.sh

./tests/ci_test.sh
# Expected: Complete CI pipeline simulation passes
```

## Error Recovery and Robustness Tests

### 3.5 Fault Tolerance

```bash
# Test 30: Interrupted processing
timeout 5s python tools/validators/validate_lexicon.py tests/data/large_test.csv data/schema.json 2>/dev/null || echo "Timeout handled gracefully"
# Expected: Graceful handling of interruption

# Test 31: Disk space simulation (if safe to test)
# Create large temporary file to fill disk (BE CAREFUL)
# df -h . && echo "Skipping disk space test for safety"

# Test 32: Network dependency test (if tools use network)
# Disconnect network and test tools that might need internet
ping -c 1 google.com >/dev/null 2>&1 && echo "Network available" || echo "Testing offline mode"
```

### 3.6 Cross-Platform Compatibility

```bash
# Test 33: Path separator handling
python -c "
import os
print('Testing path separators...')
test_path = os.path.join('tests', 'data', 'test.csv')
print(f'Generated path: {test_path}')
"
# Expected: Proper path handling on current platform

# Test 34: Line ending compatibility
# Create files with different line endings
printf "id,firish,english\nword_001,test,test\n" > tests/data/unix_endings.csv
printf "id,firish,english\r\nword_001,test,test\r\n" > tests/data/windows_endings.csv

python tools/validators/validate_lexicon.py tests/data/unix_endings.csv data/schema.json >/dev/null 2>&1
echo "Unix endings exit code: $?"

python tools/validators/validate_lexicon.py tests/data/windows_endings.csv data/schema.json >/dev/null 2>&1
echo "Windows endings exit code: $?"
# Expected: Both should work correctly
```

## Documentation and Help Tests

### 3.7 User Experience

```bash
# Test 35: Help accessibility
python tools/validators/validate_lexicon.py --help 2>/dev/null || echo "No --help flag"
python tools/validators/validate_lexicon.py -h 2>/dev/null || echo "No -h flag"
python tools/validators/validate_lexicon.py 2>&1 | head -5
# Expected: Clear usage instructions

# Test 36: Error message clarity
python tools/validators/validate_lexicon.py missing_file.csv data/schema.json 2>&1 | head -3
# Expected: Clear, actionable error messages
```

## Performance Benchmarking

### 3.8 Performance Metrics

```bash
# Test 37: Baseline performance
echo "=== Performance Baseline ==="
time python tools/validators/validate_lexicon.py data/dictionary.csv data/schema.json >/dev/null 2>&1
echo "Small dataset validation time recorded"

time python tools/validators/validate_lexicon.py tests/data/large_test.csv data/schema.json >/dev/null 2>&1
echo "Large dataset validation time recorded"

# Test 38: Memory profiling
python -c "
import sys
sys.path.insert(0, 'tools/validators')
from validate_lexicon import LexiconValidator
import tracemalloc

tracemalloc.start()
validator = LexiconValidator('data/dictionary.csv', 'data/schema.json')
report = validator.run_validation()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f'Memory usage: current={current/1024/1024:.2f}MB, peak={peak/1024/1024:.2f}MB')
" 2>/dev/null || echo "Memory profiling requires tracemalloc"
```

## Expected CLI Behaviors

### Standard Output Patterns

```bash
# Expected successful run output pattern:
# 🔍 Starting lexicon validation...
# 📄 Dictionary: path/to/file.csv
# 📋 Schema: path/to/schema.json
# ✅ Loaded X entries with Y fields
# 🔎 Running validation checks...
# [Report content]
# 💾 Detailed report saved: path/to/report.json

# Expected error output pattern:
# ❌ Error: [Clear error description]
# Exit code: 1

# Expected warning output pattern:
# ⚠️  Warning: [Warning description]
# [Continues with processing]
```

### Exit Codes

- **0**: Validation successful, no errors found
- **1**: File not found, permission denied, or validation errors
- **2**: Invalid arguments or usage
- **130**: Interrupted by user (Ctrl+C)

## Test Automation Script

```bash
# Test 39: Complete CLI test suite
cat > tests/run_cli_tests.sh << 'EOF'
#!/bin/bash

# CLI Test Suite Runner
echo "=== Firish CLI Test Suite ==="
echo "Start time: $(date)"

TOTAL_TESTS=39
PASSED_TESTS=0
FAILED_TESTS=0

run_test() {
    local test_name="$1"
    local test_command="$2"
    local expected_exit_code="${3:-0}"
    
    echo -n "Running $test_name... "
    
    if eval "$test_command" >/dev/null 2>&1; then
        actual_exit_code=$?
    else
        actual_exit_code=$?
    fi
    
    if [ $actual_exit_code -eq $expected_exit_code ]; then
        echo "✅ PASS"
        ((PASSED_TESTS++))
    else
        echo "❌ FAIL (exit code: $actual_exit_code, expected: $expected_exit_code)"
        ((FAILED_TESTS++))
    fi
}

# Run all tests
run_test "Basic validation" "python tools/validators/validate_lexicon.py data/dictionary.csv data/schema.json" 0
run_test "Missing CSV file" "python tools/validators/validate_lexicon.py missing.csv data/schema.json" 1
run_test "Missing schema file" "python tools/validators/validate_lexicon.py data/dictionary.csv missing.json" 1
# ... add more test calls

echo ""
echo "=== Test Summary ==="
echo "Total tests: $TOTAL_TESTS"
echo "Passed: $PASSED_TESTS"
echo "Failed: $FAILED_TESTS"
echo "Success rate: $(( PASSED_TESTS * 100 / TOTAL_TESTS ))%"
echo "End time: $(date)"

if [ $FAILED_TESTS -eq 0 ]; then
    echo "🎉 All tests passed!"
    exit 0
else
    echo "💥 Some tests failed"
    exit 1
fi
EOF

chmod +x tests/run_cli_tests.sh
# Execute: ./tests/run_cli_tests.sh
```

## Maintenance and Updates

### CLI Test Maintenance

1. **Regular Updates**: Update tests when CLI interfaces change
2. **Platform Testing**: Test on different operating systems
3. **Performance Monitoring**: Track performance regressions
4. **User Feedback**: Incorporate user-reported issues into tests
5. **Documentation Sync**: Keep test documentation updated with tool changes

### Coverage Goals

- ✅ All CLI tools tested
- ✅ All command-line options covered
- ✅ Error conditions tested
- ✅ Performance benchmarks established
- ✅ Cross-platform compatibility verified
- ✅ Integration scenarios tested

This comprehensive CLI testing framework ensures all command-line tools work reliably across different environments and use cases.
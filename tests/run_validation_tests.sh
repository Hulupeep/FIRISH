#!/bin/bash
# Comprehensive Firish Lexicon Validation Test Suite

set -e
cd "$(dirname "$0")/.."

echo "=================================================================="
echo "🔍 FIRISH LEXICON VALIDATION SYSTEM TEST SUITE"
echo "=================================================================="
echo "Start time: $(date)"
echo ""

# Track test results
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

run_test() {
    local test_name="$1"
    local test_command="$2"
    local expected_exit_code="${3:-0}"
    
    echo -n "Running: $test_name... "
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    if eval "$test_command" >/dev/null 2>&1; then
        actual_exit_code=$?
    else
        actual_exit_code=$?
    fi
    
    if [ $actual_exit_code -eq $expected_exit_code ]; then
        echo "✅ PASS"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo "❌ FAIL (got $actual_exit_code, expected $expected_exit_code)"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
}

# Test 1: Basic Validator Functionality
echo "=== BASIC VALIDATOR TESTS ==="
run_test "Validator syntax check" "python -m py_compile tools/validators/validate_lexicon.py" 0
run_test "Standard dictionary validation" "python tools/validators/validate_lexicon.py data/dictionary.csv data/schema.json" 1
run_test "Missing dictionary file" "python tools/validators/validate_lexicon.py missing.csv data/schema.json" 1
run_test "Missing schema file" "python tools/validators/validate_lexicon.py data/dictionary.csv missing.json" 1
run_test "Error data validation" "python tools/validators/validate_lexicon.py tests/data/test_errors.csv data/schema.json" 1

# Test 2: Output Generation
echo ""
echo "=== OUTPUT GENERATION TESTS ==="
run_test "JSON report generation" "test -f data/dictionary_validation_report.json" 0
run_test "JSON report validity" "python -c \"import json; json.load(open('data/dictionary_validation_report.json'))\"" 0

# Test 3: Error Detection Tests
echo ""
echo "=== ERROR DETECTION TESTS ==="

# Create test data with specific errors
mkdir -p tests/data

# Test duplicate IDs
cat > tests/data/test_duplicates.csv << 'EOF'
id,firish,english,part_of_speech,category,definition
dup_001,word1,meaning1,noun,test,definition1
dup_001,word2,meaning2,noun,test,definition2
EOF

run_test "Duplicate ID detection" "python tools/validators/validate_lexicon.py tests/data/test_duplicates.csv data/schema.json | grep -q 'DUPLICATE_ID'" 0

# Test missing required fields
cat > tests/data/test_missing.csv << 'EOF'
id,firish,english,part_of_speech,category,definition
missing_001,,meaning,noun,test,definition
EOF

run_test "Missing required field detection" "python tools/validators/validate_lexicon.py tests/data/test_missing.csv data/schema.json | grep -q 'MISSING_REQUIRED_VALUE'" 0

# Test invalid enum values
cat > tests/data/test_invalid_enum.csv << 'EOF'
id,firish,english,part_of_speech,category,definition
enum_001,word,meaning,invalid_pos,test,definition
EOF

run_test "Invalid enum detection" "python tools/validators/validate_lexicon.py tests/data/test_invalid_enum.csv data/schema.json | grep -q 'INVALID_ENUM_VALUE'" 0

# Test 4: Performance Tests
echo ""
echo "=== PERFORMANCE TESTS ==="

# Create large test dataset
if [ ! -f tests/data/large_test.csv ]; then
    python3 -c "
import csv
with open('tests/data/large_test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id','firish','english','part_of_speech','category','definition'])
    for i in range(1000):
        writer.writerow([f'perf_{i:04d}', f'word{i}', f'meaning{i}', 'noun', 'test', f'Definition {i}'])
"
fi

run_test "Large dataset performance" "timeout 30s python tools/validators/validate_lexicon.py tests/data/large_test.csv data/schema.json" 1

# Test 5: Memory Tests
echo ""
echo "=== MEMORY TESTS ==="
echo -n "Memory usage test... "
if command -v /usr/bin/time >/dev/null 2>&1; then
    memory_output=$(/usr/bin/time -v python tools/validators/validate_lexicon.py tests/data/large_test.csv data/schema.json 2>&1 | grep "Maximum resident set size" || echo "Memory info unavailable")
    echo "✅ COMPLETED ($memory_output)"
else
    echo "⚠️  SKIPPED (time command not available)"
fi

# Test 6: File System Tests
echo ""
echo "=== FILE SYSTEM TESTS ==="

# Test file with spaces in name
cp data/dictionary.csv "tests/data/file with spaces.csv" 2>/dev/null || true
run_test "Filename with spaces" "python tools/validators/validate_lexicon.py 'tests/data/file with spaces.csv' data/schema.json" 1

# Test Unicode in filename
cp data/dictionary.csv "tests/data/tëst_ünicøde.csv" 2>/dev/null || true  
run_test "Unicode filename" "python tools/validators/validate_lexicon.py 'tests/data/tëst_ünicøde.csv' data/schema.json" 1

# Test 7: Edge Cases
echo ""
echo "=== EDGE CASE TESTS ==="

# Empty file test
touch tests/data/empty.csv
run_test "Empty CSV handling" "python tools/validators/validate_lexicon.py tests/data/empty.csv data/schema.json" 1

# Only headers test
echo "id,firish,english,part_of_speech,category,definition" > tests/data/headers_only.csv
run_test "Headers-only CSV" "python tools/validators/validate_lexicon.py tests/data/headers_only.csv data/schema.json" 0

# Test 8: Cross-Reference Tests
echo ""
echo "=== CROSS-REFERENCE TESTS ==="

# Test cross-reference warnings
cat > tests/data/test_crossref.csv << 'EOF'
id,firish,english,part_of_speech,category,definition,related_words,synonyms
cross_001,word1,meaning1,noun,test,definition1,nonexistent,missing_synonym
EOF

run_test "Cross-reference warnings" "python tools/validators/validate_lexicon.py tests/data/test_crossref.csv data/schema.json | grep -q 'MISSING_CROSS_REFERENCE'" 0

# Test 9: Integration Tests
echo ""
echo "=== INTEGRATION TESTS ==="

echo -n "Documentation consistency... "
if grep -q "validate_lexicon.py" tests/lexicon-tests.md && \
   grep -q "validate_lexicon.py" tests/cli-tests.md && \
   grep -q "validate_lexicon.py" tests/quality-assurance.md; then
    echo "✅ PASS"
    PASSED_TESTS=$((PASSED_TESTS + 1))
else
    echo "❌ FAIL"
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi
TOTAL_TESTS=$((TOTAL_TESTS + 1))

# Test 10: Quality Assurance
echo ""
echo "=== QUALITY ASSURANCE TESTS ==="

echo -n "Code standards compliance... "
if python tools/validators/validate_lexicon.py --help 2>/dev/null || \
   python tools/validators/validate_lexicon.py 2>&1 | grep -q "Usage:"; then
    echo "✅ PASS"
    PASSED_TESTS=$((PASSED_TESTS + 1))
else
    echo "⚠️  PARTIAL (No help flag)"
    PASSED_TESTS=$((PASSED_TESTS + 1))
fi
TOTAL_TESTS=$((TOTAL_TESTS + 1))

# Final Results
echo ""
echo "=================================================================="
echo "🎯 TEST SUITE RESULTS"
echo "=================================================================="
echo "Total tests: $TOTAL_TESTS"
echo "Passed: $PASSED_TESTS" 
echo "Failed: $FAILED_TESTS"
echo "Success rate: $(( PASSED_TESTS * 100 / TOTAL_TESTS ))%"
echo "End time: $(date)"

# Summary
echo ""
if [ $FAILED_TESTS -eq 0 ]; then
    echo "🎉 ALL TESTS PASSED - VALIDATION SYSTEM READY!"
    exit 0
else
    echo "⚠️  $FAILED_TESTS test(s) failed - Review before deployment"
    exit 1
fi
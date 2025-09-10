# Firish Lexicon Validation Tests

## Overview
Comprehensive test cases for the Firish lexicon validation system, covering all validation scenarios and edge cases.

## Test Environment Setup

```bash
# Navigate to project root
cd /home/xanacan/Dropbox/WritingNew/firish

# Create test data directory
mkdir -p tests/data

# Copy validation tools
cp tools/validators/validate_lexicon.py tests/
chmod +x tests/validate_lexicon.py
```

## Test Cases

### 1. Schema Validation Tests

#### Test 1.1: Valid Schema Loading
**Purpose**: Verify schema loads correctly from valid JSON file
**Input**: `data/schema.json` (valid schema)
**Expected Output**: Schema loads without errors
**Command**: 
```bash
python tests/validate_lexicon.py data/dictionary.csv data/schema.json
```
**Expected Result**: ✅ Schema validation passes

#### Test 1.2: Invalid Schema File
**Purpose**: Test behavior with missing schema file
**Input**: Non-existent schema file
**Command**:
```bash
python tests/validate_lexicon.py data/dictionary.csv missing_schema.json
```
**Expected Result**: ❌ Error: "Schema file not found"

#### Test 1.3: Malformed JSON Schema
**Purpose**: Test handling of corrupted JSON schema
**Input**: Create malformed schema file
**Setup**:
```bash
echo '{"invalid": json}' > tests/data/bad_schema.json
```
**Command**:
```bash
python tests/validate_lexicon.py data/dictionary.csv tests/data/bad_schema.json
```
**Expected Result**: ❌ Error: "Invalid JSON schema"

### 2. CSV Data Validation Tests

#### Test 2.1: Valid CSV Loading  
**Purpose**: Verify CSV loads correctly
**Input**: `data/dictionary.csv` (valid CSV)
**Expected Output**: CSV data loads successfully
**Verification**: Check for "✅ Loaded X entries with Y fields" message

#### Test 2.2: Missing CSV File
**Purpose**: Test behavior with missing dictionary file
**Command**:
```bash
python tests/validate_lexicon.py missing_dictionary.csv data/schema.json
```
**Expected Result**: ❌ Error: "CSV file not found"

#### Test 2.3: Empty CSV File
**Purpose**: Test handling of empty dictionary
**Setup**:
```bash
touch tests/data/empty_dictionary.csv
```
**Command**:
```bash
python tests/validate_lexicon.py tests/data/empty_dictionary.csv data/schema.json
```
**Expected Result**: ⚠️ Warning: "Empty dictionary file"

### 3. Required Fields Validation Tests

#### Test 3.1: All Required Fields Present
**Purpose**: Verify validation passes when all required fields exist
**Input**: Standard `data/dictionary.csv`
**Expected Result**: ✅ No missing required field errors
**Verification**: Look for absence of "MISSING_REQUIRED_FIELDS" errors

#### Test 3.2: Missing Required Fields in Headers
**Purpose**: Test detection of missing required columns
**Setup**:
```bash
# Create CSV missing 'definition' column
cat > tests/data/missing_headers.csv << 'EOF'
id,firish,english,part_of_speech,category
word_001,sláinte,health,noun,health
EOF
```
**Command**:
```bash
python tests/validate_lexicon.py tests/data/missing_headers.csv data/schema.json
```
**Expected Result**: ❌ Error: "Missing required fields in CSV headers: definition"

#### Test 3.3: Empty Required Field Values
**Purpose**: Test detection of empty required values
**Setup**:
```bash
# Create CSV with empty required field
cat > tests/data/empty_required.csv << 'EOF'
id,firish,english,part_of_speech,category,definition
word_001,,health,noun,health,Physical well-being
EOF
```
**Command**:
```bash
python tests/validate_lexicon.py tests/data/empty_required.csv data/schema.json
```
**Expected Result**: ❌ Error: "MISSING_REQUIRED_VALUE | Row 2 | Field 'firish'"

### 4. Data Pattern Validation Tests

#### Test 4.1: Valid Field Patterns
**Purpose**: Verify correctly formatted fields pass validation
**Input**: Standard `data/dictionary.csv` with valid patterns
**Expected Result**: ✅ No pattern validation errors

#### Test 4.2: Invalid ID Pattern
**Purpose**: Test ID field pattern validation
**Setup**:
```bash
cat > tests/data/invalid_id.csv << 'EOF'
id,firish,english,part_of_speech,category,definition
word@001,sláinte,health,noun,health,Physical well-being
EOF
```
**Expected Result**: ❌ Error: "INVALID_PATTERN | Row 2 | Field 'id' | Value doesn't match required pattern"

#### Test 4.3: Invalid Firish Word Pattern
**Purpose**: Test Firish word character validation
**Setup**:
```bash
cat > tests/data/invalid_firish.csv << 'EOF'
id,firish,english,part_of_speech,category,definition
word_001,sláinte123,health,noun,health,Physical well-being
EOF
```
**Expected Result**: ❌ Error: "INVALID_PATTERN | Row 2 | Field 'firish' | Numbers not allowed"

#### Test 4.4: Field Length Validation
**Purpose**: Test minimum and maximum length constraints
**Setup**:
```bash
cat > tests/data/length_violations.csv << 'EOF'
id,firish,english,part_of_speech,category,definition
word_001,a,health,noun,health,Too short definition here
word_002,$(echo 'a' | head -c 150),health,noun,health,Very long word test
EOF
```
**Expected Result**: ❌ Multiple length validation errors

### 5. Enum Value Validation Tests

#### Test 5.1: Valid Enum Values
**Purpose**: Verify accepted enum values pass validation
**Input**: Standard dictionary with valid parts of speech
**Expected Result**: ✅ No enum validation errors

#### Test 5.2: Invalid Part of Speech
**Purpose**: Test invalid enum values
**Setup**:
```bash
cat > tests/data/invalid_enum.csv << 'EOF'
id,firish,english,part_of_speech,category,definition
word_001,sláinte,health,invalid_pos,health,Physical well-being
EOF
```
**Expected Result**: ❌ Error: "INVALID_ENUM_VALUE | Row 2 | Field 'part_of_speech'"

### 6. Numeric Range Validation Tests

#### Test 6.1: Valid Difficulty Ratings
**Purpose**: Test valid difficulty values (1-10)
**Input**: Standard dictionary with valid ratings
**Expected Result**: ✅ No range validation errors

#### Test 6.2: Invalid Difficulty Range
**Purpose**: Test out-of-range difficulty values
**Setup**:
```bash
cat > tests/data/invalid_range.csv << 'EOF'
id,firish,english,part_of_speech,category,definition,difficulty,frequency
word_001,sláinte,health,noun,health,Physical well-being,15,5
EOF
```
**Expected Result**: ❌ Error: "INVALID_RANGE | Row 2 | Field 'difficulty' | Value 15 not in range [1, 10]"

#### Test 6.3: Non-Integer Numeric Fields
**Purpose**: Test non-numeric values in integer fields
**Setup**:
```bash
cat > tests/data/non_integer.csv << 'EOF'
id,firish,english,part_of_speech,category,definition,difficulty,frequency
word_001,sláinte,health,noun,health,Physical well-being,medium,high
EOF
```
**Expected Result**: ❌ Error: "INVALID_INTEGER | Row 2 | Field 'difficulty' | Expected integer value"

### 7. Duplicate Detection Tests

#### Test 7.1: No Duplicates
**Purpose**: Verify unique entries pass validation
**Input**: Standard dictionary with unique entries
**Expected Result**: ✅ No duplicate errors

#### Test 7.2: Duplicate IDs
**Purpose**: Test detection of duplicate entry IDs
**Setup**:
```bash
cat > tests/data/duplicate_ids.csv << 'EOF'
id,firish,english,part_of_speech,category,definition
word_001,sláinte,health,noun,health,Physical well-being
word_001,beatha,life,noun,existence,Life condition
EOF
```
**Expected Result**: ❌ Error: "DUPLICATE_ID | ID 'word_001' appears 2 times"

#### Test 7.3: Duplicate Firish Words
**Purpose**: Test detection of duplicate Firish entries
**Setup**:
```bash
cat > tests/data/duplicate_firish.csv << 'EOF'
id,firish,english,part_of_speech,category,definition
word_001,sláinte,health,noun,health,Physical well-being
word_002,sláinte,toast,interjection,greeting,Toast expression
EOF
```
**Expected Result**: ⚠️ Warning: "DUPLICATE_FIRISH_WORD | Firish word 'sláinte' appears 2 times"

### 8. Rating Consistency Tests

#### Test 8.1: Consistent Ratings
**Purpose**: Verify logical rating relationships
**Input**: Dictionary with consistent difficulty/frequency ratings
**Expected Result**: ✅ No rating inconsistency warnings

#### Test 8.2: Common Word High Difficulty
**Purpose**: Test detection of inconsistent common/difficult combinations
**Setup**:
```bash
cat > tests/data/rating_inconsistency.csv << 'EOF'
id,firish,english,part_of_speech,category,definition,difficulty,frequency
word_001,sláinte,health,noun,health,Physical well-being,10,10
EOF
```
**Expected Result**: ⚠️ Warning: "RATING_INCONSISTENCY | Very common word has very high difficulty"

#### Test 8.3: Rare Word Low Difficulty
**Purpose**: Test detection of rare but easy words
**Setup**:
```bash
cat > tests/data/rare_easy.csv << 'EOF'
id,firish,english,part_of_speech,category,definition,difficulty,frequency
word_001,sláinte,health,noun,health,Physical well-being,1,1
EOF
```
**Expected Result**: ⚠️ Warning: "RATING_INCONSISTENCY | Very rare word has very low difficulty"

### 9. Example Validation Tests

#### Test 9.1: Complete Examples
**Purpose**: Verify matched example pairs pass validation
**Input**: Dictionary with both Firish and English examples
**Expected Result**: ✅ No example validation errors

#### Test 9.2: Incomplete Examples
**Purpose**: Test detection of missing example translations
**Setup**:
```bash
cat > tests/data/incomplete_examples.csv << 'EOF'
id,firish,english,part_of_speech,category,definition,example_firish,example_english
word_001,sláinte,health,noun,health,Physical well-being,Tá sláinte mhaith agam,
EOF
```
**Expected Result**: ⚠️ Warning: "INCOMPLETE_EXAMPLE | Only one example provided"

#### Test 9.3: Example Word Mismatch
**Purpose**: Test detection when word doesn't appear in example
**Setup**:
```bash
cat > tests/data/example_mismatch.csv << 'EOF'
id,firish,english,part_of_speech,category,definition,example_firish,example_english
word_001,sláinte,health,noun,health,Physical well-being,Tá beatha mhaith agam,I have good health
EOF
```
**Expected Result**: ⚠️ Warning: "EXAMPLE_MISMATCH | Firish word 'sláinte' not found in example sentence"

### 10. Cross-Reference Validation Tests

#### Test 10.1: Valid Cross-References
**Purpose**: Verify existing cross-references pass validation
**Input**: Dictionary where all referenced words exist
**Expected Result**: ✅ No missing cross-reference warnings

#### Test 10.2: Missing Cross-References
**Purpose**: Test detection of invalid word references
**Setup**:
```bash
cat > tests/data/missing_references.csv << 'EOF'
id,firish,english,part_of_speech,category,definition,related_words,synonyms
word_001,sláinte,health,noun,health,Physical well-being,nonexistent_word,missing_synonym
EOF
```
**Expected Result**: ⚠️ Warning: "MISSING_CROSS_REFERENCE | Referenced word 'nonexistent_word' not found"

## Performance Tests

### Test 11.1: Large Dictionary Performance
**Purpose**: Test validation performance with large datasets
**Setup**:
```bash
# Create large test dictionary (1000+ entries)
python -c "
import csv
with open('tests/data/large_dictionary.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id','firish','english','part_of_speech','category','definition'])
    for i in range(1000):
        writer.writerow([f'word_{i:04d}', f'firish_{i}', f'english_{i}', 'noun', 'test', f'Definition {i}'])
"
```
**Command**:
```bash
time python tests/validate_lexicon.py tests/data/large_dictionary.csv data/schema.json
```
**Expected Result**: Completes within reasonable time (<10 seconds)

### Test 11.2: Memory Usage Test
**Purpose**: Verify reasonable memory usage
**Command**:
```bash
# Monitor memory usage during validation
/usr/bin/time -v python tests/validate_lexicon.py tests/data/large_dictionary.csv data/schema.json 2>&1 | grep "Maximum resident set size"
```
**Expected Result**: Memory usage stays reasonable (<100MB for 1000 entries)

## Integration Tests

### Test 12.1: End-to-End Validation
**Purpose**: Full validation workflow test
**Steps**:
1. Load schema and CSV
2. Run all validation checks
3. Generate comprehensive report
4. Save detailed JSON report
**Expected Result**: Complete workflow executes successfully

### Test 12.2: Error Recovery Test
**Purpose**: Test graceful handling of multiple error types
**Setup**: Create CSV with multiple error types
**Expected Result**: All errors detected and reported, validation continues

## Expected Output Formats

### Successful Validation Output
```
🔍 Starting lexicon validation...
📄 Dictionary: data/dictionary.csv
📋 Schema: data/schema.json

✅ Loaded 10 entries with 15 fields
🔎 Running validation checks...

================================================================================
🔍 FIRISH LEXICON VALIDATION REPORT
================================================================================

📊 SUMMARY:
   Total Entries: 10
   Errors: 0
   Warnings: 0
   Validation: ✅ PASSED

📈 STATISTICS:
   Unique IDs: 10
   Duplicate IDs: 0
   Missing Required: 0
   Invalid Values: 0
   Rating Issues: 0
   Example Issues: 0

💾 Detailed report saved: data/dictionary_validation_report.json
```

### Failed Validation Output
```
🔍 FIRISH LEXICON VALIDATION REPORT
================================================================================

📊 SUMMARY:
   Total Entries: 5
   Errors: 3
   Warnings: 2
   Validation: ❌ FAILED

❌ ERRORS (3):
   [ERROR] MISSING_REQUIRED_VALUE | Row 2 | Field 'definition' | Required field is empty
   [ERROR] DUPLICATE_ID | ID 'word_001' appears 2 times
   [ERROR] INVALID_RANGE | Row 3 | Field 'difficulty' | Value 15 not in range [1, 10]

⚠️  WARNINGS (2):
   [WARNING] RATING_INCONSISTENCY | Row 4 | Very common word has very high difficulty
   [WARNING] EXAMPLE_MISMATCH | Row 5 | Firish word not found in example sentence
```

## Test Execution Commands

### Run All Tests
```bash
#!/bin/bash
# Run complete test suite

echo "=== Firish Lexicon Validation Test Suite ==="

# Test 1: Standard validation
echo "Test 1: Standard Dictionary Validation"
python tests/validate_lexicon.py data/dictionary.csv data/schema.json

# Test 2: Error cases
echo -e "\nTest 2: Missing files"
python tests/validate_lexicon.py missing.csv data/schema.json 2>/dev/null && echo "FAIL" || echo "PASS"
python tests/validate_lexicon.py data/dictionary.csv missing.json 2>/dev/null && echo "FAIL" || echo "PASS"

# Test 3-12: Run specific test cases as created above
# ... (additional test executions)

echo -e "\n=== Test Suite Complete ==="
```

### Individual Test Commands
```bash
# Basic validation
python tools/validators/validate_lexicon.py data/dictionary.csv data/schema.json

# Test with custom data
python tools/validators/validate_lexicon.py tests/data/test_dictionary.csv data/schema.json

# Performance test
time python tools/validators/validate_lexicon.py tests/data/large_dictionary.csv data/schema.json
```

## Test Data Requirements

Each test case should include:
- **Setup**: Commands to create test data
- **Input**: Specific test files or data
- **Expected Output**: Exact expected results
- **Verification**: How to confirm test success/failure
- **Cleanup**: Commands to remove test files

## Coverage Requirements

The test suite should achieve:
- ✅ 100% validation rule coverage
- ✅ All error types tested
- ✅ All warning types tested  
- ✅ Edge cases and boundary conditions
- ✅ Performance and scalability
- ✅ Integration and workflow testing

## Maintenance Notes

- Update test cases when schema changes
- Add new tests for new validation rules
- Monitor test execution time and optimize as needed
- Ensure test data represents real-world scenarios
- Document any test failures and resolutions
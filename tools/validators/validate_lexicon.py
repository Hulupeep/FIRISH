#!/usr/bin/env python3
"""
Firish Lexicon Validator
========================

Comprehensive validation tool for dictionary.csv against schema.json with:
- Missing fields detection
- Invalid values validation  
- Duplicate entries checking
- Rating consistency analysis
- Example validation
- Proper error reporting and statistics

Uses Python standard library only.
"""

import csv
import json
import re
import sys
import os
from collections import defaultdict, Counter
from typing import Dict, List, Set, Tuple, Any, Optional
from datetime import datetime


class ValidationError:
    """Represents a validation error with context."""
    
    def __init__(self, error_type: str, message: str, row: int = None, 
                 field: str = None, value: str = None, severity: str = 'error'):
        self.error_type = error_type
        self.message = message
        self.row = row
        self.field = field
        self.value = value
        self.severity = severity  # 'error', 'warning', 'info'
        
    def __str__(self):
        parts = [f"[{self.severity.upper()}]", f"{self.error_type}:"]
        if self.row is not None:
            parts.append(f"Row {self.row + 1}")
        if self.field:
            parts.append(f"Field '{self.field}'")
        parts.append(self.message)
        if self.value and len(str(self.value)) < 50:
            parts.append(f"Value: '{self.value}'")
        return " | ".join(parts)


class LexiconValidator:
    """Main validator class for Firish lexicon."""
    
    def __init__(self, csv_path: str, schema_path: str):
        self.csv_path = csv_path
        self.schema_path = schema_path
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []
        self.stats = {
            'total_entries': 0,
            'unique_ids': set(),
            'duplicate_ids': set(),
            'missing_required_fields': 0,
            'invalid_values': 0,
            'rating_inconsistencies': 0,
            'example_mismatches': 0,
            'categories': Counter(),
            'parts_of_speech': Counter(),
            'difficulty_distribution': Counter(),
            'frequency_distribution': Counter()
        }
        
    def load_schema(self) -> Dict[str, Any]:
        """Load and parse the JSON schema."""
        try:
            with open(self.schema_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON schema: {e}")
            
    def load_csv_data(self) -> Tuple[List[str], List[Dict[str, str]]]:
        """Load and parse CSV data."""
        try:
            with open(self.csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames or []
                rows = list(reader)
                return headers, rows
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found: {self.csv_path}")
        except Exception as e:
            raise ValueError(f"Error reading CSV file: {e}")
            
    def validate_required_fields(self, headers: List[str], schema: Dict[str, Any]) -> None:
        """Check for required fields in CSV headers."""
        entry_schema = schema.get('properties', {}).get('entries', {}).get('items', {})
        required_fields = entry_schema.get('required', [])
        
        missing_fields = set(required_fields) - set(headers)
        if missing_fields:
            self.errors.append(ValidationError(
                'MISSING_REQUIRED_FIELDS',
                f"Missing required fields in CSV headers: {', '.join(sorted(missing_fields))}"
            ))
            
    def validate_field_patterns(self, row_idx: int, row: Dict[str, str], 
                               field_schemas: Dict[str, Any]) -> None:
        """Validate field patterns and constraints."""
        for field, value in row.items():
            if not value.strip():  # Skip empty values for now
                continue
                
            field_schema = field_schemas.get(field, {})
            
            # Pattern validation
            if 'pattern' in field_schema:
                pattern = field_schema['pattern']
                if not re.match(pattern, value):
                    self.errors.append(ValidationError(
                        'INVALID_PATTERN',
                        f"Value doesn't match required pattern: {pattern}",
                        row_idx, field, value
                    ))
                    self.stats['invalid_values'] += 1
                    
            # Length validation
            min_length = field_schema.get('minLength', 0)
            max_length = field_schema.get('maxLength', float('inf'))
            if not (min_length <= len(value) <= max_length):
                self.errors.append(ValidationError(
                    'INVALID_LENGTH',
                    f"Length {len(value)} not in range [{min_length}, {max_length}]",
                    row_idx, field, value
                ))
                self.stats['invalid_values'] += 1
                
            # Enum validation
            if 'enum' in field_schema:
                valid_values = field_schema['enum']
                if value not in valid_values:
                    self.errors.append(ValidationError(
                        'INVALID_ENUM_VALUE',
                        f"Value not in allowed list: {valid_values}",
                        row_idx, field, value
                    ))
                    self.stats['invalid_values'] += 1
                    
            # Integer validation for numeric fields
            if field_schema.get('type') == 'integer':
                try:
                    int_value = int(value)
                    min_val = field_schema.get('minimum', float('-inf'))
                    max_val = field_schema.get('maximum', float('inf'))
                    if not (min_val <= int_value <= max_val):
                        self.errors.append(ValidationError(
                            'INVALID_RANGE',
                            f"Integer value {int_value} not in range [{min_val}, {max_val}]",
                            row_idx, field, value
                        ))
                        self.stats['invalid_values'] += 1
                except ValueError:
                    self.errors.append(ValidationError(
                        'INVALID_INTEGER',
                        f"Expected integer value",
                        row_idx, field, value
                    ))
                    self.stats['invalid_values'] += 1
                    
    def validate_duplicates(self, rows: List[Dict[str, str]]) -> None:
        """Check for duplicate entries."""
        id_counts = Counter()
        firish_counts = Counter()
        
        for row_idx, row in enumerate(rows):
            entry_id = row.get('id', '').strip()
            firish_word = row.get('firish', '').strip().lower()
            
            if entry_id:
                id_counts[entry_id] += 1
                if id_counts[entry_id] == 1:
                    self.stats['unique_ids'].add(entry_id)
                else:
                    self.stats['duplicate_ids'].add(entry_id)
                    
            if firish_word:
                firish_counts[firish_word] += 1
                
        # Report duplicate IDs
        for entry_id, count in id_counts.items():
            if count > 1:
                self.errors.append(ValidationError(
                    'DUPLICATE_ID',
                    f"ID '{entry_id}' appears {count} times"
                ))
                
        # Report duplicate Firish words (as warnings)
        for firish_word, count in firish_counts.items():
            if count > 1:
                self.warnings.append(ValidationError(
                    'DUPLICATE_FIRISH_WORD',
                    f"Firish word '{firish_word}' appears {count} times",
                    severity='warning'
                ))
                
    def validate_rating_consistency(self, rows: List[Dict[str, str]]) -> None:
        """Check for rating consistency and logical relationships."""
        for row_idx, row in enumerate(rows):
            difficulty = row.get('difficulty', '').strip()
            frequency = row.get('frequency', '').strip()
            
            if difficulty and frequency:
                try:
                    diff_val = int(difficulty)
                    freq_val = int(frequency)
                    
                    self.stats['difficulty_distribution'][diff_val] += 1
                    self.stats['frequency_distribution'][freq_val] += 1
                    
                    # Very common words (freq 9-10) shouldn't be very difficult (diff 8-10)
                    if freq_val >= 9 and diff_val >= 8:
                        self.warnings.append(ValidationError(
                            'RATING_INCONSISTENCY',
                            f"Very common word (freq={freq_val}) has very high difficulty (diff={diff_val})",
                            row_idx, 'difficulty/frequency', f"{diff_val}/{freq_val}",
                            severity='warning'
                        ))
                        self.stats['rating_inconsistencies'] += 1
                        
                    # Very rare words (freq 1-2) being very easy (diff 1-2) is unusual
                    if freq_val <= 2 and diff_val <= 2:
                        self.warnings.append(ValidationError(
                            'RATING_INCONSISTENCY',
                            f"Very rare word (freq={freq_val}) has very low difficulty (diff={diff_val})",
                            row_idx, 'difficulty/frequency', f"{diff_val}/{freq_val}",
                            severity='warning'
                        ))
                        self.stats['rating_inconsistencies'] += 1
                        
                except ValueError:
                    pass  # Already handled in field validation
                    
    def validate_examples(self, rows: List[Dict[str, str]]) -> None:
        """Validate example sentences and translations."""
        for row_idx, row in enumerate(rows):
            firish_word = row.get('firish', '').strip()
            example_firish = row.get('example_firish', '').strip()
            example_english = row.get('example_english', '').strip()
            
            # If one example exists, both should exist
            if bool(example_firish) != bool(example_english):
                self.warnings.append(ValidationError(
                    'INCOMPLETE_EXAMPLE',
                    f"Only one example provided (Firish: {'yes' if example_firish else 'no'}, "
                    f"English: {'yes' if example_english else 'no'})",
                    row_idx, 'example_firish/example_english', '',
                    severity='warning'
                ))
                
            # Firish word should appear in Firish example
            if firish_word and example_firish:
                # Simple word boundary check
                if not re.search(r'\b' + re.escape(firish_word.lower()) + r'\b', 
                                 example_firish.lower()):
                    self.warnings.append(ValidationError(
                        'EXAMPLE_MISMATCH',
                        f"Firish word '{firish_word}' not found in example sentence",
                        row_idx, 'example_firish', example_firish,
                        severity='warning'
                    ))
                    self.stats['example_mismatches'] += 1
                    
    def validate_cross_references(self, rows: List[Dict[str, str]]) -> None:
        """Validate cross-references like related_words, synonyms, antonyms."""
        all_firish_words = {row.get('firish', '').strip().lower() 
                           for row in rows if row.get('firish', '').strip()}
        
        for row_idx, row in enumerate(rows):
            for field in ['related_words', 'synonyms', 'antonyms']:
                values = row.get(field, '').strip()
                if not values:
                    continue
                    
                # Parse pipe-separated values
                referenced_words = [w.strip().lower() for w in values.split('|') if w.strip()]
                
                for word in referenced_words:
                    if word not in all_firish_words:
                        self.warnings.append(ValidationError(
                            'MISSING_CROSS_REFERENCE',
                            f"Referenced word '{word}' not found in dictionary",
                            row_idx, field, word,
                            severity='warning'
                        ))
                        
    def collect_statistics(self, rows: List[Dict[str, str]]) -> None:
        """Collect general statistics about the lexicon."""
        self.stats['total_entries'] = len(rows)
        
        for row in rows:
            category = row.get('category', '').strip()
            pos = row.get('part_of_speech', '').strip()
            
            if category:
                self.stats['categories'][category] += 1
            if pos:
                self.stats['parts_of_speech'][pos] += 1
                
    def validate_required_field_completeness(self, rows: List[Dict[str, str]], 
                                           required_fields: List[str]) -> None:
        """Check that required fields are not empty."""
        for row_idx, row in enumerate(rows):
            for field in required_fields:
                value = row.get(field, '').strip()
                if not value:
                    self.errors.append(ValidationError(
                        'MISSING_REQUIRED_VALUE',
                        f"Required field is empty",
                        row_idx, field, value
                    ))
                    self.stats['missing_required_fields'] += 1
                    
    def run_validation(self) -> Dict[str, Any]:
        """Run complete validation process."""
        print(f"🔍 Starting lexicon validation...")
        print(f"📄 Dictionary: {self.csv_path}")
        print(f"📋 Schema: {self.schema_path}")
        print()
        
        try:
            # Load data
            schema = self.load_schema()
            headers, rows = self.load_csv_data()
            
            print(f"✅ Loaded {len(rows)} entries with {len(headers)} fields")
            
            # Get field schemas
            entry_schema = schema.get('properties', {}).get('entries', {}).get('items', {})
            field_schemas = entry_schema.get('properties', {})
            required_fields = entry_schema.get('required', [])
            
            # Run validation checks
            print("🔎 Running validation checks...")
            
            self.validate_required_fields(headers, schema)
            self.validate_required_field_completeness(rows, required_fields)
            
            for row_idx, row in enumerate(rows):
                self.validate_field_patterns(row_idx, row, field_schemas)
                
            self.validate_duplicates(rows)
            self.validate_rating_consistency(rows)
            self.validate_examples(rows)
            self.validate_cross_references(rows)
            self.collect_statistics(rows)
            
            # Generate report
            return self.generate_report()
            
        except Exception as e:
            self.errors.append(ValidationError(
                'VALIDATION_FAILURE',
                f"Validation failed: {str(e)}"
            ))
            return self.generate_report()
            
    def generate_report(self) -> Dict[str, Any]:
        """Generate comprehensive validation report."""
        total_issues = len(self.errors) + len(self.warnings)
        
        report = {
            'validation_timestamp': datetime.now().isoformat(),
            'files': {
                'csv_path': self.csv_path,
                'schema_path': self.schema_path
            },
            'summary': {
                'total_entries': self.stats['total_entries'],
                'total_errors': len(self.errors),
                'total_warnings': len(self.warnings),
                'total_issues': total_issues,
                'validation_passed': len(self.errors) == 0
            },
            'statistics': {
                'unique_ids': len(self.stats['unique_ids']),
                'duplicate_ids': len(self.stats['duplicate_ids']),
                'missing_required_fields': self.stats['missing_required_fields'],
                'invalid_values': self.stats['invalid_values'],
                'rating_inconsistencies': self.stats['rating_inconsistencies'],
                'example_mismatches': self.stats['example_mismatches'],
                'categories': dict(self.stats['categories'].most_common(10)),
                'parts_of_speech': dict(self.stats['parts_of_speech'].most_common()),
                'difficulty_distribution': dict(sorted(self.stats['difficulty_distribution'].items())),
                'frequency_distribution': dict(sorted(self.stats['frequency_distribution'].items()))
            },
            'errors': [str(error) for error in self.errors],
            'warnings': [str(warning) for warning in self.warnings]
        }
        
        return report
        
    def print_report(self, report: Dict[str, Any]) -> None:
        """Print formatted validation report."""
        print("\n" + "="*80)
        print("🔍 FIRISH LEXICON VALIDATION REPORT")
        print("="*80)
        
        summary = report['summary']
        stats = report['statistics']
        
        # Summary
        print(f"\n📊 SUMMARY:")
        print(f"   Total Entries: {summary['total_entries']}")
        print(f"   Errors: {summary['total_errors']}")
        print(f"   Warnings: {summary['total_warnings']}")
        print(f"   Validation: {'✅ PASSED' if summary['validation_passed'] else '❌ FAILED'}")
        
        # Statistics
        print(f"\n📈 STATISTICS:")
        print(f"   Unique IDs: {stats['unique_ids']}")
        print(f"   Duplicate IDs: {stats['duplicate_ids']}")
        print(f"   Missing Required: {stats['missing_required_fields']}")
        print(f"   Invalid Values: {stats['invalid_values']}")
        print(f"   Rating Issues: {stats['rating_inconsistencies']}")
        print(f"   Example Issues: {stats['example_mismatches']}")
        
        # Categories
        if stats['categories']:
            print(f"\n🏷️  TOP CATEGORIES:")
            for category, count in stats['categories'].items():
                print(f"   {category}: {count}")
                
        # Parts of speech
        if stats['parts_of_speech']:
            print(f"\n📝 PARTS OF SPEECH:")
            for pos, count in stats['parts_of_speech'].items():
                print(f"   {pos}: {count}")
                
        # Difficulty distribution
        if stats['difficulty_distribution']:
            print(f"\n⚡ DIFFICULTY DISTRIBUTION:")
            for diff, count in stats['difficulty_distribution'].items():
                print(f"   Level {diff}: {count} words")
                
        # Frequency distribution  
        if stats['frequency_distribution']:
            print(f"\n🔄 FREQUENCY DISTRIBUTION:")
            for freq, count in stats['frequency_distribution'].items():
                print(f"   Level {freq}: {count} words")
        
        # Errors
        if report['errors']:
            print(f"\n❌ ERRORS ({len(report['errors'])}):")
            for error in report['errors'][:20]:  # Show first 20
                print(f"   {error}")
            if len(report['errors']) > 20:
                print(f"   ... and {len(report['errors']) - 20} more errors")
                
        # Warnings
        if report['warnings']:
            print(f"\n⚠️  WARNINGS ({len(report['warnings'])}):")
            for warning in report['warnings'][:10]:  # Show first 10
                print(f"   {warning}")
            if len(report['warnings']) > 10:
                print(f"   ... and {len(report['warnings']) - 10} more warnings")
        
        print("\n" + "="*80)


def main():
    """Main entry point."""
    if len(sys.argv) != 3:
        print("Usage: python validate_lexicon.py <dictionary.csv> <schema.json>")
        print("\nExample:")
        print("  python validate_lexicon.py data/dictionary.csv data/schema.json")
        sys.exit(1)
        
    csv_path = sys.argv[1]
    schema_path = sys.argv[2]
    
    # Check file existence
    if not os.path.exists(csv_path):
        print(f"❌ Error: Dictionary file not found: {csv_path}")
        sys.exit(1)
        
    if not os.path.exists(schema_path):
        print(f"❌ Error: Schema file not found: {schema_path}")
        sys.exit(1)
        
    validator = LexiconValidator(csv_path, schema_path)
    report = validator.run_validation()
    validator.print_report(report)
    
    # Save detailed report
    report_path = os.path.splitext(csv_path)[0] + '_validation_report.json'
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"💾 Detailed report saved: {report_path}")
    except Exception as e:
        print(f"⚠️  Could not save report: {e}")
    
    # Exit with appropriate code
    sys.exit(0 if report['summary']['validation_passed'] else 1)


if __name__ == '__main__':
    main()
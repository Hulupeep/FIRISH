#!/usr/bin/env python3
"""
FIRISH Language Validator
Validates FIRISH syntax, semantics, and emotional coherence
"""

import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional
from dataclasses import dataclass
from enum import Enum

class ValidationLevel(Enum):
    SYNTAX = "syntax"
    SEMANTIC = "semantic" 
    EMOTIONAL = "emotional"
    CULTURAL = "cultural"

@dataclass
class ValidationError:
    line_number: int
    column: int
    level: ValidationLevel
    message: str
    suggestion: Optional[str] = None

class FirishValidator:
    """Comprehensive FIRISH language validator"""
    
    def __init__(self, lexicon_path: Optional[str] = None):
        self.lexicon_path = lexicon_path or self._find_lexicon()
        self.vocabulary = self._load_vocabulary()
        self.errors: List[ValidationError] = []
        
        # Define validation patterns
        self.patterns = {
            'emotional_modifier': r'~([a-zA-Z_][a-zA-Z0-9_]*)',
            'cultural_modifier': r'\.([a-zA-Z_][a-zA-Z0-9_]*)',
            'transition': r'([a-zA-Z_~.]+)>([a-zA-Z_~.]+)',
            'assignment': r'([a-zA-Z_~.>]+)\s*=\s*(.+)',
            'comment': r'#.*$',
            'word': r'[a-zA-Z_][a-zA-Z0-9_]*'
        }
        
        # Compile patterns
        self.compiled_patterns = {
            name: re.compile(pattern) 
            for name, pattern in self.patterns.items()
        }
    
    def _find_lexicon(self) -> str:
        """Find lexicon file"""
        possible_paths = [
            Path(__file__).parent.parent.parent / "lexicon" / "core_vocabulary.json",
            Path("lexicon/core_vocabulary.json"),
        ]
        
        for path in possible_paths:
            if path.exists():
                return str(path)
        return "lexicon/core_vocabulary.json"
    
    def _load_vocabulary(self) -> Dict:
        """Load vocabulary from lexicon"""
        try:
            with open(self.lexicon_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"vocabulary": {"emotional_markers": {}}}
    
    def validate_file(self, filepath: str) -> List[ValidationError]:
        """Validate entire FIRISH file"""
        self.errors = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.validate_content(content)
        except FileNotFoundError:
            self.errors.append(ValidationError(
                0, 0, ValidationLevel.SYNTAX,
                f"File not found: {filepath}"
            ))
            return self.errors
    
    def validate_content(self, content: str) -> List[ValidationError]:
        """Validate FIRISH content string"""
        self.errors = []
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            self._validate_line(line, line_num)
        
        return self.errors
    
    def _validate_line(self, line: str, line_num: int):
        """Validate single line of FIRISH code"""
        original_line = line
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or line.startswith('#'):
            return
        
        # Validate assignment statements
        assignment_match = self.compiled_patterns['assignment'].match(line)
        if assignment_match:
            variable, value = assignment_match.groups()
            self._validate_variable(variable.strip(), line_num, original_line)
            self._validate_value(value.strip(), line_num, original_line)
            return
        
        # Validate standalone expressions
        self._validate_expression(line, line_num, original_line)
    
    def _validate_variable(self, variable: str, line_num: int, original_line: str):
        """Validate variable name (left side of assignment)"""
        self._validate_expression(variable, line_num, original_line, is_variable=True)
    
    def _validate_value(self, value: str, line_num: int, original_line: str):
        """Validate value (right side of assignment)"""
        # Remove quotes from string literals
        if (value.startswith('"') and value.endswith('"')) or \
           (value.startswith("'") and value.endswith("'")):
            # String literal - basic validation
            return
        
        # Otherwise validate as expression
        self._validate_expression(value, line_num, original_line)
    
    def _validate_expression(self, expr: str, line_num: int, original_line: str, is_variable: bool = False):
        """Validate FIRISH expression"""
        # Check for transitions
        transition_match = self.compiled_patterns['transition'].search(expr)
        if transition_match:
            from_state, to_state = transition_match.groups()
            self._validate_emotional_state(from_state.strip(), line_num, original_line)
            self._validate_emotional_state(to_state.strip(), line_num, original_line)
            self._validate_transition_coherence(from_state, to_state, line_num, original_line)
            return
        
        # Validate as regular expression with modifiers
        self._validate_emotional_state(expr, line_num, original_line, is_variable)
    
    def _validate_emotional_state(self, state: str, line_num: int, original_line: str, is_variable: bool = False):
        """Validate emotional state expression"""
        # Split on cultural modifier
        parts = state.split('.')
        base_part = parts[0]
        cultural_context = parts[1] if len(parts) > 1 else None
        
        # Validate cultural context
        if cultural_context:
            self._validate_cultural_context(cultural_context, line_num, original_line)
        
        # Split base part into word and emotions
        emotion_parts = base_part.split('~')
        base_word = emotion_parts[0] if emotion_parts else ""
        emotions = emotion_parts[1:] if len(emotion_parts) > 1 else []
        
        # Validate base word
        if base_word:
            self._validate_base_word(base_word, line_num, original_line, is_variable)
        
        # Validate emotions
        for emotion in emotions:
            self._validate_emotion(emotion, line_num, original_line)
        
        # Check emotional coherence
        if len(emotions) > 1:
            self._validate_emotional_coherence(emotions, line_num, original_line)
    
    def _validate_base_word(self, word: str, line_num: int, original_line: str, is_variable: bool = False):
        """Validate base word"""
        # Check syntax
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', word):
            self.errors.append(ValidationError(
                line_num, original_line.find(word),
                ValidationLevel.SYNTAX,
                f"Invalid word syntax: '{word}'",
                "Words must start with letter or underscore, contain only letters, numbers, and underscores"
            ))
            return
        
        # For variables, more lenient validation
        if is_variable:
            return
        
        # Check if word exists in vocabulary (semantic validation)
        if not self._word_exists_in_vocabulary(word):
            self.errors.append(ValidationError(
                line_num, original_line.find(word),
                ValidationLevel.SEMANTIC,
                f"Unknown word: '{word}'",
                f"Consider adding '{word}' to the lexicon or check spelling"
            ))
    
    def _validate_emotion(self, emotion: str, line_num: int, original_line: str):
        """Validate emotional modifier"""
        # Check syntax
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', emotion):
            self.errors.append(ValidationError(
                line_num, original_line.find(f'~{emotion}'),
                ValidationLevel.SYNTAX,
                f"Invalid emotion syntax: '{emotion}'"
            ))
            return
        
        # Check if emotion is recognized
        if not self._emotion_exists_in_vocabulary(emotion):
            self.errors.append(ValidationError(
                line_num, original_line.find(f'~{emotion}'),
                ValidationLevel.EMOTIONAL,
                f"Unrecognized emotion: '{emotion}'",
                f"Consider adding '{emotion}' to emotional markers or check spelling"
            ))
    
    def _validate_cultural_context(self, context: str, line_num: int, original_line: str):
        """Validate cultural context modifier"""
        # Check syntax
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', context):
            self.errors.append(ValidationError(
                line_num, original_line.find(f'.{context}'),
                ValidationLevel.SYNTAX,
                f"Invalid cultural context syntax: '{context}'"
            ))
            return
        
        # Basic cultural context validation (could be expanded)
        recognized_contexts = {'irish', 'formal', 'casual', 'ancient', 'modern', 'traditional'}
        if context not in recognized_contexts:
            self.errors.append(ValidationError(
                line_num, original_line.find(f'.{context}'),
                ValidationLevel.CULTURAL,
                f"Unrecognized cultural context: '{context}'",
                f"Recognized contexts: {', '.join(sorted(recognized_contexts))}"
            ))
    
    def _validate_emotional_coherence(self, emotions: List[str], line_num: int, original_line: str):
        """Validate emotional coherence between multiple emotions"""
        # Basic contradiction detection
        contradictions = [
            ({'happy', 'joy', 'bright'}, {'sad', 'sorrow', 'dark'}),
            ({'calm', 'peace', 'gentle'}, {'angry', 'fierce', 'rage'}),
            ({'warm', 'hot'}, {'cold', 'icy', 'frozen'})
        ]
        
        emotion_set = set(emotions)
        for positive_set, negative_set in contradictions:
            if emotion_set & positive_set and emotion_set & negative_set:
                self.errors.append(ValidationError(
                    line_num, 0,
                    ValidationLevel.EMOTIONAL,
                    f"Contradictory emotions detected: {', '.join(emotion_set & positive_set)} vs {', '.join(emotion_set & negative_set)}",
                    "Consider using transition operator (>) to show emotional change"
                ))
    
    def _validate_transition_coherence(self, from_state: str, to_state: str, line_num: int, original_line: str):
        """Validate emotional transition makes sense"""
        # This could be expanded with more sophisticated emotional transition rules
        # For now, just ensure they're different
        if from_state.strip() == to_state.strip():
            self.errors.append(ValidationError(
                line_num, original_line.find('>'),
                ValidationLevel.EMOTIONAL,
                f"Transition to same state: '{from_state}' > '{to_state}'",
                "Transitions should show emotional change"
            ))
    
    def _word_exists_in_vocabulary(self, word: str) -> bool:
        """Check if word exists in loaded vocabulary"""
        vocabulary = self.vocabulary.get('vocabulary', {})
        
        for category in vocabulary.values():
            if isinstance(category, dict):
                for entry in category.values():
                    if isinstance(entry, dict):
                        if entry.get('firish') == word:
                            return True
                        if word in entry.get('variants', []):
                            return True
        
        return False
    
    def _emotion_exists_in_vocabulary(self, emotion: str) -> bool:
        """Check if emotion exists in emotional markers"""
        emotional_markers = self.vocabulary.get('vocabulary', {}).get('emotional_markers', {})
        
        for emotion_list in emotional_markers.values():
            if isinstance(emotion_list, list) and emotion in emotion_list:
                return True
        
        # Also check if it's a key in emotional markers
        return emotion in emotional_markers

def main():
    """CLI interface for validator"""
    parser = argparse.ArgumentParser(description="FIRISH Language Validator")
    parser.add_argument('file', help='FIRISH file to validate')
    parser.add_argument('--lexicon', '-l', help='Path to lexicon file')
    parser.add_argument('--level', '-v', choices=['syntax', 'semantic', 'emotional', 'cultural'], 
                       action='append', help='Validation levels to check (default: all)')
    parser.add_argument('--format', choices=['text', 'json'], default='text', 
                       help='Output format')
    
    args = parser.parse_args()
    
    validator = FirishValidator(args.lexicon)
    errors = validator.validate_file(args.file)
    
    # Filter by validation level if specified
    if args.level:
        requested_levels = {ValidationLevel(level) for level in args.level}
        errors = [e for e in errors if e.level in requested_levels]
    
    # Output results
    if args.format == 'json':
        import json
        error_dicts = [
            {
                'line': e.line_number,
                'column': e.column,
                'level': e.level.value,
                'message': e.message,
                'suggestion': e.suggestion
            }
            for e in errors
        ]
        print(json.dumps(error_dicts, indent=2))
    else:
        if not errors:
            print(f"✅ {args.file} is valid FIRISH!")
        else:
            print(f"❌ Found {len(errors)} validation errors in {args.file}:")
            print()
            
            for error in errors:
                level_emoji = {
                    ValidationLevel.SYNTAX: "🔴",
                    ValidationLevel.SEMANTIC: "🟡", 
                    ValidationLevel.EMOTIONAL: "💙",
                    ValidationLevel.CULTURAL: "🟢"
                }
                
                print(f"{level_emoji[error.level]} Line {error.line_number}: {error.message}")
                if error.suggestion:
                    print(f"   💡 {error.suggestion}")
                print()

if __name__ == '__main__':
    main()
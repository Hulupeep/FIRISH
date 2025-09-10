#!/usr/bin/env python3
"""
FIRISH Language Translator CLI Tool
Translates between FIRISH and English, preserving emotional context
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

class FirishTranslator:
    """FIRISH to English translator with emotional context preservation"""
    
    def __init__(self, lexicon_path: Optional[str] = None):
        self.lexicon_path = lexicon_path or self._find_lexicon()
        self.vocabulary = self._load_vocabulary()
        
    def _find_lexicon(self) -> str:
        """Find the lexicon file in the project structure"""
        # Look for lexicon in various locations
        possible_paths = [
            Path(__file__).parent.parent.parent / "lexicon" / "core_vocabulary.json",
            Path("lexicon/core_vocabulary.json"),
            Path("../lexicon/core_vocabulary.json"),
        ]
        
        for path in possible_paths:
            if path.exists():
                return str(path)
        
        # Return default path if not found
        return "lexicon/core_vocabulary.json"
    
    def _load_vocabulary(self) -> Dict:
        """Load vocabulary from JSON lexicon"""
        try:
            with open(self.lexicon_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  Warning: Lexicon file not found at {self.lexicon_path}")
            return {"vocabulary": {}}
        except json.JSONDecodeError:
            print(f"⚠️  Warning: Invalid JSON in lexicon file {self.lexicon_path}")
            return {"vocabulary": {}}
    
    def translate_to_english(self, firish_text: str) -> str:
        """Translate FIRISH text to English"""
        lines = firish_text.strip().split('\n')
        translated_lines = []
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                translated_lines.append(line)
                continue
            
            # Handle assignment statements
            if '=' in line:
                var, value = line.split('=', 1)
                var = var.strip()
                value = value.strip().strip('"')
                
                # Translate the variable name
                translated_var = self._translate_expression(var)
                translated_lines.append(f"{translated_var}: {value}")
            else:
                # Translate standalone expression
                translated = self._translate_expression(line)
                translated_lines.append(translated)
        
        return '\n'.join(translated_lines)
    
    def _translate_expression(self, expression: str) -> str:
        """Translate a single FIRISH expression"""
        # Handle transitions
        if '>' in expression:
            from_part, to_part = expression.split('>', 1)
            from_translated = self._translate_word_with_modifiers(from_part.strip())
            to_translated = self._translate_word_with_modifiers(to_part.strip())
            return f"transforming from {from_translated} to {to_translated}"
        
        # Handle regular expressions
        return self._translate_word_with_modifiers(expression)
    
    def _translate_word_with_modifiers(self, word_expr: str) -> str:
        """Translate word with emotional and cultural modifiers"""
        parts = word_expr.split('.')
        base_part = parts[0]
        cultural_context = parts[1] if len(parts) > 1 else None
        
        # Split base part into word and emotions
        emotion_parts = base_part.split('~')
        base_word = emotion_parts[0]
        emotions = emotion_parts[1:] if len(emotion_parts) > 1 else []
        
        # Translate base word
        translated_base = self._translate_base_word(base_word)
        
        # Add emotional context
        if emotions:
            emotion_desc = self._translate_emotions(emotions)
            if len(emotions) == 1:
                translated_base = f"{emotion_desc} {translated_base}"
            else:
                translated_base = f"{translated_base} with {emotion_desc}"
        
        # Add cultural context
        if cultural_context:
            translated_base = f"{translated_base} (in {cultural_context} tradition)"
        
        return translated_base
    
    def _translate_base_word(self, word: str) -> str:
        """Translate base word using vocabulary"""
        vocabulary = self.vocabulary.get('vocabulary', {})
        
        # Search through vocabulary categories
        for category in vocabulary.values():
            if isinstance(category, dict):
                for entry_key, entry_data in category.items():
                    if isinstance(entry_data, dict) and entry_data.get('firish') == word:
                        return word  # Return the word itself for now
        
        # If not found in vocabulary, return as-is
        return word
    
    def _translate_emotions(self, emotions: List[str]) -> str:
        """Translate emotional modifiers to descriptive English"""
        emotion_map = {
            'warm': 'warmly',
            'cold': 'coldly', 
            'bright': 'brightly',
            'dark': 'darkly',
            'deep': 'deeply',
            'gentle': 'gently',
            'fierce': 'fiercely',
            'calm': 'calmly',
            'peaceful': 'peacefully',
            'joyful': 'joyfully',
            'sad': 'sadly',
            'angry': 'angrily'
        }
        
        translated_emotions = [emotion_map.get(emotion, emotion) for emotion in emotions]
        
        if len(translated_emotions) == 1:
            return translated_emotions[0]
        elif len(translated_emotions) == 2:
            return f"{translated_emotions[0]} and {translated_emotions[1]}"
        else:
            return ", ".join(translated_emotions[:-1]) + f", and {translated_emotions[-1]}"

def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(
        description="FIRISH Language Translator - Convert between FIRISH and English",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --to-english "hello~warm"
  %(prog)s --to-english --file examples/basic_greetings.firish
  %(prog)s --interactive
        """
    )
    
    parser.add_argument(
        '--to-english', 
        help='Translate FIRISH text to English'
    )
    
    parser.add_argument(
        '--file', '-f',
        help='Translate content from file'
    )
    
    parser.add_argument(
        '--lexicon', '-l',
        help='Path to lexicon file (JSON format)'
    )
    
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Start interactive translation mode'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Output file (default: stdout)'
    )
    
    args = parser.parse_args()
    
    # Create translator
    translator = FirishTranslator(args.lexicon)
    
    # Handle different modes
    if args.interactive:
        run_interactive_mode(translator)
    elif args.file:
        translate_file(translator, args.file, args.output)
    elif args.to_english:
        result = translator.translate_to_english(args.to_english)
        output_result(result, args.output)
    else:
        parser.print_help()

def run_interactive_mode(translator: FirishTranslator):
    """Run interactive translation mode"""
    print("🌊 FIRISH Interactive Translator")
    print("Enter FIRISH expressions (or 'quit' to exit):")
    print("=" * 40)
    
    while True:
        try:
            user_input = input("FIRISH> ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Slán! (Goodbye!)")
                break
            
            if user_input:
                result = translator.translate_to_english(user_input)
                print(f"English: {result}")
                print()
        
        except KeyboardInterrupt:
            print("\nSlán! (Goodbye!)")
            break
        except EOFError:
            break

def translate_file(translator: FirishTranslator, input_file: str, output_file: Optional[str]):
    """Translate entire file"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        result = translator.translate_to_english(content)
        output_result(result, output_file)
        
        print(f"✅ Translated {input_file}")
        if output_file:
            print(f"   Output saved to {output_file}")
    
    except FileNotFoundError:
        print(f"❌ File not found: {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error translating file: {e}")
        sys.exit(1)

def output_result(result: str, output_file: Optional[str]):
    """Output result to file or stdout"""
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
    else:
        print(result)

if __name__ == '__main__':
    main()
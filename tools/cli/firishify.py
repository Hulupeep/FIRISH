#!/usr/bin/env python3
"""
Firishify CLI Tool - Convert English text to Firish using the EASE algorithm

Firish is a playful cryptolect mixing English, French, and Irish using the EASE rule:
at each word, pick the easiest/fastest option that your partner understands 
but an 8-year-old overhearing is least likely to decode.

Usage:
    python firishify.py "your text here"
    python firishify.py --opacity mid "your text here"
    python firishify.py --help

Author: Firish Language Project
License: MIT
"""

import argparse
import csv
import os
import re
import sys
from typing import Dict, List, Optional, Tuple, NamedTuple
from pathlib import Path

class LexiconEntry(NamedTuple):
    """Represents a single lexicon entry with multiple language options"""
    english: str
    irish: str
    french: str
    pos: str  # part of speech
    opacity_low: str
    opacity_mid: str
    opacity_high: str
    category: str

class FirishConverter:
    """Main class for converting English text to Firish using EASE algorithm"""
    
    def __init__(self, lexicon_path: Optional[str] = None):
        """Initialize converter with lexicon data"""
        self.lexicon: Dict[str, LexiconEntry] = {}
        self.irish_particles = {
            'an': 'an',  # the/question particle
            'ní': 'ní',  # negative particle
            'tá': 'tá',  # is/state particle
            'níl': 'níl',  # is not
            'ar': 'ar',  # on
            'le': 'le',  # with
            'do': 'do',  # to/for
            'faoi': 'faoi',  # about
            'go': 'go',  # to
            'ó': 'ó',  # from
            'má': 'má',  # if
            'agus': 'agus',  # and
        }
        
        # Load lexicon data
        if lexicon_path is None:
            # Default path relative to this script
            script_dir = Path(__file__).parent
            lexicon_path = script_dir.parent.parent / "lexicon" / "dictionary.csv"
        
        self.load_lexicon(lexicon_path)
    
    def load_lexicon(self, lexicon_path: Path) -> None:
        """Load the lexicon from CSV file"""
        try:
            with open(lexicon_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    entry = LexiconEntry(
                        english=row['english'].lower(),
                        irish=row['irish'],
                        french=row['french'], 
                        pos=row['pos'],
                        opacity_low=row['opacity_low'],
                        opacity_mid=row['opacity_mid'],
                        opacity_high=row['opacity_high'],
                        category=row['category']
                    )
                    self.lexicon[entry.english] = entry
                    
            print(f"Loaded {len(self.lexicon)} entries from lexicon", file=sys.stderr)
                    
        except FileNotFoundError:
            print(f"Error: Lexicon file not found at {lexicon_path}", file=sys.stderr)
            print("Please ensure the dictionary.csv file exists in the lexicon/ directory", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error loading lexicon: {e}", file=sys.stderr)
            sys.exit(1)
    
    def normalize_word(self, word: str) -> str:
        """Normalize word for lexicon lookup - remove punctuation but keep apostrophes"""
        # Remove punctuation except apostrophes, convert to lowercase
        cleaned = re.sub(r'[^\w\s\']', '', word.lower())
        return cleaned
    
    def apply_ease_algorithm(self, word: str, opacity: str) -> str:
        """
        Apply the EASE algorithm to select the best word form
        
        EASE principles:
        1. Fastest to say
        2. Least likely understood by child 
        3. Still clear to partner
        
        Args:
            word: The English word to convert
            opacity: 'low', 'mid', or 'high'
            
        Returns:
            The selected word form based on opacity level
        """
        normalized = self.normalize_word(word)
        
        # Check if word is in lexicon
        if normalized in self.lexicon:
            entry = self.lexicon[normalized]
            
            if opacity == 'low':
                return entry.opacity_low
            elif opacity == 'mid': 
                return entry.opacity_mid
            elif opacity == 'high':
                return entry.opacity_high
                
        # Handle Irish particles - always use them for opacity
        if normalized in self.irish_particles:
            return self.irish_particles[normalized]
            
        # Fallback: return original word if not in lexicon
        return word
    
    def handle_questions(self, text: str, opacity: str) -> str:
        """Handle question formation using Irish question particles"""
        text_lower = text.lower().strip()
        
        # Question patterns that should use "An" particle
        question_patterns = [
            r'^are\s+you',
            r'^do\s+you', 
            r'^did\s+you',
            r'^can\s+you',
            r'^will\s+you',
            r'^would\s+you'
        ]
        
        for pattern in question_patterns:
            if re.match(pattern, text_lower):
                # Replace with Irish question particle
                if opacity in ['mid', 'high']:
                    # Use Irish question particle "An"
                    modified = re.sub(pattern, 'An', text, flags=re.IGNORECASE)
                    return modified
                    
        return text
    
    def handle_negation(self, text: str, opacity: str) -> str:
        """Handle negation using Irish negative particles"""
        # Common negative patterns
        negation_patterns = [
            (r'\bnot\b', 'ní'),
            (r'\bdon\'t\b', 'ní'),
            (r'\bdoesn\'t\b', 'ní'), 
            (r'\bdidn\'t\b', 'ní'),
            (r'\bwon\'t\b', 'ní'),
            (r'\bcan\'t\b', 'ní féidir'),
            (r'\bisn\'t\b', 'níl')
        ]
        
        if opacity in ['mid', 'high']:
            for pattern, replacement in negation_patterns:
                text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
                
        return text
    
    def generate_echo_response(self, question: str) -> str:
        """Generate Irish-style echo responses for yes/no questions"""
        question_lower = question.lower().strip()
        
        # Map common question verbs to their echo responses
        echo_patterns = [
            (r'\bare\s+you', 'Tá (yes) / Níl (no)'),
            (r'\bdo\s+you', 'Déanaim (yes) / Ní dhéanaim (no)'),
            (r'\bcan\s+you', 'Is féidir (yes) / Ní féidir (no)'),
            (r'\bwill\s+you', 'Déanfaidh (yes) / Ní dhéanfaidh (no)'),
            (r'\bdid\s+you', 'Rinne (yes) / Ní dhearna (no)')
        ]
        
        for pattern, response in echo_patterns:
            if re.search(pattern, question_lower):
                return f"\n[Echo response: {response}]"
                
        return ""
    
    def convert_text(self, text: str, opacity: str = 'low') -> str:
        """
        Convert English text to Firish using the EASE algorithm
        
        Args:
            text: Input English text
            opacity: Opacity level ('low', 'mid', 'high')
            
        Returns:
            Converted Firish text
        """
        if not text.strip():
            return text
            
        # Handle questions first
        text = self.handle_questions(text, opacity)
        
        # Handle negation
        text = self.handle_negation(text, opacity)
        
        # Split into words while preserving punctuation and spacing
        words = re.findall(r'\w+[\'\w]*|[^\w\s]|\s+', text)
        
        converted_words = []
        
        for word in words:
            if word.isspace() or not word.isalpha():
                # Keep whitespace and punctuation as-is
                converted_words.append(word)
            else:
                # Apply EASE algorithm to convert word
                converted_word = self.apply_ease_algorithm(word, opacity)
                converted_words.append(converted_word)
        
        result = ''.join(converted_words)
        
        # Add echo response hint for questions
        if text.strip().endswith('?'):
            echo = self.generate_echo_response(text)
            result += echo
            
        return result
    
    def print_conversion_info(self, original: str, converted: str, opacity: str):
        """Print helpful conversion information"""
        print(f"\n--- Firish Conversion (Opacity: {opacity}) ---")
        print(f"Original:  {original}")
        print(f"Firish:    {converted}")
        print(f"\nEASE Algorithm Applied:")
        print(f"- Opacity level: {opacity}")
        print(f"- Mixed EN/FR/GA based on accessibility and discretion")
        
        if converted.endswith('?') or 'An ' in converted:
            print(f"- Question detected: Using Irish particles")
        if 'ní' in converted.lower():
            print(f"- Negation detected: Using Irish negative particles")

def create_test_examples() -> List[Tuple[str, str]]:
    """Create test examples for validation"""
    return [
        ("Are you ready for breakfast?", "low"),
        ("I want to go shopping", "mid"), 
        ("Let's go home now", "high"),
        ("Can you buy snacks at the shop?", "mid"),
        ("The homework is too hard", "high"),
        ("We need to talk about the party", "mid"),
        ("Don't forget your bag", "low"),
        ("She is tired and wants to sleep", "mid"),
        ("When is dinner ready?", "low"),
        ("I don't understand the teacher", "high")
    ]

def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(
        description="Convert English text to Firish using the EASE algorithm",
        epilog="""
Examples:
  %(prog)s "Are you ready for breakfast?"
  %(prog)s --opacity mid "I want to go shopping"
  %(prog)s --opacity high "Let's go home now"
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'text',
        nargs='?',
        help='English text to convert to Firish'
    )
    
    parser.add_argument(
        '--opacity',
        choices=['low', 'mid', 'high'],
        default='low',
        help='Opacity level: low (family-friendly), mid (public privacy), high (maximum discretion)'
    )
    
    parser.add_argument(
        '--lexicon',
        help='Path to custom lexicon CSV file'
    )
    
    parser.add_argument(
        '--examples',
        action='store_true',
        help='Show conversion examples and exit'
    )
    
    parser.add_argument(
        '--test',
        action='store_true', 
        help='Run test conversions and exit'
    )
    
    args = parser.parse_args()
    
    # Initialize converter
    try:
        converter = FirishConverter(args.lexicon)
    except Exception as e:
        print(f"Error initializing converter: {e}", file=sys.stderr)
        return 1
    
    # Handle examples mode
    if args.examples:
        print("Firish Conversion Examples:")
        print("==========================")
        examples = [
            ("Are you ready?", "low"),
            ("I want to buy sweets", "mid"),  
            ("Let's go to the shop", "high"),
            ("Can you help me?", "mid"),
            ("The homework is hard", "high")
        ]
        
        for text, opacity in examples:
            converted = converter.convert_text(text, opacity)
            print(f"\nOpacity {opacity}: '{text}' -> '{converted}'")
        return 0
    
    # Handle test mode
    if args.test:
        print("Running Firish Converter Tests:")
        print("===============================")
        test_examples = create_test_examples()
        
        for text, opacity in test_examples:
            try:
                converted = converter.convert_text(text, opacity)
                print(f"✓ {opacity.upper()}: '{text}' -> '{converted}'")
            except Exception as e:
                print(f"✗ ERROR: {text} -> {e}")
                
        print(f"\nCompleted {len(test_examples)} test conversions")
        return 0
    
    # Handle text conversion
    if not args.text:
        print("Error: Please provide text to convert or use --examples/--test", file=sys.stderr)
        parser.print_help()
        return 1
    
    try:
        converted = converter.convert_text(args.text, args.opacity)
        converter.print_conversion_info(args.text, converted, args.opacity)
        
    except Exception as e:
        print(f"Error during conversion: {e}", file=sys.stderr)
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
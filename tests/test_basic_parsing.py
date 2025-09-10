#!/usr/bin/env python3
"""
Basic parsing tests for FIRISH language implementation
Tests core grammar and emotional modifier parsing
"""

import unittest
import re
from typing import Dict, List, Optional, Tuple

class FirishParser:
    """Basic FIRISH language parser for testing"""
    
    def __init__(self):
        self.emotional_pattern = r'~([a-zA-Z_]+)'
        self.cultural_pattern = r'\.([a-zA-Z_]+)'
        self.transition_pattern = r'([a-zA-Z_~]+)>([a-zA-Z_~]+)'
    
    def parse_statement(self, statement: str) -> Dict:
        """Parse a FIRISH statement into components"""
        result = {
            'base_word': None,
            'emotions': [],
            'cultural_context': None,
            'transition': None,
            'raw': statement.strip()
        }
        
        # Handle transitions first
        transition_match = re.search(self.transition_pattern, statement)
        if transition_match:
            from_state, to_state = transition_match.groups()
            result['transition'] = {
                'from': from_state,
                'to': to_state
            }
            # Remove transition from statement for further parsing
            statement = re.sub(self.transition_pattern, '', statement)
        
        # Extract emotional modifiers
        emotions = re.findall(self.emotional_pattern, statement)
        result['emotions'] = emotions
        
        # Extract cultural context
        cultural_match = re.search(self.cultural_pattern, statement)
        if cultural_match:
            result['cultural_context'] = cultural_match.group(1)
        
        # Extract base word (what remains after removing modifiers)
        base = statement
        base = re.sub(self.emotional_pattern, '', base)
        base = re.sub(self.cultural_pattern, '', base)
        base = base.strip()
        result['base_word'] = base if base else None
        
        return result

class TestFirishParsing(unittest.TestCase):
    """Test cases for FIRISH language parsing"""
    
    def setUp(self):
        self.parser = FirishParser()
    
    def test_simple_word(self):
        """Test parsing simple words without modifiers"""
        result = self.parser.parse_statement("hello")
        self.assertEqual(result['base_word'], "hello")
        self.assertEqual(result['emotions'], [])
        self.assertIsNone(result['cultural_context'])
    
    def test_emotional_modifier(self):
        """Test parsing words with emotional modifiers"""
        result = self.parser.parse_statement("hello~warm")
        self.assertEqual(result['base_word'], "hello")
        self.assertEqual(result['emotions'], ["warm"])
    
    def test_multiple_emotions(self):
        """Test parsing words with multiple emotional modifiers"""
        result = self.parser.parse_statement("feeling~happy~nervous")
        self.assertEqual(result['base_word'], "feeling")
        self.assertEqual(set(result['emotions']), {"happy", "nervous"})
    
    def test_cultural_context(self):
        """Test parsing words with cultural context"""
        result = self.parser.parse_statement("greeting.irish")
        self.assertEqual(result['base_word'], "greeting")
        self.assertEqual(result['cultural_context'], "irish")
    
    def test_complex_expression(self):
        """Test parsing complex expressions with multiple modifiers"""
        result = self.parser.parse_statement("love~deep.irish")
        self.assertEqual(result['base_word'], "love")
        self.assertEqual(result['emotions'], ["deep"])
        self.assertEqual(result['cultural_context'], "irish")
    
    def test_transition(self):
        """Test parsing emotional transitions"""
        result = self.parser.parse_statement("sad>happy")
        self.assertIsNotNone(result['transition'])
        self.assertEqual(result['transition']['from'], "sad")
        self.assertEqual(result['transition']['to'], "happy")
    
    def test_complex_transition(self):
        """Test parsing transitions with emotional modifiers"""
        result = self.parser.parse_statement("sad~deep>happy~bright")
        self.assertIsNotNone(result['transition'])
        self.assertEqual(result['transition']['from'], "sad~deep")
        self.assertEqual(result['transition']['to'], "happy~bright")
    
    def test_empty_string(self):
        """Test parsing empty strings"""
        result = self.parser.parse_statement("")
        self.assertIsNone(result['base_word'])
        self.assertEqual(result['emotions'], [])
    
    def test_whitespace_handling(self):
        """Test proper handling of whitespace"""
        result = self.parser.parse_statement("  hello~warm  ")
        self.assertEqual(result['base_word'], "hello")
        self.assertEqual(result['emotions'], ["warm"])

class TestFirishSemantics(unittest.TestCase):
    """Test semantic validation and meaning extraction"""
    
    def setUp(self):
        self.parser = FirishParser()
        # Basic emotion validation (would be expanded with proper lexicon)
        self.valid_emotions = {
            'happy', 'sad', 'angry', 'peaceful', 'warm', 'cold',
            'bright', 'dark', 'deep', 'gentle', 'fierce', 'calm'
        }
    
    def validate_emotions(self, emotions: List[str]) -> bool:
        """Validate that emotions are recognized"""
        return all(emotion in self.valid_emotions for emotion in emotions)
    
    def test_valid_emotions(self):
        """Test recognition of valid emotions"""
        result = self.parser.parse_statement("greeting~warm~gentle")
        self.assertTrue(self.validate_emotions(result['emotions']))
    
    def test_emotional_coherence(self):
        """Test basic emotional coherence (would be more complex in full implementation)"""
        # This would test for contradictory emotions, etc.
        result = self.parser.parse_statement("smile~bright~happy")
        emotions = result['emotions']
        # Basic test: bright and happy are coherent
        self.assertIn('bright', emotions)
        self.assertIn('happy', emotions)

if __name__ == '__main__':
    print("🔍 Running FIRISH Language Parser Tests")
    print("=" * 50)
    
    # Run the tests
    unittest.main(verbosity=2)
#!/usr/bin/env python3
"""
Compare Rule-based vs LLM Firish Translation
"""

import sys
import os
from pathlib import Path

# Import both CLI tools
try:
    from firishify import translate_to_firish as rule_translate
except ImportError:
    rule_translate = None

try:
    from firish_llm import FirishLLM
    llm = FirishLLM()
except ImportError:
    llm = None

def compare_translations(text, context="family, casual, medium"):
    """Compare rule-based vs LLM translation"""
    print(f"🔤 Original: {text}")
    print(f"📍 Context: [{context}]")
    print()
    
    # Rule-based translation
    if rule_translate:
        try:
            rule_result = rule_translate(text)
            print(f"⚙️  Rule-based: {rule_result}")
        except Exception as e:
            print(f"⚙️  Rule-based: ❌ Error: {e}")
    else:
        print(f"⚙️  Rule-based: ❌ Not available")
    
    # LLM translation
    if llm and llm.model:
        try:
            llm_result = llm.translate(text, context)
            print(f"🤖 LLM-based:  {llm_result}")
        except Exception as e:
            print(f"🤖 LLM-based:  ❌ Error: {e}")
    else:
        print(f"🤖 LLM-based:  ❌ Model not loaded")
    
    print("-" * 60)

def main():
    if len(sys.argv) < 2:
        print("Usage: python firish_compare.py 'text to translate'")
        print("       python firish_compare.py 'text' 'context'")
        sys.exit(1)
    
    text = sys.argv[1]
    context = sys.argv[2] if len(sys.argv) > 2 else "family, casual, medium"
    
    print("🔥 Firish Translation Comparison")
    print("=" * 60)
    compare_translations(text, context)

if __name__ == "__main__":
    main()
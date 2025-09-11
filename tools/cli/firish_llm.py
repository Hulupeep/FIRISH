#!/usr/bin/env python3
"""
Firish LLM Translation Tool
Uses fine-tuned T5-small model for Firish translation
"""

import argparse
import sys
import os
from pathlib import Path

try:
    from transformers import T5Tokenizer, T5ForConditionalGeneration
    import torch
except ImportError:
    print("❌ Required packages not installed. Run: pip install transformers torch")
    sys.exit(1)

class FirishLLM:
    def __init__(self, model_path=None):
        if model_path is None:
            # Default to models directory relative to script
            script_dir = Path(__file__).parent.parent.parent
            model_path = script_dir / "models" / "t5-firish"
        
        self.model_path = Path(model_path)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = None
        self.tokenizer = None
        
        if self.model_path.exists():
            self.load_model()
        else:
            print(f"❌ Model not found at {self.model_path}")
            print("💡 Run 'python download_model.py' to get the trained model")
    
    def load_model(self):
        """Load the fine-tuned T5 model"""
        try:
            print(f"📥 Loading Firish T5 model from {self.model_path}")
            self.tokenizer = T5Tokenizer.from_pretrained(str(self.model_path))
            self.model = T5ForConditionalGeneration.from_pretrained(str(self.model_path))
            self.model.to(self.device)
            self.model.eval()
            print(f"✅ Model loaded on {self.device}")
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            sys.exit(1)
    
    def translate(self, text, context="family, casual, medium"):
        """Translate English text to Firish using the LLM"""
        if not self.model:
            return "❌ Model not loaded"
        
        # Format input for T5
        input_text = f"translate to firish [{context}]: {text}"
        
        # Tokenize and move to device
        inputs = self.tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        try:
            # Generate translation
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs['input_ids'],
                    max_length=100,
                    num_return_sequences=1,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=self.tokenizer.pad_token_id,
                    early_stopping=True
                )
            
            # Decode result
            result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return result
            
        except Exception as e:
            return f"❌ Translation error: {e}"
    
    def batch_translate(self, texts, context="family, casual, medium"):
        """Translate multiple texts"""
        results = []
        for text in texts:
            result = self.translate(text, context)
            results.append(result)
        return results

def main():
    parser = argparse.ArgumentParser(description="Firish LLM Translation Tool")
    parser.add_argument("text", nargs="?", help="Text to translate")
    parser.add_argument("-c", "--context", default="family, casual, medium",
                      help="Context for translation (e.g., 'parents, child nearby, high')")
    parser.add_argument("-i", "--interactive", action="store_true",
                      help="Interactive mode")
    parser.add_argument("-f", "--file", help="Translate text from file")
    parser.add_argument("--model-path", help="Path to model directory")
    
    args = parser.parse_args()
    
    # Initialize LLM
    llm = FirishLLM(args.model_path)
    
    if args.interactive:
        print("🔥 Firish LLM Interactive Mode")
        print("Enter text to translate (Ctrl+C to exit)")
        print("Format: [context] text")
        print("Example: [parents, child nearby, high] We need to leave now")
        print()
        
        try:
            while True:
                user_input = input("firish-llm> ").strip()
                if not user_input:
                    continue
                
                # Parse context if provided
                context = args.context
                text = user_input
                
                if user_input.startswith('[') and ']' in user_input:
                    end_bracket = user_input.index(']')
                    context = user_input[1:end_bracket]
                    text = user_input[end_bracket + 1:].strip()
                
                if text:
                    result = llm.translate(text, context)
                    print(f"🔥 {result}")
                    print()
        
        except KeyboardInterrupt:
            print("\n👋 Slán go fóill!")
            sys.exit(0)
    
    elif args.file:
        # Translate from file
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            print(f"📝 Translating {len(lines)} lines from {args.file}")
            results = llm.batch_translate([line.strip() for line in lines], args.context)
            
            for original, translation in zip(lines, results):
                print(f"EN: {original.strip()}")
                print(f"FI: {translation}")
                print()
        
        except FileNotFoundError:
            print(f"❌ File not found: {args.file}")
            sys.exit(1)
    
    elif args.text:
        # Single translation
        result = llm.translate(args.text, args.context)
        print(f"Context: [{args.context}]")
        print(f"English: {args.text}")
        print(f"Firish:  {result}")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
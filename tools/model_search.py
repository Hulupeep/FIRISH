#!/usr/bin/env python3
"""
Search Hugging Face Hub for models suitable for Firish translation
"""

try:
    from huggingface_hub import HfApi
    import pandas as pd
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.run(["pip", "install", "huggingface_hub", "pandas"], check=True)
    from huggingface_hub import HfApi
    import pandas as pd

def search_models():
    api = HfApi()
    
    print("🔍 Searching for Translation Models suitable for Firish...\n")
    
    # Search for translation models
    print("=" * 60)
    print("📚 TRANSLATION MODELS")
    print("=" * 60)
    
    translation_models = api.list_models(
        task="translation",
        sort="downloads",
        direction=-1,
        limit=10
    )
    
    for i, model in enumerate(translation_models, 1):
        print(f"{i}. {model.id}")
        print(f"   Downloads: {model.downloads:,}")
        if hasattr(model, 'tags') and model.tags:
            relevant_tags = [tag for tag in model.tags if any(lang in tag.lower() for lang in ['multilingual', 'french', 'irish', 'celtic', 'gaelic'])]
            if relevant_tags:
                print(f"   Relevant tags: {', '.join(relevant_tags)}")
        print()
    
    # Search for multilingual models
    print("=" * 60)  
    print("🌍 MULTILINGUAL MODELS")
    print("=" * 60)
    
    multilingual_models = api.list_models(
        search="multilingual",
        sort="downloads", 
        direction=-1,
        limit=10
    )
    
    for i, model in enumerate(multilingual_models, 1):
        print(f"{i}. {model.id}")
        print(f"   Downloads: {model.downloads:,}")
        if hasattr(model, 'pipeline_tag'):
            print(f"   Task: {model.pipeline_tag}")
        print()
    
    # Search for French-specific models
    print("=" * 60)
    print("🇫🇷 FRENCH LANGUAGE MODELS")  
    print("=" * 60)
    
    french_models = api.list_models(
        search="french english",
        sort="downloads",
        direction=-1, 
        limit=8
    )
    
    for i, model in enumerate(french_models, 1):
        print(f"{i}. {model.id}")
        print(f"   Downloads: {model.downloads:,}")
        if hasattr(model, 'pipeline_tag'):
            print(f"   Task: {model.pipeline_tag}")
        print()
    
    # Search for Irish/Celtic models
    print("=" * 60)
    print("🇮🇪 IRISH/CELTIC LANGUAGE MODELS")
    print("=" * 60)
    
    irish_searches = ["irish", "gaelic", "celtic", "irish-english"]
    found_irish = False
    
    for search_term in irish_searches:
        try:
            irish_models = api.list_models(
                search=search_term,
                sort="downloads",
                direction=-1,
                limit=5
            )
            
            for model in irish_models:
                if any(term in model.id.lower() for term in ['irish', 'gaelic', 'celtic', 'ga']):
                    print(f"• {model.id}")
                    print(f"  Downloads: {model.downloads:,}")
                    if hasattr(model, 'pipeline_tag'):
                        print(f"  Task: {model.pipeline_tag}")
                    print()
                    found_irish = True
        except Exception as e:
            continue
    
    if not found_irish:
        print("No specific Irish/Celtic models found with significant downloads.")
        print()
    
    # Search for context-aware models
    print("=" * 60)
    print("🧠 CONTEXT-AWARE & INSTRUCTION MODELS")
    print("=" * 60)
    
    context_searches = ["instruction", "chat", "context"]
    for search_term in context_searches:
        try:
            context_models = api.list_models(
                search=search_term,
                sort="downloads",
                direction=-1,
                limit=3
            )
            
            print(f"\n{search_term.upper()} Models:")
            for model in context_models:
                if model.downloads > 1000:  # Filter for popular models
                    print(f"• {model.id}")
                    print(f"  Downloads: {model.downloads:,}")
                    print()
        except Exception as e:
            continue

def main():
    try:
        search_models()
        
        print("=" * 60)
        print("🎯 RECOMMENDATIONS FOR FIRISH")
        print("=" * 60)
        print("""
For Firish translation, we need models that can:
1. Handle multilingual mixing (EN/FR/GA)
2. Understand context for appropriate obfuscation
3. Maintain conversational flow
4. Support fine-tuning for specific patterns

Best candidates to explore:
• Multilingual models (mT5, mBART) for language mixing
• Instruction-tuned models for context awareness  
• Translation models as base for fine-tuning
• Small models suitable for local deployment
        """)
        
    except Exception as e:
        print(f"Error searching models: {e}")
        print("Try: pip install huggingface_hub pandas")

if __name__ == "__main__":
    main()
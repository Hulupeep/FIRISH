#!/usr/bin/env python3
"""
Create training dataset for T5-small Firish fine-tuning from authentic examples
"""

import json
import csv
from pathlib import Path

def create_training_data():
    """Create comprehensive training dataset from our authentic Firish examples"""
    
    # Base training examples from our corrections
    training_examples = []
    
    print("🔍 Creating Authentic Firish Training Dataset...")
    print("=" * 60)
    
    # 1. Correction Examples (from training-data-evals.firish.md)
    correction_examples = [
        # Restaurant scenarios
        {
            "input": "translate to firish [restaurant, strangers, medium]: The bill is expensive",
            "output": "Le bil-allachta est cher"
        },
        {
            "input": "translate to firish [restaurant, couple, high]: Look at the bill. It's big. How much tip?",
            "output": "Regarde le bil-allachta. Tá sé mór. Cé mhéid tip-ach?"
        },
        
        # Homework coordination
        {
            "input": "translate to firish [parents, child nearby, medium]: Is the homework finished?",
            "output": "An bhfuil an obair maison finis?"
        },
        {
            "input": "translate to firish [parents, coordination, medium]: Did they finish their homework?",
            "output": "An bhfuil siad finis leur obair maison?"
        },
        
        # Shopping coordination
        {
            "input": "translate to firish [family, planning, medium]: We need groceries for the weekend",
            "output": "Nous avons besoin groceries-ach pour le weekend-achta"
        },
        
        # Bedtime scenarios
        {
            "input": "translate to firish [parents, bedtime, low]: Are they ready for sleep?",
            "output": "Tá siad ready-ach pour sleep?"
        },
        
        # Time pressure scenarios
        {
            "input": "translate to firish [urgent, public, high]: Hurry up! We are late for the appointment with accountant",
            "output": "Hurryup-achta! Nous sommes en retard pour rendezvous avec accountant-allachta"
        },
        
        # Morning routines
        {
            "input": "translate to firish [morning, child nearby, low]: Are they awake? School starts soon",
            "output": "An bhfuil siad awake-ach encore? School-allachta commence bientôt"
        },
        
        # Dinner planning
        {
            "input": "translate to firish [family, meal planning, medium]: What are we cooking tonight? Pasta or rice?",
            "output": "Qu'est-ce que nous cooking-ach ce soir? Pasta ou rice-allachta?"
        },
        
        # Phone calls
        {
            "input": "translate to firish [phone, quick coordination, medium]: Are you busy now? Quick question for you",
            "output": "An bhfuil tú busy-ach maintenant? Quick-allachta question pour toi"
        },
        
        # Weather coordination
        {
            "input": "translate to firish [family, weather, medium]: It's raining outside. Umbrella necessary",
            "output": "Tá sé raining-allachta dehors. Umbrella-ach nécessaire"
        },
        
        # Work discussions
        {
            "input": "translate to firish [couple, work planning, medium]: Is work finished today? Home early possible?",
            "output": "An work-ach fini aujourd'hui? Home-allachta early possible?"
        },
        
        # Child behavior
        {
            "input": "translate to firish [parents, child management, medium]: They are very loud. Quiet please!",
            "output": "Siad très loud-ach. Quiet-allachta s'il vous plaît!"
        },
        
        # Shopping lists
        {
            "input": "translate to firish [family, shopping, low]: We forgot milk and bread for tomorrow",
            "output": "Nous oublions milk-ach et bread-allachta pour tomorrow-ach"
        },
        
        # Evening plans
        {
            "input": "translate to firish [couple, evening, low]: Movie tonight or book reading together?",
            "output": "Movie-ach ce soir ou book-allachta reading ensemble?"
        }
    ]
    
    training_examples.extend(correction_examples)
    
    # 2. Context Variations - Same content, different contexts
    base_scenarios = [
        ("Should we check their homework?", [
            ("translate to firish [parents, child present, low]", "An bhfuil nous check leur obair maison?"),
            ("translate to firish [parents, child nearby, medium]", "An bhfuil nous check-ach leur obair maison?"),
            ("translate to firish [parents, strangers nearby, high]", "An bhfuil nous vérifier-ach leur travail-allachta maison?")
        ]),
        
        ("The bill is too expensive", [
            ("translate to firish [couple, private, low]", "Le bil est trop cher"),
            ("translate to firish [couple, restaurant, medium]", "Le bil-allachta est trop cher"),
            ("translate to firish [couple, strangers listening, high]", "Le bil-allachta est très expensive-ach")
        ]),
        
        ("Are you ready for breakfast?", [
            ("translate to firish [parent-child, morning, low]", "An bhfuil tú ready pour breakfast?"),
            ("translate to firish [family, morning rush, medium]", "An bhfuil tú ready-ach pour breakfast?"),
            ("translate to firish [family, guests present, high]", "An bhfuil tú prêt-ach pour petit-déjeuner-allachta?")
        ]),
        
        ("We need to go shopping", [
            ("translate to firish [family, planning, low]", "Muid gá go shopping"),
            ("translate to firish [parents, coordination, medium]", "Nous besoin aller shopping-ach"),
            ("translate to firish [parents, child listening, high]", "Nous devons aller courses-allachta")
        ])
    ]
    
    for english, variations in base_scenarios:
        for context, firish in variations:
            training_examples.append({
                "input": f"{context}: {english}",
                "output": firish
            })
    
    # 3. Professional/Specific Term Examples
    professional_examples = [
        {
            "input": "translate to firish [adults, appointment planning, high]: Meeting at three with the accountant",
            "output": "Rendezvous à trois avec accountant-allachta"
        },
        {
            "input": "translate to firish [couple, medical, high]: Doctor appointment tomorrow morning",
            "output": "Rendez-vous doctor-ach tomorrow-ach matin"
        },
        {
            "input": "translate to firish [parents, school coordination, medium]: Parent-teacher meeting after school",
            "output": "Parent-teacher meeting-ach après école"
        }
    ]
    
    training_examples.extend(professional_examples)
    
    # 4. Negative/Correction Examples (what NOT to do)
    negative_examples = [
        {
            "input": "translate to firish [family, basic, low]: I want to eat now",
            "output": "Je veux manger maintenant"  # No English concealment needed for basic concepts
        },
        {
            "input": "translate to firish [family, simple, low]: Good morning everyone",
            "output": "Bonjour tout le monde"  # Use well-known French
        }
    ]
    
    training_examples.extend(negative_examples)
    
    print(f"📊 Created {len(training_examples)} training examples")
    
    # Create validation data (hold out 20% for testing)
    import random
    random.seed(42)
    random.shuffle(training_examples)
    
    split_idx = int(0.8 * len(training_examples))
    train_data = training_examples[:split_idx]
    val_data = training_examples[split_idx:]
    
    print(f"📈 Training set: {len(train_data)} examples")
    print(f"🔍 Validation set: {len(val_data)} examples")
    
    # Save as JSON for T5 training
    train_output = {
        "data": [
            {
                "input_text": example["input"],
                "target_text": example["output"]
            }
            for example in train_data
        ]
    }
    
    val_output = {
        "data": [
            {
                "input_text": example["input"], 
                "target_text": example["output"]
            }
            for example in val_data
        ]
    }
    
    # Create output directory
    output_dir = Path("training")
    output_dir.mkdir(exist_ok=True)
    
    # Save training data
    with open(output_dir / "firish_train.json", "w", encoding="utf-8") as f:
        json.dump(train_output, f, indent=2, ensure_ascii=False)
    
    with open(output_dir / "firish_val.json", "w", encoding="utf-8") as f:
        json.dump(val_output, f, indent=2, ensure_ascii=False)
        
    # Also create CSV format
    with open(output_dir / "firish_train.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["input_text", "target_text"])
        for example in train_data:
            writer.writerow([example["input"], example["output"]])
    
    print(f"💾 Saved training data to:")
    print(f"   - {output_dir}/firish_train.json ({len(train_data)} examples)")
    print(f"   - {output_dir}/firish_val.json ({len(val_data)} examples)")  
    print(f"   - {output_dir}/firish_train.csv (CSV format)")
    
    # Show sample data
    print("\n📝 Sample Training Examples:")
    print("-" * 60)
    for i, example in enumerate(train_data[:3]):
        print(f"{i+1}. Input:  {example['input']}")
        print(f"   Output: {example['output']}")
        print()
    
    return len(train_data), len(val_data)

if __name__ == "__main__":
    train_count, val_count = create_training_data()
    print("=" * 60)
    print("✅ TRAINING DATASET READY FOR T5 FINE-TUNING")
    print(f"📊 Total Examples: {train_count + val_count}")
    print("🚀 Ready to upload to Kaggle for GPU training!")
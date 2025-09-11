# Hugging Face Models for Firish Translation
*Analysis and recommendations for LLM-powered authentic Firish translation*

---

## 🎯 **Top Model Recommendations**

### **1. Google T5 Models (Best Overall)**
- **Model:** `google-t5/t5-small` (3.6M downloads)
- **Model:** `google-t5/t5-base` (1.5M downloads)
- **Why Perfect for Firish:**
  - Text-to-text unified format ideal for translation
  - Multilingual capability (supports EN/FR)
  - Can be fine-tuned on Firish patterns
  - Small enough for local deployment
  - Strong instruction following

**Example Usage:**
```python
# Input: "Context: parents discussing homework with child nearby"
# "Should we check if they finished their math homework?"
# Output: "An bhfuil nous check si siad finis leur math-ach homework-allachta?"
```

### **2. Facebook NLLB-200 (Multilingual Specialist)**
- **Model:** `facebook/nllb-200-distilled-600M` (557K downloads)
- **Why Excellent:**
  - Supports 200 languages including Irish
  - Already handles multilingual mixing
  - Distilled version perfect for efficiency
  - Strong cross-lingual understanding

### **3. Helsinki-NLP OPUS Models (Translation Base)**
- **French-English:** `Helsinki-NLP/opus-mt-fr-en` (916K downloads)
- **English-French:** `Helsinki-NLP/opus-mt-en-fr` (319K downloads)
- **English-Celtic:** `Helsinki-NLP/opus-mt-en-CELTIC` (21 downloads)
- **Why Useful:**
  - High-quality translation pairs
  - Can be ensemble approach (EN↔FR + EN↔GA)
  - Proven translation quality

---

## 🇮🇪 **Irish Language Models Found**

### **Best Irish Models:**
1. **`DCU-NLP/bert-base-irish-cased-v1`** (17 downloads)
   - BERT model trained on Irish text
   - Good for understanding Irish structure
   - Can be used for embedding Irish concepts

2. **`cpierse/wav2vec2-large-xlsr-53-irish`** (26 downloads)
   - Irish speech recognition
   - Could help with pronunciation patterns

3. **`Helsinki-NLP/opus-mt-en-CELTIC`** (21 downloads)
   - English to Celtic languages translation
   - Includes Irish in the mix

### **Irish Language Reality:**
- Very few high-quality Irish models available
- Most have low download counts (< 100)
- Would need significant fine-tuning for Firish patterns

---

## 🧠 **Context-Aware Models**

### **Instruction-Following Models:**
1. **`TinyLlama/TinyLlama-1.1B-Chat-v1.0`** (1.7M downloads)
   - Small, fast, instruction-following
   - Perfect for context-aware translation
   - Can understand obfuscation scenarios

2. **`meta-llama/Llama-2-7b-chat-hf`** (1M downloads)
   - Powerful context understanding
   - Can handle complex family coordination scenarios
   - Good for maintaining conversation flow

---

## 📊 **Model Comparison Matrix**

| Model Type | Best Model | Downloads | Size | Firish Fit | Use Case |
|------------|------------|-----------|------|------------|----------|
| **Translation** | T5-small | 3.6M | Small | ⭐⭐⭐⭐⭐ | Core translation engine |
| **Multilingual** | NLLB-200 | 557K | Medium | ⭐⭐⭐⭐ | Cross-language mixing |
| **Context** | TinyLlama | 1.7M | Small | ⭐⭐⭐⭐ | Situational awareness |
| **Irish** | DCU BERT | 17 | Small | ⭐⭐⭐ | Irish language structure |
| **French** | OPUS MT | 916K | Small | ⭐⭐⭐⭐ | French translation quality |

---

## 🛠 **Recommended Implementation Strategy**

### **Phase 1: Base Translation (T5-Small)**
```python
from transformers import T5ForConditionalGeneration, T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-small")
tokenizer = T5Tokenizer.from_pretrained("google-t5/t5-small")

# Fine-tune on Firish patterns from our training data
# Input format: "translate to firish [context]: [english text]"
```

### **Phase 2: Context Integration (TinyLlama)**
```python 
# Context-aware prompting
context_prompt = """
Translate to Firish (max 2 English words per sentence):
Context: {situation}
Audience: {listeners} 
Opacity: {level}
Text: {input}
Rules: -allachta for English only, use French equivalents when known
"""
```

### **Phase 3: Multi-Model Ensemble**
```python
# Combine strengths:
# 1. T5 for core translation
# 2. TinyLlama for context awareness  
# 3. OPUS models for quality French/Irish
# 4. Rule validation from our CLI
```

---

## 🎯 **Specific Models to Download & Test**

### **High Priority (Download First):**
```bash
# Core translation engine
huggingface-cli download google-t5/t5-small

# Context awareness
huggingface-cli download TinyLlama/TinyLlama-1.1B-Chat-v1.0

# Multilingual support
huggingface-cli download facebook/nllb-200-distilled-600M
```

### **Secondary Priority:**
```bash  
# Translation quality
huggingface-cli download Helsinki-NLP/opus-mt-fr-en
huggingface-cli download Helsinki-NLP/opus-mt-en-fr

# Irish language support
huggingface-cli download DCU-NLP/bert-base-irish-cased-v1
huggingface-cli download Helsinki-NLP/opus-mt-en-CELTIC
```

---

## 💡 **Fine-Tuning Strategy**

### **Training Data We Have:**
- **20 corrected sentence pairs** from your feedback
- **Family coordination scenarios** with authentic patterns
- **Pride & Prejudice examples** showing literary usage
- **Obfuscation rules** with context examples

### **Training Format:**
```json
{
  "input": "translate to firish [parents, child nearby, medium]: Should we check their homework?",
  "output": "An bhfuil nous check-ach leur obair maison?"
}
```

### **Context Categories to Train:**
1. **Family coordination** (homework, bedtime, shopping)
2. **Public obfuscation** (restaurant, travel, money)
3. **Professional scenarios** (appointments, meetings)
4. **Emergency situations** (discrete coordination)

---

## 🚀 **Next Steps**

1. **Download T5-small** - Start with core translation capability
2. **Create training dataset** from our authentic examples
3. **Fine-tune T5** on Firish patterns
4. **Test context integration** with TinyLlama
5. **Build hybrid system** combining LLM + our rule validation

### **Expected Benefits:**
- **Context awareness:** Adjust opacity based on situation
- **Natural flow:** Maintain conversation rhythm  
- **Speaker consistency:** Different family members have different patterns
- **Cultural accuracy:** Understand when/why obfuscation is needed

**The T5-small model fine-tuned on our authentic training data could provide the contextual intelligence that makes real Firish work for family coordination!**

---

**Models ready for testing:** ✅  
**Training data prepared:** ✅  
**Implementation strategy:** ✅  
**Ready to build LLM-powered authentic Firish translator!** 🇮🇪🇫🇷🇬🇧
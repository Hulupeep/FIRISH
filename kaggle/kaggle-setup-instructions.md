# 🚀 Kaggle Setup Instructions for Firish T5 Fine-tuning

**Complete step-by-step guide to train your Firish model on Kaggle's free GPU (30 hours/week)**

---

## 📋 Prerequisites

✅ **You have:** Kaggle CLI set up with API key  
✅ **You need:** ~3 hours of time (2-3 hours training + setup)  
✅ **Cost:** FREE (uses Kaggle's 30 hours/week GPU quota)

---

## 🔄 Step 1: Upload Training Dataset to Kaggle

### **Create Kaggle Dataset from Training Data:**

```bash
# From the firish project directory:
cd kaggle

# Create dataset directory structure
mkdir -p firish-training-dataset
cp ../training/firish_train.json firish-training-dataset/
cp ../training/firish_val.json firish-training-dataset/  
cp ../training/firish_train.csv firish-training-dataset/
cp dataset-metadata.json firish-training-dataset/

# Initialize and create Kaggle dataset
cd firish-training-dataset
kaggle datasets create -p . --dir-mode zip

# Note the dataset name - should be: yourusername/firish-training
```

**Expected output:**
```
Dataset creation successful
Dataset URL: https://www.kaggle.com/datasets/yourusername/firish-training
```

---

## 📓 Step 2: Create Kaggle Notebook

### **Upload the Training Notebook:**

```bash
# From kaggle directory:
kaggle kernels push -p firish-t5-training.ipynb
```

**Or manually:**
1. Go to https://www.kaggle.com/code
2. Click "New Notebook"  
3. Upload `firish-t5-training.ipynb`
4. Set notebook settings:
   - **Language:** Python
   - **Accelerator:** GPU T4 x2 (or whatever's available)
   - **Internet:** On
   - **Environment:** Latest

---

## 🎯 Step 3: Configure Notebook Data Sources

### **Add Training Dataset to Notebook:**

1. **In your Kaggle notebook:**
   - Click "+ Add data" in right sidebar
   - Search for "firish-training" 
   - Add your uploaded dataset
   - Should appear as `/kaggle/input/firish-training/`

2. **Verify data path in notebook:**
   - Check that files load correctly:
     - `/kaggle/input/firish-training/firish_train.json`
     - `/kaggle/input/firish-training/firish_val.json`

---

## ⚡ Step 4: Start Training

### **Run the Training Notebook:**

1. **Turn on GPU:**
   - Settings → Accelerator → GPU T4 x2
   - Should show: "GPU T4 x2 (16 GB VRAM)" available

2. **Run all cells in order:**
   - Cell 1: Install dependencies (~3 minutes)
   - Cell 2: Load training data (~30 seconds)  
   - Cell 3: Load T5-small model (~1 minute)
   - Cell 4: Preprocess data (~1 minute)
   - Cell 5: Configure training (~10 seconds)
   - Cell 6: Initialize trainer (~30 seconds)
   - **Cell 7: START TRAINING (~2-3 hours)** 🔥
   - Cell 8: Test model (~2 minutes)
   - Cell 9: Evaluate model (~1 minute)
   - Cell 10: Create download package (~2 minutes)

3. **Monitor training:**
   - Watch loss decreasing in training logs
   - Training should complete in ~2-3 hours
   - GPU quota used: ~3 hours (plenty left in 30hr/week)

---

## 📊 Step 5: Training Monitoring

### **What to Watch During Training:**

```
🚀 Starting Firish T5-small fine-tuning...
⏰ Training started at: 2024-XX-XX XX:XX:XX
⌛ Estimated time: 2-3 hours

{'loss': 2.1234, 'learning_rate': 5e-05, 'epoch': 0.5, 'step': 50}
{'loss': 1.8765, 'learning_rate': 4.5e-05, 'epoch': 1.0, 'step': 100}
{'loss': 1.5432, 'learning_rate': 4e-05, 'epoch': 1.5, 'step': 150}
...
{'eval_loss': 1.2345, 'eval_exact_match': 0.4, 'epoch': 2.0, 'step': 200}
...

🎉 Training completed!
📊 Final training loss: 1.1234
✅ Model saved to ./firish-t5-small
```

**Good signs:**
- ✅ Loss decreasing over time
- ✅ Evaluation loss staying reasonable  
- ✅ Exact match score improving
- ✅ No GPU out-of-memory errors

**Warning signs:**
- ⚠️ Loss stuck or increasing (overfitting)
- ⚠️ GPU memory errors (reduce batch size)
- ⚠️ Very low exact match (check data format)

---

## 💾 Step 6: Download Your Fine-tuned Model

### **After Training Completes:**

1. **Run the final cell** to create model zip package
2. **Download the zip file:**
   - Look for: `firish-t5-small-YYYYMMDD_HHMMSS.zip`
   - Size should be ~200MB
   - Contains complete fine-tuned model

3. **Verify download contents:**
   ```
   firish-t5-small-YYYYMMDD_HHMMSS.zip
   ├── config.json
   ├── pytorch_model.bin  
   ├── tokenizer_config.json
   ├── tokenizer.json
   ├── special_tokens_map.json
   ├── spiece.model
   └── model_info.json
   ```

---

## 🧪 Step 7: Test Your Model Locally

### **Integration with Existing Firish Tools:**

```python
# In your local environment:
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load your fine-tuned model  
model = T5ForConditionalGeneration.from_pretrained('./firish-t5-small')
tokenizer = T5Tokenizer.from_pretrained('./firish-t5-small')

# Test translation
def translate_firish(text, context="family, medium"):
    input_text = f"translate to firish [{context}]: {text}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    
    outputs = model.generate(input_ids, max_length=50, num_beams=4)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result

# Test examples
print(translate_firish("The bill is expensive", "restaurant, strangers, medium"))
print(translate_firish("Are they ready for bed?", "parents, child nearby, low"))
```

---

## 📈 Expected Results

### **Training Metrics:**
- **Training Loss:** ~2.0 → ~1.1 (decreasing)
- **Validation Loss:** ~1.5 → ~1.2 (stable)  
- **Exact Match:** ~0% → ~40-60% (improving)
- **Training Time:** 2-3 hours on T4
- **Model Size:** ~200MB fine-tuned

### **Sample Outputs:**
```
Input:  "translate to firish [restaurant, medium]: The bill is expensive"
Output: "Le bil-allachta est cher"  ✅ Perfect!

Input:  "translate to firish [family, low]: Good morning everyone"  
Output: "Bonjour tout le monde"  ✅ Correct simplicity!

Input:  "translate to firish [parents, child nearby, medium]: Did they finish homework?"
Output: "An bhfuil siad finis leur obair maison?"  ✅ Authentic!
```

---

## 🔧 Troubleshooting

### **Common Issues & Solutions:**

**❌ "GPU quota exceeded"**
- **Solution:** Wait until next day (quota resets daily) or use Colab backup

**❌ "Dataset not found"**  
- **Solution:** Check dataset name, make sure it's public, verify path in notebook

**❌ "CUDA out of memory"**
- **Solution:** Reduce batch size from 4 to 2 in training config

**❌ "Training loss not decreasing"**
- **Solution:** Check data format, increase learning rate slightly

**❌ "Model outputs nonsense"**
- **Solution:** Train longer, check that training data loaded correctly

### **GPU Time Management:**
- **Free quota:** 30 hours/week
- **Our usage:** ~3 hours total
- **Remaining:** 27 hours for other projects
- **Reset:** Every Monday at 00:00 UTC

---

## ✅ Success Checklist

- [ ] Training dataset uploaded to Kaggle
- [ ] Notebook created with GPU enabled  
- [ ] Training completed without errors
- [ ] Model zip file downloaded (~200MB)
- [ ] Local testing shows good Firish translations
- [ ] Model integrated with existing CLI tools

---

## 🎉 Congratulations!

**You now have a custom fine-tuned T5-small model that understands authentic Firish patterns!**

### **What You've Achieved:**
✅ **Context-aware translation:** Adapts to family/restaurant/public settings  
✅ **Authentic patterns:** Max 2 English words, proper -ach/-allachta suffixes  
✅ **Strategic obfuscation:** Irish backbone + French sophistication  
✅ **Production-ready:** Downloadable model for local deployment

### **Next Steps:**
1. **Compare** with rule-based CLI performance
2. **Test** on real family coordination scenarios  
3. **Integrate** into Firish translation system
4. **Share** with family members for testing

**Your Firish language model is ready for authentic family coordination! 🇮🇪🇫🇷🇬🇧**
# Firish AI Models

This directory contains the fine-tuned T5-small model for Firish translation.

## Model Files

The complete model includes these files:
- ✅ `config.json` - Model configuration
- ✅ `tokenizer_config.json` - Tokenizer settings  
- ✅ `special_tokens_map.json` - Special token mappings
- ✅ `added_tokens.json` - Additional tokens
- ✅ `generation_config.json` - Generation parameters
- ❌ `model.safetensors` - Model weights (242MB, excluded from git)
- ❌ `spiece.model` - SentencePiece model (791KB, excluded from git)

## Download Complete Model

### Option 1: Download from Kaggle (Recommended)
The trained model is available from our Kaggle training notebook:

```bash
# Install Kaggle CLI
pip install kaggle

# Configure API (get key from kaggle.com/account)
kaggle config set -n username -v yourusername
kaggle config set -n key -v yourkey

# Download model files
kaggle kernels output colmbyrne/firish-fixed --path ./downloaded-model
cp -r ./downloaded-model/firish-t5-trained/* ./models/t5-firish/
```

### Option 2: Git LFS (Future)
*Coming soon: We'll add the large model files via Git LFS*

### Option 3: Direct Download Links
*Coming soon: Direct download links for model.safetensors and spiece.model*

## Model Details

- **Base Model**: T5-small (60.5M parameters)
- **Training Data**: 25 authentic Firish examples
- **Training Platform**: Kaggle T4 GPU  
- **Training Time**: ~10 minutes (2 epochs)
- **Loss Reduction**: 5.37 → 4.55
- **Current Status**: Basic functionality, needs more training data

## Usage

Once you have the complete model files:

```bash
# Test AI translation
python tools/cli/firish_llm.py "We need to go shopping" -c "parents, child nearby, medium"

# Compare with rule-based
python tools/cli/firish_compare.py "Let's go home" "family, casual, low"
```

## Model Performance

**Current Status**: ⚠️ Needs improvement
- ✅ Model loads and generates output
- ✅ Responds to context parameters
- ❌ Sometimes generates German instead of proper Firish
- ❌ Limited by small training dataset (25 examples)

**Example Output**:
```
Input: "We need to go shopping"
Current: "Wir sollten einkaufen gehen"  ❌
Expected: "Nous besoin aller shopping-ach"  ✅
```

## Help Improve the Model

The model needs more authentic training data! Help us by:

1. **Contributing examples**: Share authentic code-switching patterns
2. **Reporting issues**: Use our [issue templates](../.github/ISSUE_TEMPLATE/)
3. **Training improvements**: Expand the dataset and retrain

See [NEXT_ACTIONS.md](../NEXT_ACTIONS.md) for detailed improvement plans.

## Training Notebook

The complete training pipeline is available on Kaggle:
- **Notebook**: https://www.kaggle.com/code/colmbyrne/firish-fixed
- **Dataset**: https://www.kaggle.com/datasets/colmbyrne/firish-training

You can fork and modify the training process to experiment with improvements!

---

*Model created by Colm Byrne as part of the Firish language preservation experiment*
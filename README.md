# 🔥 Firish - A Playful Code-Switching Language

> *A playful code-switching language and argot for parents or Irish people traveling abroad*

**Created by**: Colm Byrne  
**Purpose**: An experimental cryptolect preserving colloquial multilingual patterns through computational linguistics

## What is Firish?

Firish is a constructed language (conlang) that emerged from the natural code-switching patterns used by multilingual families, particularly those with English, French, and Irish (Gaeilge) backgrounds. This project represents an attempt to **codify colloquial use of language into a formal cryptolect for preservation and systematic study**.

**The Core Idea**: Take the spontaneous, playful language-mixing that happens naturally in multilingual households and traveling communities, then create:
- 🧠 **Algorithmic rules** for systematic generation  
- 🤖 **AI models** trained on authentic patterns
- 📚 **Documentation** preserving these linguistic behaviors
- 🔧 **Tools** for practical application

This bridges **descriptive linguistics** (how people actually mix languages) with **computational linguistics** (how machines can learn and generate these patterns).

### The Experiment

Firish serves dual purposes:
1. **Practical**: A **playful school-yard language** that mixes English, French, and Irish for family coordination and light privacy
2. **Research**: A **linguistic preservation experiment** - can we capture and formalize the intuitive code-switching patterns that emerge naturally in multilingual communities?

The **EASE algorithm** (Easiest Accessible Selection with Enhanced opacity) represents our attempt to codify the unconscious decision-making process multilingual speakers use when code-switching for both clarity and discretion.

## 🤖 NEW: AI-Powered Translation

We now offer both **rule-based** and **AI-powered** Firish translation:

- **Rule-based**: Uses the EASE algorithm for systematic, predictable translations
- **LLM-based**: Fine-tuned T5-small model trained on authentic Firish patterns
- **Comparison tool**: Side-by-side testing of both approaches

### Quick Translation Examples

**English**: "We need to go shopping"
- **Rule-based**: `nous besoin à aller shopping-ach`
- **LLM-based**: Currently in training - [contribute more examples](https://github.com/issues)

## Language Features

* **Blended language**: English (EN) + French (FR) + Irish (GA)
* **Core principle**: EASE - pick the most accessible word for your partner, most opaque for overhearers
* **Word order**: SVO by default (English-like), but flexible
* **Glue particles**: Irish **an** (Q), **ní** (neg), **tá/níl** (state), **is** (identity)
* **BCP-47 tag**: `art-x-firish`

### Quick Examples

**English**: "Are you buying snacks at the shop?"
**Firish Low**: "An bhfuil tú buying goûter ar an siopa?"
**Firish High**: "Ní acheter tu an goûter siopa-sa?"

**Yes/No responses** (echo the verb):
- **Tá** (yes, I am) / **Níl** (no, I'm not)
- **Tuigim** (I understand) / **Ní thuigim** (I don't understand)

## What's It For?

* **Parents/adults** coordinating around children without rudeness
* **Students** having fun in school corridors  
* **Light privacy** in public spaces
* **Learning crossover**: gentle exposure to French/Irish for English speakers
* **Irish diaspora** maintaining linguistic connections while traveling

## Why Use Firish?

✨ **It's play, not paperwork** - musical, flexible, low-friction  
🎭 **Rewards improvisation** and inside jokes  
🤝 **Social glue language** - shared winks, quick coordination  
🎯 **Soft privacy** without being secretive or rude  
🔬 **Living experiment** - help preserve code-switching patterns  

## Repository Contents

### Core Language
- **[spec/](spec/)** - Complete language specification with EASE algorithm
- **[lexicon/](lexicon/)** - Dictionary with 300+ entries, schema, and validation
- **[phrasebook/](phrasebook/)** - Practical phrases for family, school, shopping, health, emergencies
- **[examples/](examples/)** - Stories, dialogues, and parallel texts with morphological analysis
- **[learn/](learn/)** - Firish 101 quickstart guide and cheat sheet

### AI & Tools
- **[models/](models/)** - Fine-tuned T5-small model for LLM translation
- **[tools/cli/](tools/cli/)** - Translation tools (rule-based, LLM, and comparison)
- **[kaggle/](kaggle/)** - Training pipeline and datasets for model improvement
- **[tests/](tests/)** - Quality assurance and validation guides

### Documentation
- **[docs/](docs/)** - Technical documentation including LLM integration
- **[training/](training/)** - Training data and evaluation examples

## 🚀 Quick Start

### 1. Basic Translation Tools
```bash
# Rule-based translation (EASE algorithm)
python tools/cli/firishify.py "Are you ready for breakfast?"
# Output: an bhfuil tú ready pour breakfast?

# AI-powered translation (requires transformers)
python tools/cli/firish_llm.py "We need to go shopping" -c "parents, child nearby, medium"

# Compare both approaches
python tools/cli/firish_compare.py "Let's go home" "family, public, low"
```

### 2. Learning Path
1. **Learn the basics**: [Firish 101](learn/Firish101.md) (1-hour guide)
2. **Family phrases**: Practice with [Family Codebook](phrasebook/family-codebook.md)
3. **Reference**: Keep the [Cheat Sheet](learn/cheat-sheet.md) handy
4. **Contribute**: Help improve the AI model with more examples

## EASE Rule in Action

Pick the **shortest/most fluent** form that **reduces overhearer comprehension**:

| Context | English | Firish Choice | Why |
|---------|---------|---------------|-----|
| Around kids | "Let's go shopping" | "Téigimís shopping" | Irish verb, EN noun (kids know "shopping") |
| Quick coordination | "Did you pay?" | "An do payer tú?" | Mixed particles, FR verb |
| Higher opacity | "The homework is hard" | "Tá an devoirs crua" | GA structure, FR noun, GA adj |

## 🤖 AI Model Status

**Current**: T5-small fine-tuned on 25 authentic examples  
**Performance**: Basic functionality, needs more training data  
**Training Platform**: Kaggle (free T4 GPU)  

**Help Improve**: [Contribute training examples](https://github.com/issues) based on authentic code-switching patterns you've observed!

## 📋 Next Actions & Roadmap

### Immediate Improvements Needed
- [ ] **Expand training dataset** from 25 to 100+ authentic examples
- [ ] **Improve model accuracy** - currently mixing German instead of proper Firish
- [ ] **Better context handling** for situation/audience/opacity parameters
- [ ] **Evaluation metrics** - BLEU scores against authentic Firish
- [ ] **Hybrid approach** - combine rule-based fallback with LLM enhancement

### Community Contributions Welcome
- [ ] **Document real code-switching patterns** from multilingual families
- [ ] **Add more lexicon entries** with proper accessibility/opacity ratings  
- [ ] **Create conversation examples** for training data
- [ ] **Test and validate** translation quality
- [ ] **Expand to other language combinations** (Spanish-English-Irish, etc.)

See our [GitHub Issues](../../issues) for detailed tasks and how to contribute!

## Features

* **314 lexicon entries** with accessibility/opacity ratings
* **Three opacity levels**: Low (family-friendly) → Mid (public privacy) → High (maximum discretion)
* **Echo answer system**: Irish-style verb echoing for natural responses
* **Dual translation modes**: Rule-based (EASE) + AI-powered (T5-small)
* **Working tools**: CLI converter and data validator (Python)
* **Complete documentation**: Specification, grammar, learning materials
* **Quality assured**: Comprehensive testing and validation framework
* **Open training pipeline**: Kaggle notebooks for model improvement

## Installation & Dependencies

### Basic (Rule-based only)
```bash
git clone https://github.com/yourusername/FIRISH.git
cd FIRISH/tools/cli
python firishify.py "Hello world"  # No dependencies needed
```

### AI-powered (LLM translation)
```bash
pip install transformers torch
python tools/cli/firish_llm.py "Hello world" -c "family, casual, low"
```

## Contributing

We need help expanding Firish! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding vocabulary and phrases
- Contributing training examples  
- Improving AI model accuracy
- Documentation and examples
- Testing and validation

**Special need**: Authentic code-switching examples from multilingual families!

## Licenses

- **Code/Tools**: MIT License ([LICENSE-CODE](LICENSE-CODE))
- **Language Content**: CC BY-SA 4.0 ([LICENSE-TEXT](LICENSE-TEXT))
- **AI Models**: CC BY-SA 4.0 (trained on open data)

## Language Tag

Use BCP-47 tag `art-x-firish` for:
- HTML lang attributes
- Markdown code fences  
- File naming (`.firish.md`, `.firish.txt`)
- Language detection systems

## Academic & Research Context

This project contributes to several fields:
- **Code-switching research**: Computational modeling of natural multilingual behavior
- **Cryptolect preservation**: Documenting informal communication patterns
- **Conlang development**: Systematic creation of constructed languages
- **NLP for low-resource languages**: Training models on limited, high-quality data

**Citation**: If using Firish in academic work, please cite as created by Colm Byrne and reference this repository.

---

**Go raibh maith agat** for exploring Firish! Start with small conversations and let the language grow naturally. Help us preserve and expand these playful multilingual patterns! 🇮🇪🇫🇷🇬🇧

**Created with ❤️ by Colm Byrne** - *preserving the art of playful code-switching*
# Firish: The Playful Code-Switching Language

> **A blended cryptolect mixing English, French, and Irish for fun family coordination**

Firish is a **playful school-yard language** that mixes English, French, and Irish using the **EASE rule**: at each word, pick the easiest/fastest option that your partner understands but an 8-year-old overhearing is least likely to decode.

## What is Firish?

* **Blended language**: English (EN) + French (FR) + Irish (GA)
* **Core principle**: EASE - pick the most accessible word for your partner, most opaque for overhearers
* **Word order**: SVO by default (English-like), but flexible
* **Glue particles**: Irish **an** (Q), **ní** (neg), **tá/níl** (state), **is** (identity)
* **BCP-47 tag**: `art-x-firish`

## Quick Examples

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

## Why Use Firish?

✨ **It's play, not paperwork** - musical, flexible, low-friction
🎭 **Rewards improvisation** and inside jokes
🤝 **Social glue language** - shared winks, quick coordination
🎯 **Soft privacy** without being secretive or rude

## Repository Contents

- **[spec/](spec/)** - Complete language specification with EASE algorithm
- **[lexicon/](lexicon/)** - Dictionary with 300+ entries, schema, and validation
- **[phrasebook/](phrasebook/)** - Practical phrases for family, school, shopping, health, emergencies
- **[examples/](examples/)** - Stories, dialogues, and parallel texts with morphological analysis
- **[learn/](learn/)** - Firish 101 quickstart guide and cheat sheet
- **[tools/](tools/)** - CLI converter and lexicon validator
- **[tests/](tests/)** - Quality assurance and validation guides

## Quick Start

1. **Learn the basics**: [Firish 101](learn/Firish101.md) (1-hour guide)
2. **Try it out**: Use our [CLI tool](tools/cli/firishify.py) to convert English text
3. **Family phrases**: Practice with [Family Codebook](phrasebook/family-codebook.md)
4. **Reference**: Keep the [Cheat Sheet](learn/cheat-sheet.md) handy

## EASE Rule in Action

Pick the **shortest/most fluent** form that **reduces overhearer comprehension**:

| Context | English | Firish Choice | Why |
|---------|---------|---------------|-----|
| Around kids | "Let's go shopping" | "Téigimís shopping" | Irish verb, EN noun (kids know "shopping") |
| Quick coordination | "Did you pay?" | "An do payer tú?" | Mixed particles, FR verb |
| Higher opacity | "The homework is hard" | "Tá an devoirs crua" | GA structure, FR noun, GA adj |

## Features

* **314 lexicon entries** with accessibility/opacity ratings
* **Three opacity levels**: Low (family-friendly) → Mid (public privacy) → High (maximum discretion)
* **Echo answer system**: Irish-style verb echoing for natural responses
* **Working tools**: CLI converter and data validator (Python, no dependencies)
* **Complete documentation**: Specification, grammar, learning materials
* **Quality assured**: Comprehensive testing and validation framework

## Tools Usage

### Convert English to Firish
```bash
python tools/cli/firishify.py "Are you ready for breakfast?"
# Output: an bhfuil you ready for breakfast?

python tools/cli/firishify.py --opacity mid "I want to go shopping"
# Output: vouloir mé to aller shopping

python tools/cli/firishify.py --opacity high "Let's go home now"
# Output: téigimís home anois
```

### Validate Lexicon Data
```bash
python tools/validators/validate_lexicon.py
# Validates dictionary.csv against schema.json
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding vocabulary, phrases, and examples.

## Licenses

- **Code/Tools**: MIT License ([LICENSE-CODE](LICENSE-CODE))
- **Language Content**: CC BY-SA 4.0 ([LICENSE-TEXT](LICENSE-TEXT))

## Language Tag

Use BCP-47 tag `art-x-firish` for:
- HTML lang attributes
- Markdown code fences  
- File naming (`.firish.md`, `.firish.txt`)
- Language detection systems

---

**Go raibh maith agat** for exploring Firish! Start with small conversations and let the language grow naturally. 🇮🇪🇫🇷🇬🇧
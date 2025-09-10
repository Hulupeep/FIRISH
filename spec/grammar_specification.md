# FIRISH Grammar Specification

## Overview
This document provides the technical grammar specification for the FIRISH (Feelings in Rhythm: Irish-inspired Semantic Harmony) language.

## Core Grammar Rules

### 1. Basic Structure
```
statement := word [emotional_modifier] [cultural_modifier] [transition]
```

### 2. Emotional Modifiers
- **Syntax**: `~emotion`
- **Examples**: `~joy`, `~deep`, `~gentle`
- **Function**: Adds emotional context to base words

### 3. Cultural Modifiers  
- **Syntax**: `.context`
- **Examples**: `.irish`, `.formal`, `.ancient`
- **Function**: Provides cultural or contextual framing

### 4. Transition Operators
- **Syntax**: `emotion1>emotion2`
- **Examples**: `sad>hope`, `anger>peace`
- **Function**: Expresses emotional transformation

### 5. Compound Emotions
- **Syntax**: `emotion1~emotion2`
- **Examples**: `happy~nervous`, `tired~peaceful`
- **Function**: Multiple simultaneous emotional states

## Syntax Rules

### Word Formation
1. Base words follow English-like patterns
2. Emotional modifiers use tilde (`~`)
3. Cultural contexts use period (`.`)
4. Transitions use arrow (`>`)

### Punctuation
- Sentences can end with traditional punctuation (`.`, `!`, `?`)
- Emotional intensity can be conveyed through punctuation
- Multiple exclamation marks indicate high emotion

### Comments
- Line comments begin with `#`
- Used for translation notes and cultural context

## Semantic Rules

### Emotional Consistency
- Emotional modifiers should align with base word meaning
- Contradictory emotions can be compound (`happy~sad`)
- Transitions show emotional journey

### Cultural Sensitivity
- Cultural modifiers should be respectful
- Irish language elements welcome but not required
- Context markers help interpretation

## Examples

### Simple Statements
```firish
hello~warm         # warm greeting
goodbye~peaceful   # peaceful farewell
```

### Complex Expressions
```firish
love~deep>eternal.irish = "grá mo chroí, síoraí"
```

### Emotional Narratives
```firish
morning~quiet
work~focused
evening~tired>peaceful
night~grateful
```

## Implementation Notes

### Parser Requirements
1. Handle tilde-separated emotional modifiers
2. Process period-separated cultural contexts
3. Parse arrow-separated transitions
4. Support compound emotional states

### Validation Rules
1. Emotional modifiers must be valid emotions
2. Cultural contexts should be recognized
3. Transitions should be meaningful
4. Base words should exist in lexicon

## Future Extensions

### Advanced Features
- Intensity scaling (`~very_happy`, `~slightly_sad`)
- Time-based emotions (`morning~fresh`, `evening~reflective`)
- Relationship emotions (`love.family`, `respect.teacher`)

### Integration Possibilities
- Voice recognition for emotional tone
- Text-to-speech with emotional inflection
- Translation to/from other emotional languages
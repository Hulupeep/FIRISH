# Firish Language Specification v1.0

## 1. Introduction

Firish is a constructed language designed to balance linguistic efficiency with natural expressiveness. It features a systematic approach to word formation, contextual opacity mechanics, and an innovative EASE (Efficiency and Simplicity Enhancement) algorithm for adaptive communication.

## 2. Phonology

### 2.1 Phoneme Inventory

**Consonants:**
- Stops: /p t k b d g/
- Fricatives: /f θ s ʃ x v ð z ʒ ɣ h/
- Nasals: /m n ŋ/
- Liquids: /l r/
- Glides: /w j/

**Vowels:**
- Short: /a e i o u/
- Long: /aː eː iː oː uː/
- Diphthongs: /ai au ei ou/

### 2.2 Phonotactics

**Syllable Structure:** (C)(C)V(C)(C)

**Constraints:**
- Maximum two consonants in onset and coda
- Sonority sequencing principle applies
- No identical consonants in clusters
- Stress falls on penultimate syllable by default

**Allowed Onset Clusters:**
- Stop + liquid: /pr br tr dr kr gr pl bl kl gl/
- Fricative + liquid: /fr θr sr ʃr fl θl sl ʃl/
- /s/ + stop: /sp st sk/
- Fricative + glide: /fj θw sw ʃw/

**Allowed Coda Clusters:**
- Liquid + stop: /rp rt rk rb rd rg lp lt lk lb ld lg/
- Nasal + stop: /mp nt ŋk mb nd ŋg/
- Fricative + stop: /sp st sk/

### 2.3 Phonological Processes

**Vowel Harmony:** Progressive assimilation in compound words
- High vowels /i u/ spread rightward
- Mid vowels /e o/ remain neutral
- Low vowel /a/ blocks harmony

**Consonant Mutation:**
- Word-initial consonants undergo lenition in certain grammatical contexts
- /p t k/ → /b d g/ after definite articles
- /b d g/ → /v ð ɣ/ in genitive constructions

**Stress Assignment:**
- Primary stress on penultimate syllable
- Secondary stress every two syllables leftward
- Monosyllabic words receive primary stress
- Compound words: stress on first element

## 3. Morphology

### 3.1 Word Classes

**Core Classes:**
- Nouns (substantives)
- Verbs (predicates)
- Modifiers (adjectives/adverbs)
- Particles (functional elements)

**Functional Classes:**
- Determiners
- Pronouns
- Conjunctions
- Prepositions

### 3.2 Nominal Morphology

**Number Marking:**
- Singular: unmarked
- Plural: suffix -en
- Collective: suffix -um
- Distributive: reduplication + -a

**Case System (analytic):**
- Nominative: unmarked
- Accusative: particle ko
- Genitive: particle tu
- Dative: particle na
- Instrumental: particle wi
- Locative: particle lo

**Definiteness:**
- Definite: article te (triggers consonant mutation)
- Indefinite: article ka
- Generic: unmarked

### 3.3 Verbal Morphology

**Tense-Aspect System:**
- Present: unmarked
- Past: prefix sa-
- Future: prefix va-
- Perfect: suffix -eth
- Progressive: suffix -ing
- Habitual: suffix -ar

**Mood:**
- Indicative: unmarked
- Subjunctive: prefix le-
- Imperative: suffix -o
- Conditional: prefix me-

**Voice:**
- Active: unmarked
- Passive: suffix -is + auxiliary
- Reflexive: pronoun self + verb
- Causative: prefix kau-

**Agreement:**
- Person: suffixes -m (1sg), -s (2sg), -t (3sg), -me (1pl), -se (2pl), -te (3pl)
- Gender: neutral (no marking)

### 3.4 Modifier Morphology

**Degree:**
- Positive: unmarked
- Comparative: suffix -er
- Superlative: prefix mo- + suffix -est
- Excessive: prefix over-

**Derivational Morphology:**
- Agentive: suffix -ist
- Abstract: suffix -ness
- Diminutive: suffix -let
- Augmentative: suffix -on

## 4. Syntax

### 4.1 Word Order

**Basic Order:** SVO (Subject-Verb-Object)
- Flexible with topicalization
- OSV for emphasis or questions
- VSO in narrative contexts

**Constituent Order:**
- Determiner-Noun
- Noun-Adjective
- Auxiliary-Verb
- Verb-Complement
- Preposition-Noun

### 4.2 Clause Structure

**Simple Clauses:**
```
[S NP] [V VP] [O NP] [ADJ PP/AdvP]*
```

**Complex Clauses:**
- Subordination with complementizers: that = da, if = si, when = wen
- Relative clauses with relativizer hu following head noun
- Coordination with conjunctions: and = en, or = or, but = sed

### 4.3 Question Formation

**Yes/No Questions:**
- Particle ga sentence-initially
- Rising intonation

**Wh-Questions:**
- Wh-words: who = hwa, what = wat, where = war, when = wen, why = wai, how = how
- Wh-fronting with auxiliary inversion for verbs

### 4.4 Negation

**Standard Negation:**
- Particle non pre-verbally
- Negative polarity items licensed in scope of non

**Emphatic Negation:**
- Double negation: non...nil (not...nothing)
- Negative quantifiers: nobodi (nobody), notheng (nothing)

## 5. EASE Algorithm Implementation

### 5.1 Core Principles

The EASE algorithm operates on four dimensions:
1. **Efficiency:** Minimize cognitive load through regular patterns
2. **Adaptability:** Adjust complexity based on context and familiarity
3. **Simplicity:** Reduce unnecessary morphological marking
4. **Enhancement:** Add precision when communicative need requires it

### 5.2 Selection Mechanisms

**Lexical Selection:**
- High-frequency words prefer shorter forms
- Technical domains activate specialized vocabulary
- Emotional contexts trigger expressive variants

**Morphological Selection:**
- Optional plural marking in definite contexts
- Aspect marking only when temporally relevant
- Case marking reduced in fixed word order

**Syntactic Selection:**
- Simple clauses in routine communication
- Complex structures for precise expression
- Ellipsis in predictable contexts

### 5.3 Context Sensitivity

**Familiarity Levels:**
- Intimate: maximal reduction and ellipsis
- Informal: moderate simplification
- Formal: full morphological marking
- Technical: domain-specific elaboration

**Cognitive Load Assessment:**
- Monitor sentence complexity metrics
- Adapt to processing difficulty indicators
- Balance precision against comprehensibility

## 6. Opacity Mechanics

### 6.1 Theoretical Foundation

Opacity in Firish refers to the systematic variation in explicitness based on contextual factors. Information can be:
- **Transparent:** Fully explicit
- **Translucent:** Partially recoverable from context
- **Opaque:** Maximally implicit

### 6.2 Opacity Triggers

**Pragmatic Factors:**
- Shared knowledge between interlocutors
- Situational context availability
- Discourse continuity

**Linguistic Factors:**
- Morphological redundancy
- Syntactic predictability
- Lexical frequency effects

### 6.3 Opacity Implementation

**Ellipsis Rules:**
- Subject deletion in continuing topics
- Object deletion with transitive verbs in context
- Auxiliary deletion in consistent tense contexts

**Reduction Patterns:**
- Phonological reduction in high-frequency items
- Morphological simplification in regular paradigms
- Syntactic compression in familiar constructions

**Recovery Mechanisms:**
- Context-based inference rules
- Default assumption principles
- Clarification request protocols

## 7. Particle System

### 7.1 Functional Categories

**Grammatical Particles:**
- Case markers: ko (ACC), na (DAT), tu (GEN), wi (INST), lo (LOC)
- Question marker: ga
- Negation: non
- Emphatic: jen

**Discourse Particles:**
- Topic marker: wa
- Focus marker: sa
- Contrast marker: sed
- Continuation: en

**Modal Particles:**
- Certainty: shu (certain), mai (maybe)
- Evidentiality: sei (I see/know), hir (I hear)
- Politeness: plez (please), tai (thanks)

### 7.2 Particle Syntax

**Position:**
- Case particles follow their NPs
- Discourse particles in second position (Wackernagel position)
- Modal particles clause-finally

**Stacking:**
- Maximum two particles per position
- Scope relations: outer particle has wider scope
- Morphophonological fusion in high-frequency combinations

### 7.3 Particle Semantics

**Compositional Meaning:**
- Core grammatical function plus pragmatic contribution
- Context-sensitive interpretation rules
- Interaction with prosody for emphasis

## 8. Echo Response System

### 8.1 Echo Types

**Confirmatory Echoes:**
- Full repetition: agreement/confirmation
- Partial repetition: selective confirmation
- Modified repetition: qualified agreement

**Interrogative Echoes:**
- Rising intonation on repeated element
- Focus on questioned constituent
- Request for clarification or confirmation

**Expressive Echoes:**
- Emotional coloring through prosody
- Evaluative modification of repeated content
- Social alignment signaling

### 8.2 Echo Constraints

**Syntactic Constraints:**
- Echo constituent boundaries
- Preservation of grammatical relations
- Agreement maintenance in modified echoes

**Pragmatic Constraints:**
- Relevance to discourse context
- Appropriate social register
- Turn-taking conventions

### 8.3 Echo Functions

**Discourse Management:**
- Turn acknowledgment
- Topic continuation
- Attention direction

**Social Functions:**
- Rapport building
- Empathy expression
- Power negotiation

## 9. Lexicon Organization

### 9.1 Core Vocabulary

**Basic Concepts (500 words):**
- Body parts, family terms, basic actions
- Numbers, colors, spatial relations
- Time expressions, weather terms
- Common objects and materials

**Extended Vocabulary (2000 words):**
- Abstract concepts, complex actions
- Technical terminology by domain
- Cultural and social concepts
- Specialized registers

### 9.2 Word Formation Strategies

**Compounding:**
- Head-final: waterfall = water-fall
- Coordinative: parent = mother-father
- Exocentric: redhead = red-head (person)

**Derivation:**
- Productive suffixes for major categories
- Conversion between word classes
- Productive prefixation for negation and intensity

**Borrowing:**
- Phonological adaptation rules
- Semantic field constraints
- Etymology marking in formal registers

### 9.3 Semantic Fields

**Spatial Domain:**
- Absolute directions, relative positions
- Containment and support relations
- Motion and path expressions

**Temporal Domain:**
- Absolute and relative time reference
- Duration and frequency expressions
- Sequence and simultaneity

**Social Domain:**
- Kinship terminology
- Status and role designations
- Interaction and communication verbs

## 10. Pragmatics and Usage

### 10.1 Speech Acts

**Direct Acts:**
- Statements, questions, commands
- Conventional performatives
- Explicit illocutionary force

**Indirect Acts:**
- Politeness-motivated indirection
- Contextual inference requirements
- Cultural convention sensitivity

### 10.2 Politeness System

**Honorifics:**
- Age-based respect markers
- Professional title usage
- Social distance indicators

**Register Variation:**
- Formal vs. informal morphology
- Vocabulary choice by social context
- Syntactic complexity adjustment

### 10.3 Discourse Organization

**Topic Management:**
- Topic introduction and development
- Topic shift signaling
- Topic closure markers

**Coherence Relations:**
- Causal, temporal, and logical connections
- Contrast and concession marking
- Elaboration and exemplification

## 11. Orthography

### 11.1 Writing System

**Alphabet:** Modified Latin script (26 letters + 5 diacritics)

**Letter-Sound Correspondences:**
- Mostly phonemic with regular exceptions
- Diacritics for vowel length and tone
- Digraphs for complex consonants

**Capitalization:**
- Sentence-initial words
- Proper nouns and titles
- Emphatic expressions

### 11.2 Punctuation

**Standard Marks:**
- Period (.), comma (,), semicolon (;)
- Question mark (?), exclamation point (!)
- Quotation marks (""), apostrophe (')

**Special Marks:**
- Echo marker (~) for repetitive structures
- Opacity marker (°) for implicit content
- Particle separator (|) in linguistic notation

### 11.3 Typography

**Text Organization:**
- Paragraph structure for topic units
- Bullet points for lists
- Indentation for subordinate clauses

## 12. Historical Development

### 12.1 Design Principles

**Naturalism:**
- Plausible sound changes
- Realistic morphological development
- Consistent syntactic evolution

**Efficiency:**
- Streamlined paradigms
- Regular phonological rules
- Minimal allomorphy

### 12.2 Planned Evolution

**Phase 1:** Core grammar and basic vocabulary
**Phase 2:** Extended lexicon and register variation
**Phase 3:** Dialectal differentiation and stylistic elaboration

### 12.3 Variant Management

**Regional Varieties:**
- Phonological variation patterns
- Lexical innovation tendencies
- Syntactic preference differences

**Social Varieties:**
- Age-graded changes
- Professional specialization
- Cultural adaptation patterns

## 13. Implementation Notes

### 13.1 Computational Processing

**Parsing Considerations:**
- Ambiguity resolution strategies
- Context-sensitive rule application
- Efficiency optimization for real-time processing

**Generation Algorithms:**
- Template-based construction
- Rule-based morphological synthesis
- Context-appropriate selection mechanisms

### 13.2 Learning Resources

**Pedagogical Sequence:**
- Phonology → Basic morphology → Core syntax
- High-frequency vocabulary first
- Gradual complexity introduction

**Assessment Metrics:**
- Comprehension accuracy measures
- Production fluency indicators
- Pragmatic appropriateness evaluation

### 13.3 Community Guidelines

**Usage Standards:**
- Prescriptive core for consistency
- Descriptive periphery for innovation
- Community-driven evolution principles

**Documentation Standards:**
- Regular specification updates
- Usage corpus maintenance
- Community feedback integration

## 14. References and Bibliography

### 14.1 Theoretical Foundations

- Chomsky, N. (1995). *The Minimalist Program*
- Goldberg, A. (2006). *Constructions at Work*
- Tomasello, M. (2003). *Constructing a Language*

### 14.2 Typological Studies

- Comrie, B. (1989). *Language Universals and Linguistic Typology*
- Croft, W. (2003). *Typology and Universals*
- Haspelmath, M. (2001). *Language Typology and Language Universals*

### 14.3 Constructed Language Research

- Okrent, A. (2009). *In the Land of Invented Languages*
- Peterson, D. J. (2015). *The Art of Language Invention*
- Adams, M. (2011). *From Elvish to Klingon*

---

*This specification represents version 1.0 of the Firish language system. Updates and revisions will be documented in subsequent versions as the language develops through usage and community input.*
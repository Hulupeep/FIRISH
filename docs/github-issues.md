# Firish Project GitHub Issues

## Issue 1: Spec: Copula Guidance (is vs tá)

**Title:** Add copula guidance rules for "is" vs "tá" usage in Firish code-switching

**Labels:** `enhancement`, `documentation`, `grammar`, `high-priority`

**Description:**
The Firish specification needs clear guidance on when to use English "is" versus Irish "tá" in code-switching contexts. This is a fundamental grammatical distinction that affects the authenticity and comprehensibility of Firish expressions.

**Problem Statement:**
Currently, learners and speakers lack clear rules for choosing between English "is" and Irish "tá" when code-switching, leading to inconsistent usage patterns and potential misunderstandings.

**Acceptance Criteria:**
- [ ] Add a dedicated section to `spec/grammar.md` explaining copula usage rules
- [ ] Include 6 comprehensive examples showing correct usage patterns
- [ ] Cover both permanent states (using "is") and temporary states (using "tá")
- [ ] Explain contextual factors that influence choice
- [ ] Include common mistakes and how to avoid them
- [ ] Provide practice exercises for learners

**Implementation Details:**
1. Research Irish copula system (is vs tá distinction)
2. Analyze code-switching patterns in other Celtic-English varieties
3. Create clear, beginner-friendly rules
4. Develop diverse example sentences covering:
   - Identity statements
   - Location descriptions
   - Temporary vs permanent characteristics
   - Emotional states
   - Professional roles
   - Weather descriptions

**Estimated Effort:** 8-12 hours
**Priority:** High
**Difficulty:** Intermediate

---

## Issue 2: Morphology: Standardize -allachta Suffix Usage

**Title:** Create consistent rules for -allachta suffix in Firish morphology

**Labels:** `enhancement`, `morphology`, `standardization`, `medium-priority`

**Description:**
The -allachta suffix appears in Firish but lacks standardized usage rules, leading to artificial constructions that don't reflect authentic Irish morphological patterns.

**Problem Statement:**
Current usage of -allachta suffix is inconsistent and sometimes creates unnatural word formations that don't align with Irish morphological principles.

**Acceptance Criteria:**
- [ ] Research authentic Irish -allachta suffix usage patterns
- [ ] Create standardized rules for Firish implementation
- [ ] Replace artificial constructions with authentic patterns
- [ ] Update existing examples to follow new standards
- [ ] Add morphological productivity rules
- [ ] Include semantic constraints on suffix usage

**Implementation Details:**
1. Analyze corpus of Irish texts for -allachta usage
2. Identify productive vs non-productive uses
3. Create formation rules based on stem types
4. Develop semantic categories for appropriate usage
5. Review and update all existing Firish examples
6. Create style guide for future contributions

**Examples to Address:**
- Overuse in abstract concept formation
- Incorrect attachment to non-Irish stems
- Semantic mismatch with base words

**Estimated Effort:** 12-16 hours
**Priority:** Medium
**Difficulty:** Advanced

---

## Issue 3: Opacity Legend in Example Files

**Title:** Add opacity level indicators to Firish examples for trilingual accessibility

**Labels:** `enhancement`, `accessibility`, `documentation`, `medium-priority`

**Description:**
Example files need opacity level indicators to help learners understand trilingual accessibility levels and choose appropriate learning materials for their proficiency.

**Problem Statement:**
Learners cannot easily assess the difficulty level of Firish examples, making it hard to find appropriate materials for their current proficiency level.

**Acceptance Criteria:**
- [ ] Design opacity level system (e.g., 1-5 scale)
- [ ] Define criteria for each opacity level
- [ ] Add indicators to all existing example files
- [ ] Create legend explaining the system
- [ ] Implement consistent formatting across examples
- [ ] Include progression guidance for learners

**Opacity Level System:**
- **Level 1:** Mostly English with basic Irish insertions
- **Level 2:** Balanced code-switching with familiar Irish terms
- **Level 3:** Complex switching with intermediate Irish structures
- **Level 4:** Advanced mixing with idiomatic expressions
- **Level 5:** Near-native fluency required for comprehension

**Implementation Details:**
1. Review all existing examples
2. Assess trilingual complexity
3. Assign opacity levels consistently
4. Add visual indicators (icons, colors, or badges)
5. Create filtering system for learners
6. Update README with legend explanation

**Estimated Effort:** 6-8 hours
**Priority:** Medium
**Difficulty:** Beginner-Intermediate

---

## Issue 4: Training Data Growth (25 → 150 Examples)

**Title:** Expand training examples from 25 to 150 for improved T5-small fine-tuning

**Labels:** `enhancement`, `machine-learning`, `training-data`, `high-priority`

**Description:**
The current 25 training examples are insufficient for effective T5-small model fine-tuning. Expanding to 150 comprehensive examples will significantly improve model performance and generalization.

**Problem Statement:**
Limited training data (25 examples) results in poor model performance, overfitting, and inadequate coverage of Firish linguistic patterns.

**Acceptance Criteria:**
- [ ] Expand from 25 to 150 training examples
- [ ] Ensure balanced representation across linguistic phenomena
- [ ] Maintain high quality and authenticity standards
- [ ] Include diverse domains and contexts
- [ ] Validate examples with native Irish speakers
- [ ] Create systematic annotation guidelines

**Distribution Requirements:**
- **Grammar patterns:** 30 examples
- **Code-switching scenarios:** 40 examples
- **Domain-specific vocabulary:** 25 examples
- **Morphological variations:** 20 examples
- **Conversational contexts:** 35 examples

**Quality Standards:**
- Authentic Irish morphology and syntax
- Natural code-switching patterns
- Contextually appropriate usage
- Consistent annotation format
- Peer review by Irish language experts

**Implementation Details:**
1. Develop example collection strategy
2. Create annotation guidelines
3. Recruit Irish language contributors
4. Implement quality assurance process
5. Validate against existing corpus data
6. Prepare data for model training

**Estimated Effort:** 40-60 hours
**Priority:** High
**Difficulty:** Advanced

---

## Issue 5: Model Card & Misuse Policy Documentation

**Title:** Create comprehensive model card and misuse policy for T5-small Firish model

**Labels:** `documentation`, `ethics`, `machine-learning`, `compliance`, `high-priority`

**Description:**
The T5-small Firish model needs proper documentation including model card with performance metrics, limitations, and comprehensive misuse policy to ensure responsible deployment and usage.

**Problem Statement:**
Lack of proper model documentation and ethical guidelines creates risks for misuse and doesn't provide users with essential information about model capabilities and limitations.

**Acceptance Criteria:**
- [ ] Create comprehensive model card following industry standards
- [ ] Document model architecture and training process
- [ ] Include performance benchmarks and limitations
- [ ] Develop detailed misuse policy
- [ ] Provide usage guidelines and best practices
- [ ] Include bias assessment and mitigation strategies

**Model Card Requirements:**
- **Model Details:** Architecture, version, date
- **Intended Use:** Primary applications, target users
- **Performance:** Benchmarks, test results, confidence intervals
- **Limitations:** Known failure cases, scope boundaries
- **Bias Assessment:** Evaluation across demographic groups
- **Training Data:** Sources, preprocessing, annotation process

**Misuse Policy Components:**
- **Prohibited Uses:** Specific forbidden applications
- **Risk Mitigation:** Safety measures and monitoring
- **Reporting Mechanisms:** How to report misuse
- **Legal Compliance:** Relevant regulations and standards
- **Community Guidelines:** Expected behavior standards

**Implementation Details:**
1. Research industry standards for model cards
2. Evaluate model performance comprehensively
3. Conduct bias assessment across relevant dimensions
4. Consult with ethics experts on policy development
5. Create user-friendly documentation format
6. Implement monitoring and reporting systems

**Estimated Effort:** 20-30 hours
**Priority:** High
**Difficulty:** Intermediate-Advanced

---

## Implementation Priority Order

1. **Issue #1** (Copula Guidance) - Foundation for consistent usage
2. **Issue #5** (Model Card) - Essential for responsible deployment
3. **Issue #4** (Training Data) - Critical for model improvement
4. **Issue #2** (Morphology) - Important for authenticity
5. **Issue #3** (Opacity Legend) - Enhances user experience

## Contributing Guidelines

- All issues welcome community contributions
- Please comment on issues before starting work
- Follow existing code style and documentation patterns
- Include tests and examples with implementations
- Request review from maintainers before finalizing

## Additional Resources

- [Irish Grammar Reference](https://www.teanglann.ie/)
- [Code-switching Research Papers](./references/)
- [T5 Model Documentation](https://huggingface.co/docs/transformers/model_doc/t5)
- [Responsible AI Guidelines](https://ai.google/responsibilities/responsible-ai-practices/)
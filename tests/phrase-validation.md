# Phrase Validation Testing Documentation

## Overview
Comprehensive testing framework for validating Firish phrases, expressions, idioms, and complex linguistic structures beyond individual word entries.

## Phrase Validation Categories

### 1. Basic Phrase Structure Validation

#### 1.1 Simple Phrases
**Purpose**: Validate basic noun phrases, verb phrases, and adjective phrases
**Test Cases**:

```csv
# Test data: tests/data/basic_phrases.csv
id,firish,english,part_of_speech,category,definition,phrase_type,structure
phrase_001,teach mór,big house,phrase,housing,A large residential building,noun_phrase,adjective + noun
phrase_002,ag rith,running,phrase,action,The act of running,verb_phrase,preposition + verbal_noun
phrase_003,go mall,slowly,phrase,manner,In a slow manner,adverb_phrase,particle + adjective
phrase_004,ar an mbord,on the table,phrase,location,Positioned upon the table surface,prepositional_phrase,preposition + article + noun
phrase_005,faoi dheireadh,finally/at last,phrase,time,After a long time or delay,adverb_phrase,preposition + noun
```

**Validation Tests**:
```bash
# Test 1.1.1: Basic phrase structure validation
python tools/validators/validate_lexicon.py tests/data/basic_phrases.csv data/schema.json

# Expected validations:
# ✅ phrase_type field contains valid values
# ✅ structure field describes grammatical components
# ✅ Firish phrases follow expected patterns
# ✅ English translations are appropriate for phrase meaning
```

#### 1.2 Complex Phrases
**Purpose**: Test multi-word expressions and compound phrases
**Test Cases**:

```csv
# Test data: tests/data/complex_phrases.csv
id,firish,english,part_of_speech,category,definition,phrase_type,grammatical_notes
phrase_101,Tá sé ag cur báistí,It is raining,phrase,weather,Expressing the state of rain falling,weather_expression,Progressive tense with meteorological verb
phrase_102,Níl aon tinteán mar do thinteán féin,There's no place like home,idiom,home,Expression about the comfort of one's own home,idiomatic_expression,Comparative construction with negative
phrase_103,Beidh lá eile ag an bPaorach,Another day will come to the pauper,idiom,hope,Expression of hope for better times,proverb,Future tense with metaphorical meaning
phrase_104,Tá an-áthas orm,I am very happy,phrase,emotion,Expression of great joy or happiness,emotional_expression,Intensifier with abstract noun construction
phrase_105,Ar dheis Dé go raibh a anam,May his soul be at God's right hand,phrase,blessing,Traditional blessing for the deceased,religious_formula,Subjunctive mood in blessing format
```

**Validation Tests**:
```bash
# Test 1.2.1: Complex phrase validation
python tools/validators/validate_lexicon.py tests/data/complex_phrases.csv data/schema.json

# Expected validations:
# ✅ Idiomatic expressions marked appropriately
# ✅ Cultural context preserved in definitions
# ✅ Grammatical notes explain complex structures
# ⚠️  Warning for very culture-specific expressions
```

### 2. Idiomatic Expression Validation

#### 2.1 Common Idioms
**Purpose**: Validate frequently used idiomatic expressions
**Test Cases**:

```csv
# Test data: tests/data/common_idioms.csv
id,firish,english,part_of_speech,category,definition,literal_translation,cultural_context,usage_frequency
idiom_001,Tá sé ar buile,He is furious,idiom,emotion,Expression of extreme anger,He is on fury,Common in heated situations,8
idiom_002,Chuir sé ruaig orm,He chased me away,idiom,action,To forcefully make someone leave,He put a chase on me,Used in conflict situations,6
idiom_003,Bhí sé i gcroí na cathrach,He was in the heart of the city,idiom,location,To be in the city center,He was in heart of the city,Urban context expression,7
idiom_004,Tá sé ina chodladh,He is asleep,phrase,state,The condition of being asleep,He is in his sleep,Basic state expression,10
idiom_005,Rinne sé dearmad air,He forgot about it,idiom,cognition,To fail to remember something,He made forgetfulness on it,Common memory lapse expression,9
```

**Validation Criteria**:
```python
# Idiom-specific validation rules
IDIOM_VALIDATION_RULES = {
    'literal_translation': {
        'required': True,
        'different_from_english': True,  # Should differ from direct translation
        'explanation': 'Helps learners understand word-for-word meaning'
    },
    'cultural_context': {
        'required': True,
        'min_length': 10,
        'explanation': 'Provides usage context and cultural background'
    },
    'usage_frequency': {
        'range': [1, 10],
        'correlation_check': True,  # Should correlate with difficulty
    }
}
```

#### 2.2 Rare and Archaic Idioms
**Purpose**: Test handling of less common idiomatic expressions
**Test Cases**:

```csv
# Test data: tests/data/rare_idioms.csv
id,firish,english,part_of_speech,category,definition,archaic_notes,regional_usage,difficulty
idiom_201,Dhéanfadh sé cloch de mhadra,He would make a stone of a dog,idiom,transformation,Expression about extreme change,Archaic expression rarely used in modern Irish,Ulster Irish primarily,9
idiom_202,Tá sé chomh cam le driopás,He is as crooked as a dripping,idiom,character,Describing someone very dishonest,Old rural expression,Munster dialect,8
idiom_203,Ní bheidh a leithéid arís ann,There won't be his like again,idiom,uniqueness,Expression about someone irreplaceable,Traditional eulogy phrase,Universal but formal,7
```

**Validation Tests**:
```bash
# Test 2.2.1: Archaic idiom handling
python tools/validators/validate_lexicon.py tests/data/rare_idioms.csv data/schema.json

# Expected validations:
# ✅ High difficulty ratings for rare expressions
# ✅ Regional usage notes present
# ⚠️  Warning for archaic terms about modern relevance
# ✅ Proper categorization as historical/regional
```

### 3. Grammatical Pattern Validation

#### 3.1 Verbal Constructions
**Purpose**: Test complex verbal patterns and constructions
**Test Cases**:

```csv
# Test data: tests/data/verbal_constructions.csv
id,firish,english,part_of_speech,category,definition,verbal_pattern,tense_mood,construction_type
verb_301,Bhí mé ag obair,I was working,phrase,action,Past continuous action,Bhí + subject + ag + verbal_noun,past_continuous,progressive_aspect
verb_302,Beidh orm imeacht,I will have to go,phrase,obligation,Future obligation expression,Beidh + preposition + subject + verbal_noun,future_obligation,modal_construction
verb_303,Dá mbeinn ann,If I were there,phrase,condition,Hypothetical condition,Dá + conditional + subject + location,conditional_mood,hypothetical_construction
verb_304,B'fhéidir go bhfaca mé é,Maybe I saw him,phrase,possibility,Expression of uncertain past event,B'fhéidir + go + past_subjunctive,subjunctive_mood,possibility_construction
verb_305,Ar mhaith leat cupán tae?,Would you like a cup of tea?,phrase,offer,Polite offer expression,Ar + conditional + leat + object,conditional_question,polite_offer
```

**Pattern Validation Rules**:
```python
VERBAL_PATTERN_RULES = {
    'progressive_aspect': {
        'pattern': r'(Bhí|Tá|Beidh).*ag.*',
        'components': ['auxiliary', 'subject', 'ag', 'verbal_noun'],
        'description': 'Irish progressive construction'
    },
    'conditional_mood': {
        'pattern': r'(Dá|Mura|Murar).*',
        'components': ['conditional_particle', 'conditional_verb'],
        'description': 'Hypothetical or conditional statements'
    }
}
```

#### 3.2 Prepositional Phrases
**Purpose**: Validate complex prepositional constructions
**Test Cases**:

```csv
# Test data: tests/data/prepositional_phrases.csv
id,firish,english,part_of_speech,category,definition,preposition_type,case_government,semantic_role
prep_401,ar an gcathaoir,on the chair,phrase,location,Positioned upon the chair,simple_preposition,dative_case,locative
prep_402,de bharr na gaoithe,because of the wind,phrase,causation,Due to wind conditions,compound_preposition,genitive_case,causal
prep_403,i rith na hoíche,during the night,phrase,time,Throughout the nighttime,compound_preposition,genitive_case,temporal
prep_404,thar lear,abroad/overseas,phrase,location,In foreign countries,compound_preposition,no_case,directional
prep_405,faoi dheireadh,finally,phrase,time,At the end/conclusion,compound_preposition,no_case,temporal
```

**Validation Tests**:
```bash
# Test 3.2.1: Prepositional phrase validation
python tools/validators/validate_lexicon.py tests/data/prepositional_phrases.csv data/schema.json

# Expected validations:
# ✅ Preposition types correctly identified
# ✅ Case government noted where applicable  
# ✅ Semantic roles properly categorized
# ✅ Compound prepositions vs. simple prepositions distinguished
```

### 4. Semantic Field Validation

#### 4.1 Thematic Phrase Groups
**Purpose**: Test phrases within specific semantic domains
**Test Cases**:

```csv
# Test data: tests/data/weather_phrases.csv
id,firish,english,part_of_speech,category,definition,semantic_field,meteorological_type,seasonal_association
weather_501,Tá sé ag cur sneachta,It is snowing,phrase,weather,Snow is falling,precipitation,snow,winter
weather_502,Tá stoirm mhór ann,There is a big storm,phrase,weather,Severe weather event occurring,extreme_weather,storm,any_season
weather_503,Tá sé fuar go maith,It is quite cold,phrase,weather,Temperature is low,temperature,cold,winter
weather_504,Tá grian álainn ann,There is beautiful sunshine,phrase,weather,Pleasant sunny conditions,light_conditions,sunny,summer
weather_505,Tá ceobhrán ann,There is drizzle,phrase,weather,Light rain falling,precipitation,drizzle,autumn
```

#### 4.2 Body Parts and Health Expressions
**Purpose**: Test anatomical and health-related phrases
**Test Cases**:

```csv
# Test data: tests/data/health_phrases.csv
id,firish,english,part_of_speech,category,definition,body_system,health_aspect,severity_level
health_601,Tá tinneas cinn orm,I have a headache,phrase,health,Pain in the head region,nervous_system,pain,mild
health_602,Tá pian i mo dhroim,I have back pain,phrase,health,Pain in the back area,musculoskeletal,pain,moderate
health_603,Tá slaghdán orm,I have a cold,phrase,health,Common respiratory infection,respiratory_system,illness,mild
health_604,Mothaím go dona,I feel sick,phrase,health,General feeling of illness,general,malaise,variable
health_605,Tá mo chroí ag preabadh,My heart is beating fast,phrase,health,Rapid heartbeat sensation,cardiovascular,symptom,mild_to_moderate
```

### 5. Cultural and Register Validation

#### 5.1 Formal vs. Informal Expressions
**Purpose**: Test register-appropriate phrase usage
**Test Cases**:

```csv
# Test data: tests/data/register_phrases.csv
id,firish,english,part_of_speech,category,definition,register_level,social_context,appropriateness
register_701,Gabh mo leithscéal,Excuse me (formal),phrase,politeness,Formal apology or attention-getting,formal,professional/stranger,high
register_702,Tá brón orm,I'm sorry,phrase,politeness,Expression of regret or sympathy,neutral,general_use,high
register_703,Cad é mar atá tú?,How are you? (formal),phrase,greeting,Formal inquiry about wellbeing,formal,professional/elder,high
register_704,Conas tá tú?,How are you? (standard),phrase,greeting,Standard greeting inquiry,neutral,general_use,high
register_705,Céard atá ag tarlú?,What's happening? (informal),phrase,inquiry,Casual question about events,informal,friends/family,medium
```

#### 5.2 Regional Dialect Variations
**Purpose**: Test dialect-specific phrase variations
**Test Cases**:

```csv
# Test data: tests/data/dialect_phrases.csv
id,firish,english,part_of_speech,category,definition,dialect_region,alternative_forms,standard_equivalent
dialect_801,Tá mé ag goil abhaile,I'm going home,phrase,movement,Traveling to one's residence,Ulster,ag dul abhaile,ag dul abhaile
dialect_802,Bhí mé thíos ansin,I was down there,phrase,location,Past presence at a lower location,Munster,bhí mé síos ansin,bhí mé síos ansin
dialect_803,Cá háit a bhfuil tú ag obair?,Where do you work?,phrase,inquiry,Question about employment location,Connacht,cá háit a n-oibríonn tú?,cén áit a n-oibríonn tú?
```

### 6. Error Pattern Detection

#### 6.1 Common Learner Errors
**Purpose**: Test validation of frequently mistaken phrases
**Test Cases**:

```csv
# Test data: tests/data/error_patterns.csv
id,firish,english,part_of_speech,category,definition,common_error,correction,error_type
error_901,*Tá mé ag bheith,*I am being,phrase,existence,Incorrect progressive with 'bí',Tá mé,anglicism
error_902,*Is maith liom ag rith,*I like running,phrase,preference,Incorrect gerund construction,Is maith liom rith,structural_transfer
error_903,*Bhí mé ag teacht go dtí an siopa,*I was coming to the shop,phrase,movement,Redundant directional construction,Bhí mé ag teacht go dtí an siopa,redundancy
```

**Error Detection Validation**:
```python
ERROR_DETECTION_RULES = {
    'invalid_entries': {
        'pattern': r'^\*',  # Asterisk indicates invalid form
        'action': 'flag_as_error_example',
        'category': 'pedagogical_content'
    },
    'correction_field': {
        'required_when': 'common_error present',
        'validation': 'must_be_valid_irish'
    }
}
```

### 7. Comprehensive Validation Tests

#### 7.1 Cross-Reference Consistency
**Purpose**: Ensure phrases reference existing vocabulary
**Test Cases**:

```bash
# Test 7.1.1: Phrase component validation
python -c "
import csv
import sys

# Load main dictionary
main_words = set()
with open('data/dictionary.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        main_words.add(row['firish'].lower().strip())

# Check phrase components
with open('tests/data/basic_phrases.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        phrase = row['firish'].lower()
        # Simple word extraction (improve for real implementation)
        words = phrase.replace(',', '').split()
        for word in words:
            if word not in main_words and len(word) > 2:
                print(f'Warning: {word} in phrase {phrase} not in main dictionary')
"
```

#### 7.2 Semantic Coherence Testing
**Purpose**: Validate logical relationships between phrase components
**Test Cases**:

```python
# Semantic coherence validation script
def validate_semantic_coherence(phrase_data):
    """
    Test semantic coherence of phrases
    """
    coherence_rules = {
        'weather_phrases': {
            'required_elements': ['weather_verb', 'weather_noun'],
            'forbidden_combinations': [('sunny', 'snow'), ('hot', 'ice')]
        },
        'emotion_phrases': {
            'intensity_consistency': True,  # Strong emotions need appropriate verbs
            'cultural_appropriateness': True
        }
    }
    
    # Implementation would check each phrase against these rules
    pass
```

#### 7.3 Usage Frequency Correlation
**Purpose**: Test correlation between phrase complexity and usage frequency
**Test Cases**:

```bash
# Test 7.3.1: Complexity-frequency correlation
python -c "
import csv
import statistics

# Load phrase data
difficulties = []
frequencies = []

with open('tests/data/basic_phrases.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row.get('difficulty') and row.get('frequency'):
            difficulties.append(int(row['difficulty']))
            frequencies.append(int(row['frequency']))

if difficulties and frequencies:
    correlation = statistics.correlation(difficulties, frequencies)
    print(f'Difficulty-Frequency correlation: {correlation:.3f}')
    if correlation < -0.3:  # Expect negative correlation
        print('✅ Expected negative correlation found')
    else:
        print('⚠️  Unexpected correlation pattern')
"
```

## Automated Phrase Validation Pipeline

### 8.1 Complete Validation Script
**Purpose**: Comprehensive automated validation of all phrase types

```bash
#!/bin/bash
# Complete phrase validation pipeline

echo "=== Firish Phrase Validation Pipeline ==="

# Create all test data files
echo "Setting up test data..."

# Run validation on each phrase category
categories=(
    "basic_phrases"
    "complex_phrases" 
    "common_idioms"
    "rare_idioms"
    "verbal_constructions"
    "prepositional_phrases"
    "weather_phrases"
    "health_phrases"
    "register_phrases"
    "dialect_phrases"
)

total_errors=0
total_warnings=0

for category in "${categories[@]}"; do
    echo "Validating $category..."
    
    if [ -f "tests/data/${category}.csv" ]; then
        # Run standard validation
        python tools/validators/validate_lexicon.py "tests/data/${category}.csv" data/schema.json > "tests/output/${category}_results.txt" 2>&1
        
        # Extract error/warning counts
        errors=$(grep -c "ERROR" "tests/output/${category}_results.txt" 2>/dev/null || echo 0)
        warnings=$(grep -c "WARNING" "tests/output/${category}_results.txt" 2>/dev/null || echo 0)
        
        echo "  Errors: $errors, Warnings: $warnings"
        
        total_errors=$((total_errors + errors))
        total_warnings=$((total_warnings + warnings))
    else
        echo "  ⚠️  Test data file not found: tests/data/${category}.csv"
    fi
done

echo ""
echo "=== Phrase Validation Summary ==="
echo "Total Errors: $total_errors"
echo "Total Warnings: $total_warnings"

if [ $total_errors -eq 0 ]; then
    echo "🎉 All phrase validation tests passed!"
    exit 0
else
    echo "💥 Phrase validation found errors"
    exit 1
fi
```

### 8.2 Expected Phrase Validation Outputs

**Successful Phrase Validation**:
```
🔍 FIRISH PHRASE VALIDATION REPORT
================================================================================

📊 SUMMARY:
   Total Entries: 25
   Errors: 0
   Warnings: 3
   Validation: ✅ PASSED

📝 PHRASE ANALYSIS:
   Simple Phrases: 8
   Complex Phrases: 7
   Idioms: 6
   Dialectal Variations: 4

⚠️  WARNINGS (3):
   [WARNING] CULTURAL_CONTEXT | Row 12 | Consider adding cultural usage notes
   [WARNING] REGISTER_CLARITY | Row 18 | Specify formality level
   [WARNING] REGIONAL_VARIATION | Row 23 | Note dialect-specific usage
```

**Failed Phrase Validation**:
```
❌ ERRORS (5):
   [ERROR] MISSING_LITERAL_TRANSLATION | Row 15 | Idiom requires literal translation
   [ERROR] INVALID_PHRASE_STRUCTURE | Row 22 | Phrase doesn't follow Irish syntax patterns
   [ERROR] SEMANTIC_MISMATCH | Row 28 | English translation doesn't match Firish meaning
   [ERROR] MISSING_CULTURAL_CONTEXT | Row 31 | Cultural idiom needs context explanation
   [ERROR] REFERENCE_NOT_FOUND | Row 35 | Phrase components not in main dictionary
```

This comprehensive phrase validation framework ensures that complex linguistic structures, cultural expressions, and idiomatic language are properly validated within the Firish lexicon system.
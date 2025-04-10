# app/rubric/readability_rubric.py

def flesch_reading_ease_rubric():
    return """
### 📘 Flesch Reading Ease (FRE)

**What It Measures:**  
FRE calculates how easy a text is to read based on sentence length and word complexity. Originally for silent reading — adapted here for listening comprehension.

---

**Standard Interpretation**  
| FRE Score | Grade Level        | Meaning               |
|-----------|--------------------|------------------------|
| 90–100    | 5th grade or below | Very Easy              |
| 80–89     | 6th grade          | Easy                   |
| 70–79     | 7th grade          | Fairly Easy            |
| 60–69     | 8th–9th grade      | Standard               |
| 50–59     | 10th–12th grade    | Fairly Difficult       |
| 30–49     | College level      | Difficult              |
| 0–29      | Graduate level     | Very Difficult         |

---

**Adapted for Preschool (Ages 3–5)**  
| FRE Score | Adapted Score | Preschool Interpretation                  |
|-----------|----------------|-------------------------------------------|
| 95–100    | 1.0            | ✅ Very clear — excellent for story time   |
| 90–94.9   | 0.9            | ✅ Easy to follow — strong preschool fit   |
| 85–89.9   | 0.8            | ✅ Approachable — some new vocab           |
| 80–84.9   | 0.6            | ⚠️ Slightly wordy — may need support      |
| 75–79.9   | 0.4            | ⚠️ Could challenge comprehension          |
| < 75      | 0.2 or lower   | ❌ Likely too complex                     |
"""


def fkgl_rubric():
    return """
### 📗 Flesch–Kincaid Grade Level (FKGL)

**What It Measures:**  
Estimates U.S. school grade level based on sentence length and syllables per word. Adapted here for read-aloud suitability.

---

**Standard Interpretation**  
| FKGL Score | Grade Level | Age Range | Meaning                |
|------------|-------------|-----------|-------------------------|
| 0.0–0.9    | K–Grade 1   | 5–6 yrs   | Very simple             |
| 1.0–1.9    | Grade 1–2   | 6–7 yrs   | Early reader            |
| 2.0–2.9    | Grade 2–3   | 7–8 yrs   | Beginner fluency        |
| 3.0–4.9    | Grade 3–5   | 8–10 yrs  | Moderate difficulty     |
| 5.0+       | Grade 6+    | 11+ yrs   | Fluent reader required  |

---

**Adapted for Preschool (Ages 3–5)**  
| FKGL Score | Adapted Score | Preschool Interpretation                      |
|------------|----------------|-----------------------------------------------|
| 0.0–1.0    | 1.0            | ✅ Simple and clear — ideal for young children |
| 1.1–1.5    | 0.8            | ✅ Mostly easy — occasional new vocab          |
| 1.6–2.0    | 0.6            | ⚠️ Slightly complex — needs guidance          |
| 2.1–2.5    | 0.4            | ⚠️ Challenging — not ideal for solo listening |
| 2.6–3.0    | 0.2            | ❌ Too complex without support                |
| > 3.0      | 0.1 or 0.0     | ❌ Inappropriate for preschool listeners       |
"""


def spache_rubric():
    return """
### 📙 Spache Readability Formula

**What It Measures:**  
Designed for early readers (Grades 1–3). Focuses on average sentence length and number of “unfamiliar” words outside a basic vocabulary list.

---

**Standard Interpretation**  
| Spache Score | Grade Level | Meaning                  |
|--------------|-------------|---------------------------|
| ≤ 1.0        | Grade 1     | Beginner-level            |
| 1.1–1.9      | Grade 2     | Early reader              |
| 2.0–2.9      | Grade 3     | Moderate difficulty       |
| ≥ 3.0        | Grade 4+    | Too difficult for early readers |

---

**Adapted for Preschool (Ages 3–5)**  
| Spache Score | Adapted Score | Preschool Interpretation                     |
|--------------|----------------|----------------------------------------------|
| ≤ 1.0        | 1.0            | ✅ Very accessible — mostly familiar words    |
| 1.1–1.5      | 0.8            | ✅ Still friendly — minor new vocab exposure  |
| 1.6–2.0      | 0.6            | ⚠️ Some complexity — may need support        |
| 2.1–2.5      | 0.4            | ⚠️ Challenging for age group                 |
| 2.6–3.0      | 0.2            | ❌ Too difficult — vocab is too advanced     |
| > 3.0        | 0.1 or 0.0     | ❌ Not suitable without adult mediation       |
"""


def dale_chall_rubric():
    return """
### 📕 Dale–Chall Readability Formula

**What It Measures:**  
Assesses text based on average sentence length and % of words not found in a list of 3,000 familiar words (targeted at Grade 4+ readers).

---

**Standard Interpretation**  
| Score      | Grade Level      | Meaning            |
|------------|------------------|---------------------|
| ≤ 4.9      | Grade 4 and below| Very easy           |
| 5.0–5.9    | Grade 5–6        | Easy                |
| 6.0–6.9    | Grade 7–8        | Somewhat difficult  |
| 7.0–8.9    | Grade 9–10       | Difficult           |
| 9.0–10.0   | Grade 11–12      | Very difficult      |

---

**Adapted for Preschool (Ages 3–5)**  
| Score Range | Adapted Score | Preschool Interpretation                         |
|-------------|----------------|--------------------------------------------------|
| ≤ 4.9       | 1.0            | ✅ Excellent — vocabulary is very age-appropriate |
| 5.0–5.5     | 0.8            | ✅ Still good — minimal complexity                |
| 5.6–6.0     | 0.6            | ⚠️ Some hard words — explain during reading      |
| 6.1–6.5     | 0.4            | ⚠️ Many unfamiliar terms — comprehension dips    |
| 6.6–7.0     | 0.2            | ❌ High density of abstract/rare words           |
| > 7.0       | 0.1 or 0.0     | ❌ Not suitable without heavy support             |
"""


def readability_composite_rubric():
    return """
### 🧮 Composite Readability Score

**What It Measures:**  
An average of all four developmental readability metrics (FRE, FKGL, Spache, Dale-Chall) to give a holistic snapshot of developmental fit.

---

| Composite Score | Interpretation                                     |
|------------------|----------------------------------------------------|
| 0.85 – 1.0       | ✅ Excellent — perfect for preschool storytime      |
| 0.65 – 0.84      | ✅ Very good — age-appropriate with mild challenge  |
| 0.45 – 0.64      | ⚠️ Somewhat challenging — requires support          |
| < 0.45           | ❌ Too complex — likely not age-appropriate         |
"""

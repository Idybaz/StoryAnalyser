def repetition_rubric():
    return """
### 🔁 Repetition (Engagement)

**What It Measures:**  
Counts repeated phrases or short n-grams to detect rhythmic, patterned storytelling.

---

| Repetition Density | Adapted Score | Interpretation                        |
|--------------------|----------------|---------------------------------------|
| > 0.12             | 1.0            | ✅ Excellent — very engaging repetition |
| 0.08–0.12          | 0.8            | ✅ Strong — child-friendly patterning   |
| 0.05–0.07          | 0.6            | ⚠️ Moderate — could benefit from more   |
| < 0.05             | 0.4            | ❌ Underused — not very engaging        |
"""

def rhyme_rubric():
    return """
### 🎶 Rhyme (Engagement)

**What It Measures:**  
Detects sound similarity between nearby words — important for phonological awareness and rhythm.

---

| Rhyme Density | Adapted Score | Interpretation                          |
|---------------|----------------|-----------------------------------------|
| > 0.08        | 1.0            | ✅ Musical and playful — highly engaging |
| 0.05–0.08     | 0.8            | ✅ Good use of rhyme                      |
| 0.03–0.05     | 0.6            | ⚠️ Limited rhyme                         |
| < 0.03        | 0.4            | ❌ No rhyme — low musicality             |
"""

def question_rubric():
    return """
### ❓ Questions (Engagement)

**What It Measures:**  
Proportion of interactive or question-based sentences, which invite child response and attention.

---

| Question Ratio | Adapted Score | Interpretation                       |
|----------------|----------------|--------------------------------------|
| > 0.15         | 1.0            | ✅ Highly interactive                  |
| 0.10–0.15      | 0.8            | ✅ Encouraging curiosity               |
| 0.05–0.09      | 0.6            | ⚠️ Limited prompting                  |
| < 0.05         | 0.4            | ❌ Little to no interactivity         |
"""

def sound_effect_rubric():
    return """
### 💥 Sound Effects (Engagement)

**What It Measures:**  
Looks for onomatopoeia, exclamations, and playful sounds — great for read-aloud energy.

---

| Sound Effect Density | Adapted Score | Interpretation                     |
|----------------------|----------------|------------------------------------|
| > 0.06               | 1.0            | ✅ Very fun — high engagement       |
| 0.04–0.06            | 0.8            | ✅ Engaging, expressive              |
| 0.02–0.03            | 0.6            | ⚠️ Underused                        |
| < 0.02               | 0.4            | ❌ Flat — lacks sensory interest     |
"""

# Optional if you want a composite explanation:
def engagement_composite_rubric():
    return """
### 🧮 Composite Engagement Score

**How It’s Calculated:**  
A weighted average of the 4 components:

- 30% Repetition  
- 30% Rhyme  
- 20% Questions  
- 20% Sound Effects

---

| Composite Score | Interpretation                    |
|------------------|-----------------------------------|
| 0.85 – 1.0       | ⭐ Highly engaging — great for 3–5 |
| 0.65 – 0.84      | ✅ Good engagement                 |
| 0.45 – 0.64      | ⚠️ Could improve interaction       |
| < 0.45           | ❌ May not hold preschool interest |
"""

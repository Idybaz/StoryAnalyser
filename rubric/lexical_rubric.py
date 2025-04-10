def ttr_rubric():
    return """
### 🔠 TTR (Type-Token Ratio)

**What It Measures:**  
TTR = Unique words ÷ Total words. It’s a quick measure of how diverse the vocabulary is.

---

**Standard Interpretation (Typical Range)**  
| TTR Score | Interpretation              |
|-----------|-----------------------------|
| > 0.75    | Very high lexical diversity |
| 0.60–0.75 | High lexical diversity       |
| 0.45–0.59 | Moderate diversity           |
| < 0.45    | Low lexical diversity        |

---

**Adapted for Preschool (Ages 3–5)**  
| TTR Score | Adapted Score (0–1) | Preschool Interpretation                      |
|-----------|---------------------|-----------------------------------------------|
| 0.50–0.65 | 1.0                 | ✅ Balanced — strong repetition + variety     |
| 0.66–0.75 | 0.9                 | ✅ Rich vocab — may introduce new words       |
| 0.40–0.49 | 0.7                 | ⚠️ Slightly repetitive — still developmentally fine |
| < 0.40    | 0.4                 | ❌ Too repetitive — limited learning exposure |
| > 0.75    | 0.5                 | ⚠️ High variation — may challenge comprehension |
"""

def mattr_rubric():
    return """
### 📈 MATTR (Moving Average Type-Token Ratio)

**What It Measures:**  
MATTR calculates vocabulary diversity over sliding windows — it’s more reliable across text lengths than raw TTR.

---

**Standard Interpretation**  
| MATTR Score | Interpretation             |
|-------------|----------------------------|
| > 0.80      | Very high diversity        |
| 0.70–0.80   | Typical adult text         |
| 0.60–0.69   | Simple or repetitive       |
| < 0.60      | Very repetitive / patterned|

---

**Adapted for Preschool (Ages 3–5)**  
| MATTR Score | Adapted Score (0–1) | Preschool Interpretation                        |
|-------------|---------------------|-------------------------------------------------|
| 0.68–0.75   | 1.0                 | ✅ Ideal mix of repetition and new words        |
| 0.64–0.67   | 0.9                 | ✅ Rich but not overwhelming                    |
| 0.60–0.63   | 0.7                 | ⚠️ Slightly repetitive — still developmentally useful |
| 0.55–0.59   | 0.5                 | ⚠️ Low richness                                 |
| < 0.55      | 0.3                 | ❌ Too repetitive — limited vocab exposure      |
| > 0.75      | 0.4                 | ❌ May overload working memory                  |
"""

def mtld_rubric():
    return """
### 🔡 MTLD (Measure of Textual Lexical Diversity)

**What It Measures:**  
MTLD measures how many words it takes for vocabulary repetition to reduce the diversity below a threshold. It’s stable even on longer texts.

---

**Standard Interpretation**  
| MTLD Score | Interpretation              |
|------------|-----------------------------|
| > 100      | Very high diversity         |
| 80–100     | High diversity              |
| 60–79      | Moderate diversity          |
| < 60       | Low lexical diversity       |

---

**Adapted for Preschool (Ages 3–5)**  
| MTLD Score | Adapted Score (0–1) | Preschool Interpretation                           |
|------------|---------------------|----------------------------------------------------|
| 60–80      | 1.0                 | ✅ Balanced — great for word learning              |
| 50–59      | 0.8                 | ✅ Good — age-appropriate variety                  |
| 40–49      | 0.6                 | ⚠️ Slightly repetitive — could use more richness   |
| 30–39      | 0.4                 | ⚠️ Too simple — may feel boring                    |
| < 30       | 0.2                 | ❌ Very limited vocabulary                         |
| > 80       | 0.4                 | ❌ Possibly overwhelming or abstract               |
"""

def hdd_rubric():
    return """
### 🔢 HDD (Hypergeometric Distribution Diversity)

**What It Measures:**  
HDD estimates the likelihood that a randomly chosen word is unique. It’s mathematically stable and great for short texts.

---

**Standard Interpretation**  
| HDD Score | Interpretation             |
|-----------|----------------------------|
| > 0.85    | Very high diversity        |
| 0.70–0.85 | High diversity             |
| 0.60–0.69 | Moderate                   |
| < 0.60    | Low lexical diversity      |

---

**Adapted for Preschool (Ages 3–5)**  
| HDD Score | Adapted Score (0–1) | Preschool Interpretation                             |
|-----------|---------------------|------------------------------------------------------|
| 0.70–0.85 | 1.0                 | ✅ Excellent variety — well balanced                 |
| 0.60–0.69 | 0.8                 | ✅ Rich vocabulary — age-aligned                     |
| 0.50–0.59 | 0.6                 | ⚠️ Slightly repetitive — still acceptable            |
| 0.40–0.49 | 0.4                 | ⚠️ Under-stimulating — minimal novelty               |
| < 0.40    | 0.2                 | ❌ Too repetitive — limited vocabulary development   |
| > 0.85    | 0.4                 | ❌ May introduce too much novelty too fast           |
"""
def lexical_composite_rubric():
    return """
### 🧮 Lexical Composite Score

**What It Measures:**  
The composite score combines TTR, MATTR, MTLD, and HDD to reflect the overall **vocabulary richness** and **variety** in a way that’s developmentally appropriate for ages 3–5.

It balances two key needs:
- 🔁 Repetition (helps with memory and language acquisition)
- 🌱 Novelty (introduces new words and concepts)

---

| Composite Score | Interpretation                                         |
|------------------|--------------------------------------------------------|
| 0.85 – 1.0       | ✅ Excellent balance — rich but not overwhelming       |
| 0.70 – 0.84      | ✅ Strong variety — supports word learning             |
| 0.55 – 0.69      | ⚠️ Moderate diversity — could use more richness        |
| 0.40 – 0.54      | ⚠️ Limited variety — may feel flat or repetitive       |
| < 0.40           | ❌ Very low diversity — may not support vocabulary growth |

"""

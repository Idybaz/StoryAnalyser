def eyfs_similarity_rubric():
    return """
### 🌱 EYFS Theme Similarity Rubric

This rubric helps interpret how well the story aligns with Early Years Foundation Stage (EYFS) curriculum themes based on text similarity scores.

---

| Similarity Score | Interpretation                              |
|------------------|----------------------------------------------|
| **0.30 – 1.00**  | ✅ **Strong alignment** — highly relevant to this EYFS theme |
| **0.20 – 0.29**  | 👍 **Moderate alignment** — some overlap with curriculum concepts |
| **0.10 – 0.19**  | ⚠️ **Weak alignment** — theme is loosely reflected |
| **Below 0.10**   | ❌ **No significant alignment** — unlikely to support this theme directly |

---

**Note:** These scores are computed using semantic similarity (Sentence-BERT), not keyword matching — so even if words don't match exactly, ideas can still align well.

✅ High scores often reflect story elements like:
- Friendship and emotions  
- Communication and conversation  
- Curiosity, helping, and imaginative play

📉 Lower scores may simply mean the theme is not a focus — not necessarily a bad story!
"""

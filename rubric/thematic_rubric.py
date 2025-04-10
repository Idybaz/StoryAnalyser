def thematic_rubric():
    return """
### 🧠 Thematic Analysis Rubric

**What It Shows:**  
This section identifies what the story is about — both from the most frequent content words and from AI-inferred phrases.

---

#### 🔠 Top Theme Words (Frequency-Based)

These are the most common **nouns and verbs** found in the story.
They often represent key characters, actions, or settings.

| Example | Interpretation |
|--------|----------------|
| `friend`, `share`, `hug` | Theme: Friendship / Empathy |
| `run`, `jump`, `ball` | Theme: Play / Movement |
| `witch`, `spell`, `curse` | Theme: Fantasy / Conflict |

✅ Great for identifying surface-level ideas.

---

#### 💡 Semantic Theme Phrases (KeyBERT)

These are short, meaningful phrases extracted using a language model.  
They reflect the deeper structure and context of the story — even when words aren't repeated.

| Example Phrase | Possible Interpretation |
|----------------|-------------------------|
| **"sea adventure"** | Exploration / Nature |
| **"help friend"** | Cooperation / Social Skills |
| **"monster chase"** | Excitement / Problem Solving |

✅ Helpful for curriculum alignment (EYFS links)
✅ Great for educators selecting stories with thematic intent

---

**Note:** No numeric score is shown — this analysis supports interpretation, not judgment.
"""

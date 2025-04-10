def sentiment_emotion_rubric():
    return """
### 🧪 VADER Sentiment Score Guide

| Score Type | Range         | Interpretation                                 |
|------------|---------------|------------------------------------------------|
| **Compound** | -1.0 to +1.0 | Overall emotional tone of the text             |
| > 0.5      | Strong Positive | 😊 Uplifting or cheerful                      |
| 0.1 – 0.5  | Mild Positive   | 🙂 Lightly positive or warm                   |
| -0.1 – 0.1 | Neutral         | 😐 Flat or emotionally balanced               |
| -0.5 – -0.1| Mild Negative   | 🙁 Slight tension, sadness, or concern        |
| < -0.5     | Strong Negative | 😞 Possibly distressing or dark               |

| **Positive / Negative / Neutral** | Range: 0.0 – 1.0 | These represent the proportion of sentences leaning toward that tone. They always add up to ~1.0. |

---

### 🎭 Emotion Score Guide (BERT-Based)

| Emotion     | What It Signals                                               |
|-------------|---------------------------------------------------------------|
| **Joy**     | 😊 Happiness, safety, friendship — great for early learners   |
| **Surprise**| 😮 Discovery, curiosity — can be positive or neutral          |
| **Trust**   | 🤝 Safety, kindness, reliability — essential for preschoolers |
| **Sadness** | 😢 Loss, separation — okay if resolved in the story           |
| **Fear**    | 😱 Uncertainty or threat — best with comforting resolution    |
| **Disgust** | 😖 Dislike or repulsion — use sparingly                       |
| **Anger**   | 😠 Frustration or unfairness — okay if modeled constructively |
| **Neutral** | 😐 Background tone — filler, not emotionally charged          |

💡 **Tips for Educators & Parents:**
- Look for **dominant emotions** with scores over ~0.15–0.20.
- A healthy mix of **joy, trust, surprise** usually indicates emotionally engaging stories.
- If **fear, anger, or sadness** are high, check that the story **resolves positively**.
"""

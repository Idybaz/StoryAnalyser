# normalized/engagement.py

def normalize_repetition(rep):
    if rep > 0.12:
        return 1.0
    elif 0.08 <= rep <= 0.12:
        return 0.8
    elif 0.05 <= rep < 0.08:
        return 0.6
    elif rep < 0.05:
        return 0.4
    return 0.6

def normalize_rhyme(rhyme):
    if rhyme > 0.08:
        return 1.0
    elif 0.05 <= rhyme <= 0.08:
        return 0.8
    elif 0.03 <= rhyme < 0.05:
        return 0.6
    elif rhyme < 0.03:
        return 0.4
    return 0.6

def normalize_question_ratio(q_ratio):
    if q_ratio > 0.15:
        return 1.0
    elif 0.10 <= q_ratio <= 0.15:
        return 0.8
    elif 0.05 <= q_ratio < 0.10:
        return 0.6
    elif q_ratio < 0.05:
        return 0.4
    return 0.6

def normalize_sound_effects(se_density):
    if se_density > 0.06:
        return 1.0
    elif 0.04 <= se_density <= 0.06:
        return 0.8
    elif 0.02 <= se_density < 0.04:
        return 0.6
    elif se_density < 0.02:
        return 0.4
    return 0.6

# 🧠 Apply to a single book (in your Streamlit app)
def normalize_engagement_scores(metrics: dict) -> dict:
    """
    Takes raw engagement features from analyze_engagement() and returns scaled scores.
    """
    try:
        repetition_raw = metrics.get("repetition_score", 0)
        rhyme_raw = metrics.get("rhyme_score", 0)
        question_raw = metrics.get("question_ratio", 0)
        sound_raw = metrics.get("sound_effect_density", 0)

        # Normalize individual metrics
        repetition_scaled = normalize_repetition(repetition_raw)
        rhyme_scaled = normalize_rhyme(rhyme_raw)
        question_scaled = normalize_question_ratio(question_raw)
        sound_scaled = normalize_sound_effects(sound_raw)

        # Composite Score with suggested weights
        composite_score = round(
            0.3 * repetition_scaled +
            0.3 * rhyme_scaled +
            0.2 * question_scaled +
            0.2 * sound_scaled, 3
        )

        return {
            "Repetition (Adapted)": repetition_scaled,
            "Rhyme (Adapted)": rhyme_scaled,
            "Questions (Adapted)": question_scaled,
            "Sound Effects (Adapted)": sound_scaled,
            "Engagement Composite Score": composite_score
        }

    except Exception as e:
        return {"error": str(e)}

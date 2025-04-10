def interpret_compound_sentiment(score: float) -> str:
    if score >= 0.5:
        return "✅ Very positive — cheerful and emotionally safe for preschool"
    elif 0.2 <= score < 0.5:
        return "✅ Slightly positive — calm or mildly upbeat tone"
    elif -0.2 < score < 0.2:
        return "⚠️ Neutral or mixed — flat emotional tone, could benefit from variation"
    elif -0.5 < score <= -0.2:
        return "⚠️ Some negativity — story may have conflict or sadness"
    else:
        return "❌ Predominantly negative — may require adult mediation"

def interpret_emotion_profile(emotion_scores: dict) -> str:
    if not emotion_scores:
        return "🤖 No emotions detected — may lack emotional variety or expression."

    top_emotions = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)
    dominant, top_val = top_emotions[0]

    if dominant == "joy" and top_val > 0.2:
        return "😊 Joyful and uplifting — great for emotional bonding and fun read-aloud"
    elif dominant in ["surprise", "neutral", "trust"]:
        return "🧠 Emotionally balanced — may support curiosity, but less emotionally expressive"
    elif dominant in ["sadness", "fear", "anger"]:
        return "⚠️ Negative dominant emotion — story may explore conflict or discomfort"
    else:
        return f"ℹ️ Main emotion is **{dominant}** — context matters in interpretation."

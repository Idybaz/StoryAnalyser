# rubric/interpreters/engagement_interp.py

def interpret_repetition_score(score: float) -> str:
    if score >= 0.9:
        return "✅ Excellent — strong repeated patterns help children predict and participate."
    elif score >= 0.7:
        return "✅ Good use — repetition reinforces rhythm and recall."
    elif score >= 0.5:
        return "⚠️ Moderate — could use more repetition for language learning."
    else:
        return "❌ Lacks repetition — may not hold attention or support memory."


def interpret_rhyme_score(score: float) -> str:
    if score >= 0.9:
        return "✅ Highly musical — rhyme supports phonological awareness and fun reading aloud."
    elif score >= 0.7:
        return "✅ Strong — rhyme adds energy and structure."
    elif score >= 0.5:
        return "⚠️ Limited — consider adding expression when reading."
    else:
        return "❌ Low rhyme — less rhythm, may feel flat during read-alouds."


def interpret_question_score(score: float) -> str:
    if score >= 0.9:
        return "✅ Very interactive — invites constant engagement and response."
    elif score >= 0.7:
        return "✅ Encourages participation — helps spark curiosity."
    elif score >= 0.5:
        return "⚠️ Somewhat prompting — a few questions, but not consistent."
    else:
        return "❌ Lacks interaction — children may stay passive while listening."


def interpret_sound_effect_score(score: float) -> str:
    if score >= 0.9:
        return "✅ Super expressive — playful sounds make the story fun and immersive."
    elif score >= 0.7:
        return "✅ Adds flair — helps children visualize and react."
    elif score >= 0.5:
        return "⚠️ Mild use — could benefit from added expression or vocal play."
    else:
        return "❌ Very little — may feel too flat or serious for young audiences."


def interpret_engagement_composite(score: float) -> str:
    if score >= 0.9:
        return "✅ Highly engaging — encourages participation, rhythm, and expressive reading."
    elif score >= 0.75:
        return "✅ Strong — well-suited for fun and interactive story time."
    elif score >= 0.6:
        return "⚠️ Mixed — some features present, but may need more performance or support."
    elif score >= 0.4:
        return "⚠️ Low engagement — might not capture attention without extra effort."
    else:
        return "❌ Not engaging — may not hold interest or support active listening."

# rubric/interpreters/lexical_interp.py

def interpret_ttr_score(score: float) -> str:
    if score >= 0.9:
        return "✅ Great balance — the vocabulary is rich without being overwhelming."
    elif score >= 0.7:
        return "✅ Repetitive enough for learning, but includes variety to build vocabulary."
    elif score >= 0.5:
        return "⚠️ Slightly repetitive — good for reinforcing key words, but may lack variety."
    elif score >= 0.4:
        return "⚠️ Heavy repetition — may feel dull or overly simplistic."
    else:
        return "❌ Too repetitive — may not expose children to enough new vocabulary."


def interpret_mattr_score(score: float) -> str:
    if score >= 0.9:
        return "✅ Vocabulary is well-varied and developmentally appropriate."
    elif score >= 0.7:
        return "✅ Good mix — reinforces concepts while introducing new words."
    elif score >= 0.5:
        return "⚠️ Slightly limited — some repetition, may need vocabulary support."
    elif score >= 0.3:
        return "⚠️ Not very diverse — word usage may feel too narrow."
    else:
        return "❌ Low diversity — unlikely to support language development."


def interpret_mtld_score(score: float) -> str:
    if score >= 0.9:
        return "✅ Excellent variation — supports rich language exposure."
    elif score >= 0.7:
        return "✅ Varied language — introduces a healthy range of vocabulary."
    elif score >= 0.5:
        return "⚠️ Moderate repetition — fine for basic listening, but not very stimulating."
    elif score >= 0.3:
        return "⚠️ Quite repetitive — useful for very young children or repetition learning."
    else:
        return "❌ Limited vocabulary — may not engage children beyond initial readings."


def interpret_hdd_score(score: float) -> str:
    if score >= 0.9:
        return "✅ Highly diverse — lots of unique words that support growth."
    elif score >= 0.7:
        return "✅ Balanced diversity — ideal mix of repetition and novelty."
    elif score >= 0.5:
        return "⚠️ Somewhat narrow — vocabulary is serviceable but not enriching."
    elif score >= 0.3:
        return "⚠️ Limited word pool — may feel flat after multiple readings."
    else:
        return "❌ Too simple — low variety may reduce developmental impact."


def interpret_lexical_composite(score: float) -> str:
    if score >= 0.9:
        return "✅ Excellent lexical variety — ideal for building early vocabulary and concept understanding."
    elif score >= 0.75:
        return "✅ Strong diversity — supports both repetition and language growth."
    elif score >= 0.6:
        return "⚠️ Mixed — provides some variety but might lack richness."
    elif score >= 0.4:
        return "⚠️ Limited — not enough diversity to stretch vocabulary."
    else:
        return "❌ Very low diversity — may not stimulate language development."

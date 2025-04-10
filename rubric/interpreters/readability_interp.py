# interpret_fre_score(score: float)
def interpret_fre_score(score: float) -> str:
    if score >= 90:
        return "✅ Excellent — very clear and easy to follow aloud for preschoolers."
    elif score >= 85:
        return "✅ Strong — mostly simple sentences with good rhythm."
    elif score >= 80:
        return "✅ Age-appropriate — some complexity but still manageable."
    elif score >= 75:
        return "⚠️ Slightly complex — may require adult pacing or emphasis."
    elif score >= 70:
        return "⚠️ Noticeably dense — young children may lose focus without support."
    else:
        return "❌ Difficult — language likely exceeds preschool comprehension."

# interpret_fkgl_score(score: float)
def interpret_fkgl_score(score: float) -> str:
    if score <= 1.0:
        return "✅ Excellent — simple structure, perfect for ages 3–5."
    elif score <= 1.5:
        return "✅ Very accessible — with light adult support."
    elif score <= 2.0:
        return "✅ Acceptable — includes some new words or longer phrases."
    elif score <= 2.5:
        return "⚠️ Slightly challenging — may need explanation or repetition."
    elif score <= 3.0:
        return "⚠️ Advanced — likely harder to follow without guidance."
    else:
        return "❌ Too complex — exceeds preschool language capacity."

# interpret_spache_score(score: float)
def interpret_spache_score(score: float) -> str:
    if score <= 1.0:
        return "✅ Beginner-friendly — vocabulary is familiar and accessible."
    elif score <= 1.5:
        return "✅ Still age-appropriate — introduces a few new words."
    elif score <= 2.0:
        return "✅ Acceptable — some vocabulary may be unfamiliar."
    elif score <= 2.5:
        return "⚠️ Less familiar — may require adult help with new terms."
    elif score <= 3.0:
        return "⚠️ Advanced — many words may need explanation."
    else:
        return "❌ Too difficult — vocabulary is not developmentally aligned."


# interpret_dale_chall_score(score: float)
def interpret_dale_chall_score(score: float) -> str:
    if score <= 4.9:
        return "✅ Excellent — uses common, familiar vocabulary."
    elif score <= 5.5:
        return "✅ Great fit — light challenge with accessible words."
    elif score <= 6.0:
        return "✅ Acceptable — some abstract or rare words appear."
    elif score <= 6.5:
        return "⚠️ Complex — many terms may confuse preschoolers."
    elif score <= 7.0:
        return "⚠️ High difficulty — likely needs guided reading."
    else:
        return "❌ Too advanced — unsuitable for early childhood levels."

#  interpret_readability_composite(score: float)
def interpret_readability_composite(score: float) -> str:
    if score >= 0.85:
        return "✅ Excellent — highly suited for preschool comprehension and attention."
    elif score >= 0.70:
        return "✅ Good — mostly readable, with minor challenges."
    elif score >= 0.50:
        return "⚠️ Mixed — parts may be difficult without adult support."
    elif score >= 0.30:
        return "⚠️ Hard to follow — regular guidance likely needed."
    else:
        return "❌ Too complex — likely inappropriate for independent or interactive preschool reading."


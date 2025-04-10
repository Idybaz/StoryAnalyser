# --- Normalization Functions ---

def normalize_ttr(ttr):
    if 0.50 <= ttr <= 0.65:
        return 1.0
    elif 0.66 <= ttr <= 0.75:
        return 0.9
    elif 0.40 <= ttr < 0.50:
        return 0.7
    elif ttr < 0.40:
        return 0.4
    elif ttr > 0.75:
        return 0.5
    else:
        return 0.6  # fallback

def normalize_mattr(mattr):
    if 0.68 <= mattr <= 0.75:
        return 1.0
    elif 0.64 <= mattr < 0.68:
        return 0.9
    elif 0.60 <= mattr < 0.64:
        return 0.7
    elif 0.55 <= mattr < 0.60:
        return 0.5
    elif mattr < 0.55:
        return 0.3
    elif mattr > 0.75:
        return 0.6 
    else:
        return 0.6

def normalize_mtld(mtld):
    if 60 <= mtld <= 80:
        return 1.0
    elif 50 <= mtld < 60:
        return 0.8
    elif 40 <= mtld < 50:
        return 0.6
    elif 30 <= mtld < 40:
        return 0.4
    elif mtld < 30:
        return 0.2
    elif mtld > 80:
        return 0.4
    else:
        return 0.6

def normalize_hdd(hdd):
    if 0.70 <= hdd <= 0.85:
        return 1.0
    elif 0.60 <= hdd < 0.70:
        return 0.8
    elif 0.50 <= hdd < 0.60:
        return 0.6
    elif 0.40 <= hdd < 0.50:
        return 0.4
    elif hdd < 0.40:
        return 0.2
    elif hdd > 0.85:
        return 0.6 
    else:
        return 0.6


def normalize_lexical_scores(scores):
    ttr = normalize_ttr(scores.get("ttr", 0))
    mattr = normalize_mattr(scores.get("mattr", 0))
    mtld = normalize_mtld(scores.get("mtld", 0))
    hdd = normalize_hdd(scores.get("hdd", 0))

    composite = round((ttr + mattr + mtld + hdd) / 4, 3)

    return {
        "TTR (Adapted)": ttr,
        "MATTR (Adapted)": mattr,
        "MTLD (Adapted)": mtld,
        "HDD (Adapted)": hdd,
        "lexical_composite": composite
    }
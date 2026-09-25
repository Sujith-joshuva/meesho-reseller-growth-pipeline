def mom_growth(previous: float, current: float) -> float: 
    return round((current - previous) / previous * 100, 2)

def is_flagged(mom_pct:float, threshold:float=8.0) -> str:
    if abs(mom_pct) > threshold:
        return "flagged"
    elif abs(mom_pct) < threshold:
        return "not_flagged"
    else:
        return "escalate_exact_boundary"
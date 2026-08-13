"""Entropy-based analyzers."""
from typing import List
from collections import Counter
import math

def shannon_entropy(values: List[float], bins: int = 10) -> float:
    """Compute a simple Shannon entropy over binned values."""
    if not values:
        return 0.0
    mn = min(values)
    mx = max(values)
    if mn == mx:
        return 0.0
    # simple binning
    width = (mx - mn) / bins
    counts = [0] * bins
    for v in values:
        idx = int((v - mn) / width)
        if idx == bins:
            idx = bins - 1
        counts[idx] += 1
    total = len(values)
    ent = 0.0
    for c in counts:
        if c == 0:
            continue
        p = c / total
        ent -= p * math.log2(p)
    return ent

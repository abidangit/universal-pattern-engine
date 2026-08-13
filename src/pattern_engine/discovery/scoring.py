"""Candidate scoring utilities for discovery."""
from typing import List, Dict, Any
import math

def mean_squared_error(a: List[float], b: List[float]) -> float:
    n = min(len(a), len(b))
    if n == 0:
        return float('inf')
    return sum((a[i]-b[i])**2 for i in range(n))/n

def score_candidate(candidate_seq: List[float], target_seq: List[float]) -> Dict[str, Any]:
    """Return a score object where lower error is better. Score is normalized to [0,1]."""
    mse = mean_squared_error(candidate_seq, target_seq)
    # convert to score where 1.0 is perfect
    score = 1.0 / (1.0 + mse)
    return {"mse": mse, "score": score}

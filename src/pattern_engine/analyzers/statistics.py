"""Basic statistical analyzers used by pattern analyzers."""
from typing import List, Dict
import math

def mean(values: List[float]) -> float:
    return sum(values) / len(values) if values else 0.0

def variance(values: List[float]) -> float:
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values) if values else 0.0

def summary(values: List[float]) -> Dict[str, float]:
    return {"mean": mean(values), "variance": variance(values), "min": min(values) if values else 0.0, "max": max(values) if values else 0.0}

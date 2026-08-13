"""Geometric sequence generator."""
from typing import List

def geometric_sequence(start: float, ratio: float, n: int) -> List[float]:
    return [start * (ratio ** i) for i in range(n)]

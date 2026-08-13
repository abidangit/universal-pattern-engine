"""Ratio transforms for sequences."""
from typing import List

def ratios(values: List[float]) -> List[float]:
    result = []
    for i in range(len(values)-1):
        a = values[i]
        b = values[i+1]
        if a == 0:
            result.append(float('inf'))
        else:
            result.append(b / a)
    return result

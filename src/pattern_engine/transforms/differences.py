"""Difference transforms for sequences."""
from typing import List

def differences(values: List[float], order: int = 1) -> List[List[float]]:
    result = []
    current = list(values)
    for _ in range(order):
        if len(current) < 2:
            break
        current = [current[i+1] - current[i] for i in range(len(current)-1)]
        result.append(current)
    return result

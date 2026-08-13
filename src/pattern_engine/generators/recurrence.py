"""Simple linear recurrence generator.
Supports recurrences of the form a_n = sum(c_i * a_{n-1-i}) with given initial values.
"""
from typing import List

def recurrence_sequence(coeffs: List[float], init: List[float], n: int) -> List[float]:
    seq = list(init)
    k = len(coeffs)
    while len(seq) < n:
        next_val = 0
        for i, c in enumerate(coeffs):
            next_val += c * seq[-1 - i]
        seq.append(next_val)
    return seq[:n]

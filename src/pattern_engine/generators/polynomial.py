"""Polynomial sequence generator for integer coefficients."""
from typing import List

def polynomial_sequence(coeffs: List[float], n: int) -> List[float]:
    """Given coeffs [a0, a1, a2...] produce sequence a0 + a1*n + a2*n^2 ... for n starting at 1."""
    seq = []
    for i in range(1, n+1):
        value = 0
        for p, c in enumerate(coeffs):
            value += c * (i ** p)
        seq.append(value)
    return seq

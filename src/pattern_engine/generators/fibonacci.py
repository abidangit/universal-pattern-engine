"""Fibonacci and related generators."""
from typing import List

def fibonacci(n: int, a: int = 0, b: int = 1) -> List[int]:
    seq = []
    if n <= 0:
        return seq
    seq = [a, b][:n]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

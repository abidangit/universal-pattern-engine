"""Simple sequence generators."""
from typing import List

def arithmetic_sequence(start: float, diff: float, n: int) -> List[float]:
    """Generate an arithmetic sequence: a, a+d, a+2d, ..."""
    return [start + i * diff for i in range(n)]

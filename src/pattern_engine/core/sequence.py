"""Sequence utilities and basic abstractions."""
from typing import List, Optional

class Sequence:
    """Simple sequence wrapper providing analysis helpers."""
    def __init__(self, values: List[float]):
        self.values = list(values)

    def differences(self, order: int = 1) -> List[List[float]]:
        """Return successive difference arrays up to `order`.
        E.g., differences(order=2) returns [first_diff, second_diff]."""
        result = []
        current = self.values
        for _ in range(order):
            if len(current) < 2:
                break
            current = [current[i+1] - current[i] for i in range(len(current)-1)]
            result.append(current)
        return result

    def is_constant_difference(self, order: int = 1) -> bool:
        diffs = self.differences(order)
        if not diffs:
            return False
        last = diffs[-1]
        return all(abs(x - last[0]) < 1e-9 for x in last)

    @classmethod
    def from_list(cls, values: List[float]) -> 'Sequence':
        return cls(values)

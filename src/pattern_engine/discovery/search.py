"""Discovery helpers: generate simple candidate explanations and score them."""
from typing import List, Dict, Any
from ..core.sequence import Sequence
from ..generators.polynomial import polynomial_sequence

class Discovery:
    def __init__(self):
        pass

    def discover(self, seq: List[float]) -> Dict[str, Any]:
        s = Sequence.from_list(seq)
        # geometric check
        if len(seq) >= 3:
            ratios = [seq[i+1] / seq[i] if seq[i] != 0 else None for i in range(len(seq)-1)]
            if None not in ratios and all(abs(r - ratios[0]) < 1e-9 for r in ratios):
                return {"classification": "geometric", "ratio": ratios[0], "confidence": 0.95}
        # polynomial search by differences up to degree 4
        for deg in range(0,5):
            diffs = s.differences(deg)
            if diffs and all(abs(x - diffs[-1][0]) < 1e-9 for x in diffs[-1]):
                # return simple polynomial degree
                return {"classification": "polynomial", "degree": deg, "confidence": 0.9}
        return {"classification": "unknown", "confidence": 0.0}

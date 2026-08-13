"""Engine: lightweight analysis and discovery helpers (Phase 1)."""
from typing import List, Dict, Any
from .sequence import Sequence

class Engine:
    """Small analyzer that attempts simple discovery rules."""
    def analyze_sequence(self, seq: List[float]) -> Dict[str, Any]:
        s = Sequence.from_list(seq)
        # Check for constant ratio (geometric)
        if len(seq) >= 3:
            ratios = []
            ok = True
            for i in range(len(seq)-1):
                if seq[i] == 0:
                    ok = False
                    break
                ratios.append(seq[i+1] / seq[i])
            if ok and all(abs(r - ratios[0]) < 1e-9 for r in ratios):
                return {"classification": "geometric", "ratio": ratios[0], "confidence": 0.9}
        # Check for polynomial via constant nth difference (up to 4)
        for order in range(1,5):
            if s.is_constant_difference(order):
                return {"classification": "polynomial", "degree": order, "confidence": 0.8}
        # Fallback: unknown / stochastic
        return {"classification": "unknown", "confidence": 0.0}

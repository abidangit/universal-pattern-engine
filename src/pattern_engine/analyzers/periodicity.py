"""Periodicity detection using autocorrelation."""
from typing import List, Optional
import numpy as np

def autocorrelation(values: List[float]) -> List[float]:
    x = np.array(values, dtype=float)
    x = x - x.mean()
    result = np.correlate(x, x, mode='full')
    return result[result.size//2:]

def dominant_period(values: List[float], max_lag: int = 20) -> Optional[int]:
    if len(values) < 3:
        return None
    ac = autocorrelation(values)
    # ignore lag zero
    ac_lags = ac[1:max_lag+1]
    lag = int(np.argmax(ac_lags)) + 1
    if ac_lags[lag-1] <= 0:
        return None
    return lag

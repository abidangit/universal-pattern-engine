"""Growth and trend analyzers."""
from typing import List, Optional

def average_ratio(values: List[float]) -> Optional[float]:
    if not values or len(values) < 2:
        return None
    ratios = []
    for i in range(len(values)-1):
        if values[i] == 0:
            continue
        ratios.append(values[i+1] / values[i])
    return sum(ratios)/len(ratios) if ratios else None

def linear_trend_slope(values: List[float]) -> Optional[float]:
    # simple least-squares slope
    if not values or len(values) < 2:
        return None
    n = len(values)
    x = list(range(n))
    x_mean = sum(x)/n
    y_mean = sum(values)/n
    num = sum((xi - x_mean)*(yi - y_mean) for xi, yi in zip(x, values))
    den = sum((xi - x_mean)**2 for xi in x)
    if den == 0:
        return None
    return num/den

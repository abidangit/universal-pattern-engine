from pattern_engine.analyzers.entropy import shannon_entropy
from pattern_engine.analyzers.periodicity import dominant_period
from pattern_engine.analyzers.growth import average_ratio, linear_trend_slope


def test_entropy_constant():
    assert shannon_entropy([1,1,1,1]) == 0.0


def test_periodic():
    seq = [1,2,1,2,1,2,1,2]
    p = dominant_period(seq, max_lag=4)
    assert p == 2


def test_growth():
    seq = [2,4,8,16]
    assert average_ratio(seq) is not None
    assert linear_trend_slope(seq) is not None

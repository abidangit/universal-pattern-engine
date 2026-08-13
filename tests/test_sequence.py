from pattern_engine.core.sequence import Sequence
from pattern_engine.core.engine import Engine
from pattern_engine.generators.arithmetic import arithmetic_sequence


def test_differences_and_polynomial_classification():
    seq = [1,4,9,16,25,36]
    s = Sequence.from_list(seq)
    diffs = s.differences(2)
    assert len(diffs) >= 2
    assert diffs[1] == [2,2,2,2]

    engine = Engine()
    r = engine.analyze_sequence(seq)
    assert r["classification"] == "polynomial"


def test_arithmetic_generator_and_engine():
    seq = arithmetic_sequence(2, 3, 6)  # 2,5,8,11,14,17
    engine = Engine()
    r = engine.analyze_sequence(seq)
    assert r["classification"] == "polynomial"

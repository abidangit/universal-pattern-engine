from pattern_engine.discovery.scoring import score_candidate


def test_score_perfect():
    a = [1,2,3]
    b = [1,2,3]
    r = score_candidate(a,b)
    assert r['mse'] == 0
    assert r['score'] == 1.0


def test_score_bad():
    a = [1,2,3]
    b = [10,10,10]
    r = score_candidate(a,b)
    assert r['mse'] > 0
    assert r['score'] < 0.1

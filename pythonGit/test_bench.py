from GitCalc import add, sub, mut, div

def test_add() -> None:
    alpha, beta = 1, 2
    result = add(alpha=alpha, beta=beta)
    assert alpha + beta == result, "Error: function 'add'"

def test_sub() -> None:
    alpha, beta = 1, 2
    result = add(alpha=alpha, beta=beta)
    assert alpha - beta == result, "Error: function 'sub'"

def test_mut() -> None:
    alpha, beta = 1, 2
    result = add(alpha=alpha, beta=beta)
    assert alpha * beta == result, "Error: function 'mut'"

def test_mut() -> None:
    alpha, beta = 1, 2
    result = add(alpha=alpha, beta=beta)
    assert (alpha // beta, alpha % beta) == result, "Error: function 'div'"

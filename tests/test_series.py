from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series


def test_any():
    actual=fibonacci(3)
    expected=2
    assert actual==expected
    
def test_any1():
    actual=lucas(3)
    expected=4
    assert actual==expected


def test_any2():
    actual=sum_series(3,0,1)
    expected=2
    assert actual==expected    
from math_series.series import *

def test_fibonacci():
    actual=fibonacci(3)
    expected=2
    assert actual==expected
    
def test_fibonacci1():
    actual=fibonacci(4)
    expected=3
    assert actual==expected

def test_lucas():
    actual=lucas(3)
    expected=4
    assert actual==expected


def test_lucas1():
    actual=lucas(4)
    expected=7
    assert actual==expected


def test_sum_series():
    actual=sum_series(3)
    expected=2
    assert actual==expected    

    
def test_sum_series1():
    actual=sum_series(3,2,1)
    expected=4
    assert actual==expected    
import pytest
from fuel import convert, gauge

def test_correct_conversion():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/3") == 33
    assert convert("2/3") == 67

def test_correct_gauge():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_non_integer_input():
    with pytest.raises(ValueError):
        convert("A/B")
    with pytest.raises(ValueError):
        convert("A/1")
    with pytest.raises(ValueError):
        convert("1/A")

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

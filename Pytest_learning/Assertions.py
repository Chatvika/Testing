def test_numbers():
    assert 5 == 5
    assert 10 > 2
    assert "hi" in "hii"
    assert True

# ex:
import pytest

def divide(a, b):
    return a / b

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
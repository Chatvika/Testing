
import pytest
from calculator import add,subtract,multiply,divide
from endtoend import run 

'''unit testing '''


def test_add():
    assert add(2,3) ==5

def test_subtract():
    assert subtract(2,3)==-1
def test_multiply():
    assert multiply(2,4) ==8

def test_divide():
    assert divide(4,2) ==2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)


'''integration testing '''
def test_add_and_multiply():
    assert multiply(add(2,3), 5) ==25


'''funcional testing'''
def test_all_functions():
    assert add(2,3) ==5
    assert subtract(3,2)==1
    assert multiply(2,3) ==6
    assert divide(10,2)==5

'''end to end testing '''
def test_endtoend(capsys):
    run()
    out=capsys.readouterr().out
    assert "2 + 3 = 5" in out

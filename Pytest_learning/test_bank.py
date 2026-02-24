
from bank import Bankaccount
import pytest

def test_deposit():
    acc=Bankaccount()
    acc.deposit(100)
    assert acc.get_balance() ==100

def test_withdraw():
    acc=Bankaccount(200)
    acc.withdraw(50)
    assert acc.get_balance()==150

def test_withdraw_more_than_balance():
    acc = Bankaccount(100)
    with pytest.raises(ValueError):
        acc.withdraw(200)


def test_negative_deposit():
    acc = Bankaccount()
    with pytest.raises(ValueError):
        acc.deposit(-50)

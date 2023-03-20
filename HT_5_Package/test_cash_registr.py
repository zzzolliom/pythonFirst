import pytest
from HT_5_Package.utils import cash_register


def test_cash_register_prise_one_bancknote():
    a = [50]
    b = 1.74
    result = cash_register(a, b)
    assert result == [10, 10, 10, 10, 5, 2, 1, 0.1, 0.1, 0.05, 0.01]

def test_cash_register_all_bancknotes():
    a = [5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01]
    b = 6668.66
    result = cash_register(a, b)
    assert result == []

def test_cash_register_without_dot():
    a = [5000, 5000, 5000, 5000, 5000]
    b = 23500
    result = cash_register(a, b)
    assert result == [1000, 500]

def test_cash_register_prise_0():
    a = [10, 10, 10, 10, 0.5]
    b = 0
    with pytest.raises(ValueError):
        cash_register(a, b)

def test_cash_register_not_enough():
    a = [10, 10, 10, 10, 0.5]
    b = 1000
    with pytest.raises(ValueError):
        cash_register(a, b)

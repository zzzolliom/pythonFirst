import pytest
from HW6.HW6_Task4 import random_digit
def test_random_digit_positive():
    a=5
    b=4
    random_digit_lst=random_digit(a,b)
    for i in random_digit_lst:
        if i<a:
            result_1  = True
    if len(random_digit_lst)==b:
        result_2=True
    assert result_1 == True and result_2 == True

def test_random_digit_equal_digit():
    a=1
    b=1
    result=random_digit(a,b)
    assert result == [0]

def test_random_digit_a_less_b():
    a = 5
    b = 10
    with pytest.raises(ValueError):
        random_digit(a, b)

def test_random_digit_a_is_str():
    a = "s"
    b = 10
    with pytest.raises(ValueError):
        random_digit(a, b)

def test_random_digit_equal_b_is_str():
    a = 10
    b = "d"
    with pytest.raises(ValueError):
        random_digit(a, b)

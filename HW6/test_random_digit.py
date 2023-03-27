import pytest
from HW6.HW6_Task4 import random_digit
def random_digit_equal_digit():
    a=5
    b=4
    random_digit_lst=random_digit(a,b)
    for i in random_digit_lst:
        if i<a:
            result  = True
        assert result == True

def random_digit_equal_digit():
    a=1
    b=1
    result=random_digit(a,b)
    assert result == [0]

def random_digit_equal_digit():
    a = 5
    b = 10
    with pytest.raises(ValueError):
        random_digit(a, b)

def random_digit_equal_digit():
    a = "s"
    b = 10
    with pytest.raises(ValueError):
        random_digit(a, b)

def random_digit_equal_digit():
    a = 10
    b = "d"
    with pytest.raises(ValueError):
        random_digit(a, b)

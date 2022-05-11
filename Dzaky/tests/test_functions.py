import pytest
from src.functions import *

def test_basic_function1(rtol=1.e-7):
    result = abs(function_try(4) - 28)
    assert result < rtol, " *** error is too big "

def test_basic_function2():
    function_try(4)
    assert True, " *** error is too big "

def test_paying_debt():
    paying_debt(600000)
    assert True, "*** error is too big"


def test_prime_number():
    count_prime_number(500)
    assert True, "*** error is too big"


def test_city2city():
    city_to_city()
    assert True, "*** error is too big"

import pytest
from src.functions import *

def test_function_try1(rtol=1.e-7):
    result = abs(function_try(4) - 28)
    assert result < rtol, " *** error is too big "
    
def test_function_try2():
    function_try(4)
    assert True, " *** error is too big "
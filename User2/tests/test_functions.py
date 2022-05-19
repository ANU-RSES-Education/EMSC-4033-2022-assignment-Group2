import pytest
from src.functions import *

def test_foo_function(rtol=100):
    result = foo_function(5) - 16
    assert result < rtol, " *** error is too big "
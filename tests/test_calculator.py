import pytest
from src.calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(2,3) == 5

def test_sub():
    assert calc.subtract(6,3) == 3

def test_multiply():
    assert calc.multiply(2,3) == 6

def test_divide():
    assert calc.divide(8,2) == 4

def test_power():
    assert calc.power(2,3) == 8

@pytest.mark.parametrize('number, result', [
    (1, False),
    (2, True),
    (0, True),
    (-4, True),
    (-5, False)
])
def test_is_even(number, result):
    assert calc.is_even(number) == result

def test_add_raises_type_error():
    with pytest.raises(TypeError):
        calc.add(4, 'dfd')
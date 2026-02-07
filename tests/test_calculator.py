import pytest
from src.calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(2,3) == 5

def test_add_raises_type_error():
    with pytest.raises(TypeError):
        calc.add(4, 'dfd')
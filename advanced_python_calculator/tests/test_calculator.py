# tests/test_calculator.py

import pytest
from app.calculator import Calculator

@pytest.fixture
def calc():
    """Fixture to create a Calculator instance."""
    calculator = Calculator()
    return calculator

def test_add(calc):
    assert calc.add(1, 2) == 3

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12

def test_divide(calc):
    assert calc.divide(10, 2) == 5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(10, 0)

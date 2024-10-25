# tests/test_calculator.py
import pytest
from app.calculator import Calculator  # Ensure this import works correctly

def test_addition():
    assert Calculator.add(2, 3) == 5

def test_subtraction():
    assert Calculator.subtract(5, 2) == 3

def test_multiplication():
    assert Calculator.multiply(3, 4) == 12

def test_division():
    assert Calculator.divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)

# Add more tests as needed

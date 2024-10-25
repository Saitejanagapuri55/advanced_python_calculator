# tests/test_calculator.py

import pytest
from app.calculator import add, subtract, multiply, divide

def test_add_large_numbers():
    assert add(1e10, 1e10) == 2e10

def test_subtract_negative_result():
    assert subtract(2, 5) == -3

def test_multiply_large_numbers():
    assert multiply(1e10, 1e10) == 1e20

def test_divide_large_numbers():
    assert divide(1e10, 1e5) == 1e5

def test_divide_negative_numbers():
    assert divide(-10, 2) == -5

def test_divide_positive_by_negative():
    assert divide(10, -2) == -5

import pytest

from main import get_float_input, get_str_input, bess_calculator, check_time


# Mock input for testing purposes
def mock_input(prompt):
    return "10.0"


# Test the get_float_input function
def test_get_float_input(monkeypatch):
    monkeypatch.setattr("builtins.input", mock_input)
    assert get_float_input("Enter a float: ") == 10.0


# Mock input for testing purposes
def mock_input_time(prompt):
    return "12:30"


# Test the get_str_input function
def test_get_str_input(monkeypatch):
    monkeypatch.setattr("builtins.input", mock_input_time)
    assert get_str_input("Enter a time: ") == "12:30"


# Test the check_time function
def test_check_time():
    assert check_time("12:00", "13:00") == 1.0


def test_bess_calculator():
    results = bess_calculator(10.0, 5.0, 3600, "12:00", "13:00")
    assert isinstance(results, dict)
    assert all(isinstance(value, float) for value in results.values())

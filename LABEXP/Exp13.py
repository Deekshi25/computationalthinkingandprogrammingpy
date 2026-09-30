import pytest

from result import calculate_average, result


def test_average():
    assert calculate_average([80, 90, 70]) == 80


def test_pass():
    assert result([80, 90, 70]) == "PASS"


def test_fail():
    assert result([20, 30, 35]) == "FAIL"


def test_empty():
    with pytest.raises(ValueError):
        calculate_average([])


def test_invalid():
    with pytest.raises(ValueError):
        calculate_average([80, 110])

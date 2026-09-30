from collections.abc import Sequence


def calculate_result(marks: Sequence[float]) -> str:
    """Return PASS when average mark is at least 40."""

    if not marks:
        raise ValueError("Marks cannot be empty")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")

    average = sum(marks) / len(marks)

    return "PASS" if average >= 40 else "FAIL"



import pytest

from app import calculate_result


def test_pass():
    assert calculate_result([50, 60, 70]) == "PASS"


def test_fail():
    assert calculate_result([20, 30, 35]) == "FAIL"


def test_empty_marks():
    with pytest.raises(ValueError):
        calculate_result([])


def test_invalid_marks():
    with pytest.raises(ValueError):
        calculate_result([50, 110])

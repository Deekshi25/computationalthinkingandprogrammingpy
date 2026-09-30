from typing import Sequence


def calculate_total(marks: Sequence[int]) -> int:
    validate_marks(marks)
    return sum(marks)


def calculate_average(marks: Sequence[int]) -> float:
    validate_marks(marks)

    if not marks:
        raise ValueError("Marks cannot be empty")

    return sum(marks) / len(marks)


def calculate_grade(average: float) -> str:
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"

    return "F"


def validate_marks(marks: Sequence[int]) -> None:
    if not marks:
        raise ValueError("Marks cannot be empty")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")

import pytest

from grade import (
    calculate_total,
    calculate_average,
    calculate_grade
)


def test_total():
    assert calculate_total([80, 90, 70]) == 240


def test_average():
    assert calculate_average([80, 90, 70]) == 80


def test_grade():
    assert calculate_grade(80) == "B"


def test_invalid_marks():
    with pytest.raises(ValueError):
        calculate_average([110])

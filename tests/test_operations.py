import pytest
from app.operations import Operations

@pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 1, 2),
            (0, 0, 0),
            (2, -1, 1),
            (0, -1, -1),
            (-5, -5, -10)
        ],
        ids=[
            "add_two_positive_numbers",
            "add_zero_twice",
            "add_when_second_num_is_neg_and_res_is_pos",
            "add_when_second_num_is_net_and_res_is_neg",
            "add_two_negative_numbers"
        ]
)
def test_addition(a: float, b: float, expected: float) -> None:
    result = Operations.addition(a, b)
    assert result == expected, f"Expected {a} + {b} == {expected}. Got {result}."

@pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 1, 0),
            (5, 1, 4),
            (1, 0, 1),
            (-1, -1, 0),
            (0, 1, -1),
            (1, 5, -4),
            (-1, 5, -6)
        ],
        ids=[
            "subtract_equal_values",
            "subtract_first_is_greater",
            "subtract_zero_from",
            "subtract_two_negative_values",
            "subtract_from_zero",
            "subtract_first_is_lesser",
            "subtract_first_negative"
        ]
)
def test_subtraction(a: float, b: float, expected: float) -> None:
    result = Operations.subtraction(a, b)
    assert result == expected, f"Expected {a} - {b} == {expected}. Got {result}."

@pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 1, 1),
            (-5, -5, 25),
            (4, 0, 0),
            (5, -5, -25),
            (-7, 5, -35)
        ],
        ids=
        [
            "multiply_two_positive_values",
            "multiply_two_negative_values",
            "multiply_by_zero",
            "multiply_second_is_negative",
            "multiply_first_is_negative"
        ]
)
def test_multiplication(a: float, b: float, expected: float) -> None:
    result = Operations.multiplication(a, b)
    assert result == expected, f"Expected {a} * {b} == {expected}. Got {result}."

@pytest.mark.parametrize(
        "a, b, expected",
        [
            (5, 1, 5),
            (0, 5, 0),
            (6, -2, -3),
            (-6, 2, -3),
            (0, -7, 0)
        ],
        ids=
        [
            "divide_two_positive",
            "divide_zero_by_positive",
            "divide_positive_by_negative",
            "divide_negative_by_positive",
            "divide_zero_by_negative"
        ]
)
def test_valid_division(a: float, b: float, expected: float) -> None:
    result = Operations.division(a, b)
    assert result == expected, f"Expected {a} / {b} == {expected}. Got {result}."

@pytest.mark.parametrize(
        "a, b",
        [
            (1, 0),
            (-1, 0),
            (0, 0)
        ],
        ids=
        [
            "divide_positive_by_zero",
            "divide_negative_by_zero",
            "divide_zero_by_zero"
        ]
)
def invalid_division(a: float, b: float) -> None:
    with pytest.raises(ZeroDivisionError, match="Error: b cannot be 0."):
        assert Operations.division(a, b)
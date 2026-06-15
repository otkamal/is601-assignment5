import pytest
from app.calculation import Calculation, CalculationFactory

@pytest.mark.parametrize(
    "op, a, b, expected",
    [
        ("add", 5, 10, 15),
        ("subtract", 17, 7, 10),
        ("divide", 10, 2, 5),
        ("multiply", 3, 3, 9),
        ("power", 5, 2, 25),
        ("ADD", 4, 2, 6),
    ],
    ids=[
        "factory_add",
        "factory_subtract",
        "factory_divide",
        "factory_multiply",
        "factory_power",
        "factory_add_case_insensitive",
    ]
)
def test_factory_build_and_execute(op: str, a: float, b: float, expected: float) -> None:
    calculation = CalculationFactory.build_calculation(op, a, b)
    result = calculation.execute()
    assert result == expected, f"Expected {op}({a}, {b}) = {expected}. Got {result}."

@pytest.mark.parametrize(
    "op, a, b, expected",
    [
        ("add", 5, 10, "Addition(a = 5, b = 10)"),
        ("subtract", 5, 10, "Subtraction(a = 5, b = 10)"),
        ("multiply", 5, 10, "Multiplication(a = 5, b = 10)"),
        ("divide", 5, 10, "Division(a = 5, b = 10)"),
        ("power", 5, 2, "Power(a = 5, b = 2)")
    ],
    ids=
    [
        "string_add",
        "string_subtract",
        "string_multiply",
        "string_divide",
        "string_power"
    ]
)
def test_calculation_string(op: str, a: float, b: float, expected: str) -> None:
    calculation = CalculationFactory.build_calculation(op, a, b)
    assert str(calculation) == expected, f"Expected {op}({a}, {b}) = {expected}. Got {str(calculation)}."

@pytest.mark.parametrize(
    "op, a, b, expected",
    [
        ("add", 5, 10, "Addition: operand_a = 5, operand_b = 10"),
        ("subtract", 5, 10, "Subtraction: operand_a = 5, operand_b = 10"),
        ("multiply", 5, 10, "Multiplication: operand_a = 5, operand_b = 10"),
        ("divide", 5, 10, "Division: operand_a = 5, operand_b = 10"),
        ("power", 5, 10, "Power: operand_a = 5, operand_b = 10"),
    ],
    ids=[
        "repr_add",
        "repr_subtract",
        "repr_multiply",
        "repr_divide",
        "repr_power"
    ]
)
def test_calculation_repr(op: str, a: float, b: float, expected: str) -> None:
    calculation = CalculationFactory.build_calculation(op, a, b)
    assert repr(calculation) == expected, f"Expected {op}({a}, {b}) = {expected}. Got {repr(calculation)}."

def test_duplicate_registration() -> None:
    with pytest.raises(ValueError, match="add is already registered."):
        @CalculationFactory.register_calculation('add')
        class Adddition(Calculation):
            def execute(self) -> float:
                return 0

def test_unsupported_operation() -> None:
    with pytest.raises(ValueError, match="is not a supported operation."):
        CalculationFactory.build_calculation("percent", 5, 100)

def test_faactory_division_by_zero() -> None:
    with pytest.raises(ZeroDivisionError, match="Error: b cannot be 0."):
        CalculationFactory.build_calculation("divide", 10, 0).execute()
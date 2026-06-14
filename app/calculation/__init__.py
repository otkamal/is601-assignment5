from abc import ABC, abstractmethod
from app.operations import Operations


class Calculation(ABC):

    """
    Abstract base class representing a calculation with two operands.

    All subclasses must implement the execute method, which performs
    the calculation and returns a float result.

    Methods:
        execute(): Performs the calculation and returns the result.
    """

    def __init__(self, a: float, b: float):
        """
        Initializes the calculation with two operands.

        Args:
            a: The first operand.
            b: The second operand.
        """
        self.operand_a = a
        self.operand_b = b

    @abstractmethod
    def execute(self) -> float:
        """
        Executes the calculation and returns the result.

        Returns:
            The result of the calculation as a float.
        """

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the calculation.

        Returns:
            A string in the format ClassName(operand_a, operand_b).
        """
        return f"{self.__class__.__name__}(a = {self.operand_a}, b = {self.operand_b})"

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the calculation for debugging.

        Returns:
            A string in the format ClassName: operand_a = a, operand_b = b.
        """
        return f"{self.__class__.__name__}: operand_a = {self.operand_a}, operand_b = {self.operand_b}"
    
class CalculationFactory:

    """
    Factory for registering and instantiating Calculation subclasses.

    Subclasses are registered via the register_calculation decorator and
    retrieved by name through build_calculation.

    Methods:
        register_calculation(calc): Decorator to register a Calculation subclass.
        build_calculation(calc, a, b): Instantiates a registered Calculation by name.
    """

    _calculations = {}

    @classmethod
    def register_calculation(cls, calc: str):
        """
        Decorator that registers a Calculation subclass under the given name.

        Args:
            calc: The operation name to register (case-insensitive).

        Returns:
            A decorator that registers the decorated class and returns it unchanged.

        Raises:
            ValueError: If the operation name is already registered.
        """
        def registration_decorator(subclass):
            calc_sanitized = calc.lower()
            if calc_sanitized in cls._calculations:
                raise ValueError(f"{calc_sanitized} is already registered.")
            cls._calculations[calc_sanitized] = subclass
            return subclass
        return registration_decorator

    @classmethod
    def build_calculation(cls, calc: str, a: float, b: float) -> Calculation:
        """
        Instantiates a registered Calculation by name.

        Args:
            calc: The operation name (case-insensitive).
            a: The first operand.
            b: The second operand.

        Returns:
            A Calculation instance ready to be executed.

        Raises:
            ValueError: If the operation name is not registered.
        """
        calc_sanitized = calc.lower()
        if calc_sanitized not in cls._calculations:
            raise ValueError(f'"{calc_sanitized}" is not a supported operation.')
        new_calculation = cls._calculations.get(calc_sanitized)
        return new_calculation(a, b)


@CalculationFactory.register_calculation('add')
class Addition(Calculation):

    """
    Calculation that adds two operands.

    Methods:
        execute(): Returns the sum of operand_a and operand_b.
    """

    def execute(self) -> float:
        """
        Adds the two operands.

        Returns:
            The sum of operand_a and operand_b.
        """
        return Operations.addition(self.operand_a, self.operand_b)


@CalculationFactory.register_calculation('subtract')
class Subtraction(Calculation):

    """
    Calculation that subtracts the second operand from the first.

    Methods:
        execute(): Returns the difference of operand_a and operand_b.
    """

    def execute(self) -> float:
        """
        Subtracts operand_b from operand_a.

        Returns:
            The difference of operand_a and operand_b.
        """
        return Operations.subtraction(self.operand_a, self.operand_b)


@CalculationFactory.register_calculation('multiply')
class Multiplication(Calculation):

    """
    Calculation that multiplies two operands.

    Methods:
        execute(): Returns the product of operand_a and operand_b.
    """

    def execute(self) -> float:
        """
        Multiplies the two operands.

        Returns:
            The product of operand_a and operand_b.
        """
        return Operations.multiplication(self.operand_a, self.operand_b)


@CalculationFactory.register_calculation('divide')
class Division(Calculation):

    """
    Calculation that divides the first operand by the second.

    Methods:
        execute(): Returns the quotient of operand_a and operand_b.
    """

    def execute(self) -> float:
        """
        Divides operand_a by operand_b.

        Returns:
            The quotient of operand_a and operand_b.

        Raises:
            ZeroDivisionError: If operand_b is zero.
        """
        return Operations.division(self.operand_a, self.operand_b)

class Operations():

    """
    A collection of basic arithmetic operations.

    All methods are static and operate on two floats,
    returning a float result.

    Methods:
        addition(a, b): Returns the sum of a and b.
        subtraction(a, b): Returns the difference of a and b.
        multiplication(a, b): Returns the product of a and b.
        division(a, b): Returns the quotient of a and b.
    """

    @staticmethod
    def addition(a: float, b: float) -> float:
        """
        Adds two numbers together.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The sum of a and b.
        """
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """
        Subtracts b from a.

        Args:
            a: The number to subtract from.
            b: The number to subtract.

        Returns:
            The difference of a and b.
        """
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """
        Multiplies two numbers together.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The product of a and b.
        """
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        """
        Divides a by b.

        Args:
            a: The dividend.
            b: The divisor.

        Returns:
            The quotient of a and b.

        Raises:
            ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Error: b cannot be 0.")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        return a ** b
    
    @staticmethod
    def modulus(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Error: b cannot be 0.")
        return a % b
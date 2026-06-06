from app.operations import Operations


def calculator() -> None:
    """
    Runs an interactive calculator REPL (Read-Eval-Print Loop).

    Prompts the user to enter an operation and two numbers in the format
    <operation> <a> <b>, computes the result, and prints it. Continues
    until the user types 'exit'.

    Supported operations:
        - add: Adds a and b.
        - subtract: Subtracts b from a.
        - multiply: Multiplies a and b.
        - divide: Divides a by b.

    Raises:
        ZeroDivisionError: If divide is used and b is zero (handled internally).
        ValueError: If the input format is invalid (handled internally).

    Example:
        >>> calculator()
        Enter an operation and two numbers, or 'exit' to quit: add 5 3
        Result: 8.0
    """
    print("Welcome to the calculator REPL. Type 'exit' to quit.")
    while True:
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ")
        user_input = user_input.lower()
        if user_input == "exit":
            print("Exiting calculator... Goodbye ~")
            break

        try:
            operation, a, b = user_input.split()
            a, b = float(a), float(b)
        except ValueError:
            print("Invalid input. Please follow <operation> <a> <b> syntax.")
            continue

        if operation == "add":
            result = Operations.addition(a, b)
        elif operation == "subtract":
            result = Operations.subtraction(a, b)
        elif operation == "multiply":
            result = Operations.multiplication(a, b)
        elif operation == "divide":
            try:
                result = Operations.division(a, b)
            except ZeroDivisionError as e:
                print(e)
                continue
        else:
            print(f"Unknown operation {operation}. Supported operations: add, subtract, multiply, divide.")
            continue

        print(f"Result: {result}")
        
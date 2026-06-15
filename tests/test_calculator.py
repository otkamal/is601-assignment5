from app.calculator import calculator

def run_calculator_with_input(monkeypatch, capsys, inputs):
    """
    Helper function to run the calculator with simulated user inputs.

    Patches builtins.input with a iterator over the provided inputs,
    runs the calculator, and returns the captured stdout output.

    Args:
        monkeypatch: The pytest monkeypatch fixture for patching builtins.input.
        capsys: The pytest capsys fixture for capturing stdout.
        inputs: A list of strings simulating user inputs. Should always
                end with 'exit' to terminate the calculator loop.

    Returns:
        The captured stdout output as a string.
    """
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))
    calculator()
    return capsys.readouterr().out

def test_addition(monkeypatch, capsys):
    """Tests addition operation in REPL."""
    input = ["add 5 5", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, input)
    assert "Result: 10.0" in output

def test_subtraction(monkeypatch, capsys):
    """Tests subtraction operation in REPL."""
    input = ["subtract 3 2", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, input)
    assert "Result: 1.0" in output

def test_multiplication(monkeypatch, capsys):
    """Tests multiplication operation in REPL."""
    input = ["multiply 4 -3", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, input)
    assert "Result: -12.0" in output

def test_division(monkeypatch, capsys):
    """Tests division operation in REPL."""
    input = ["divide 84 7", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, input)
    assert "Result: 12.0" in output

def test_division_by_zero(monkeypatch, capsys):
    """Tests division by 0 in REPL."""
    input = ["divide 100 0", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, input)
    assert "Error: b cannot be 0." in output

def test_invalid_operation(monkeypatch, capsys):
    """Tests supported operations check in REPL."""
    input = ["modulo 5 2", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, input)
    assert "\"modulo\" is not a supported operation." in output

def test_invalid_values(monkeypatch, capsys):
    """Tests valid input values in REPL."""
    input = ["add 1 flimflam", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, input)
    assert "Invalid input. Please follow <operation> <a> <b> syntax." in output

def test_exit(monkeypatch, capsys):
    """ Tests quits on 'exit' in REPL. """
    input = ["exit"]
    output = run_calculator_with_input(monkeypatch, capsys, input)
    assert "Exiting calculator... Goodbye ~" in output

def test_help(monkeypatch, capsys):
    """ Tests operation list on 'help' in REPL. """
    input = ["help", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, input)
    assert "Supported operations: " in output
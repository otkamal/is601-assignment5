# Module 3 - Calculator REPL with OOP Refactor

A command-line calculator REPL built in Python, refactored to use an `Operations` class with static methods and parameterized tests.

## What Changed in Module 3

- Arithmetic logic moved into an `Operations` class (`app/operations/`)
- Calculator REPL updated to call `Operations` static methods
- Tests refactored to use `pytest.mark.parametrize`
- Added basic linting in Github Action workflow

## Project Structure

```
mod3_assignment/
├── .github/
│   └── workflows
│       └── tests.yml
├── app/
│   ├── __init__.py
│   ├── calculator/
│   │   └── __init__.py
│   └── operations/
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_operations.py
├── main.py
├── .coveragerc
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

```
Welcome to the calculator REPL. Type 'exit' to quit.
Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: multiply 6 7
Result: 42.0
Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: exit
Exiting calculator... Goodbye ~
```

## Supported Operations

| Operation  | Example              |
|------------|----------------------|
| add        | `add 5 3`            |
| subtract   | `subtract 10 4`      |
| multiply   | `multiply 3 4`       |
| divide     | `divide 10 2`        |
| exit       | quit the application |

## Running Tests

```bash
pytest --cov=app --cov-fail-under=100
```

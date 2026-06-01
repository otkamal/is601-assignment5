# Module 2 - Basic Calculator REPL

A simple command-line calculator REPL built in Python.

## Features

- Addition, subtraction, multiplication, and division
- Interactive REPL loop
- Input validation and error handling

## Project Structure

```
mod2_assignment/
├── .github/
│   └── workflows
│       └── tests.yml
├── app/
│   ├── __init__.py
│   └── operations
│       └── __init__.py
│   └── calculator
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_operations.py
│   └── test_calculator.py
├── main.py
├── .coveragerc
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

## Setup

It is recommended to configure a virtual environment before installing dependencies.

```bash
# optionally configure a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

```
Welcome to the calculator REPL. Type 'exit' to quit.
Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: add 5 3
Result: 8.0
Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: exit
Exiting calculator... Goodbye ~
```

## Supported Operations

| Operation  | Example          |
|------------|------------------|
| add        | `add 5 3`        |
| subtract   | `subtract 10 4`  |
| multiply   | `multiply 3 4`   |
| divide     | `divide 10 2`    |
| exit       | `quit application` |

## Running Tests

```bash
pytest --cov=app --cov-fail-under=100
```

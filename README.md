# Module 4 - Calculator REPL with Factory Pattern

A command-line calculator REPL built in Python, refactored to use an abstract base class, a factory pattern, and a calculation history.

## What Changed in Module 4

- Introduced `Calculation` abstract base class (`app/calculation/`) with `__str__` and `__repr__`
- Added `CalculationFactory` with decorator-based registration for extensible operation support
- Added `Power` and `Modulus` operations to both `Operations` and `CalculationFactory`
- Calculator REPL updated to use `CalculationFactory` and track calculation history
- Added `help` command to list supported operations dynamically
- Added `history` command to display previously executed calculations
- Added launch screen using `pyfiglet`
- Added `test_calculation.py` with 100% coverage across all modules

## Project Structure

```
mod4_assignment/
├── .github/
│   └── workflows
│       └── tests.yml
├── app/
│   ├── __init__.py
│   ├── calculation/
│   │   └── __init__.py
│   ├── calculator/
│   │   └── __init__.py
│   └── operations/
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── test_calculation.py
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
 ____      _      __     ____   ____    _____   ____
/ ___|__ _| | ___|  _ \ | __ ) | __ ) | ____| |  _ \
| |   / _` | |/ __| |_) ||  _ \ |  _ \ |  _|   | |_) |
| |__| (_| | | (__|  _ < | |_) || |_) || |___  |  __/
\____\__,_|_|\___|_| \_\|____/ |____/ |_____| |_|

Type 'exit' to quit.
Enter an operation and two numbers, or 'exit' to quit.
Enter 'help' to see available operations or 'history' to see previously ran operations.
>>> add 5 3
Result: 8.0
>>> history
- Addition(a = 5.0, b = 3.0) = 8.0
>>> exit
Exiting calculator... Goodbye ~
```

## Supported Operations

| Operation  | Example                  |
|------------|--------------------------|
| add        | `add 5 3`                |
| subtract   | `subtract 10 4`          |
| multiply   | `multiply 3 4`           |
| divide     | `divide 10 2`            |
| power      | `power 2 8`              |
| modulus    | `modulus 10 3`           |
| help       | list available operations |
| history    | show previous calculations |
| exit       | quit the application     |

## Running Tests

```bash
pytest --cov=app --cov-fail-under=100
```

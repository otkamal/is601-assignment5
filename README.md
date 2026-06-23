# Module 5 - Calculator with Memento, Observer, and Singleton Config

A command-line calculator REPL built in Python, extended with undo/redo via the Memento pattern, event-driven auto-save via the Observer pattern, and centralized environment-based configuration via a Singleton.

## What Changed in Module 5

- Added `CalculatorMemento` to snapshot calculator history, enabling undo and redo
- Added `undo` and `redo` commands to the REPL
- Added Observer pattern with `Subscriber` base class, `CalculationSubscriber` (logs each result), and `AutoSaveSubscriber` (persists history on shutdown)
- Added `CalculatorConfig` singleton that reads all settings from environment variables with sensible defaults
- Added `save`, `load`, and `clear` commands to the REPL
- Added `.env` support via `python-dotenv` for configuring history size, auto-save, precision, and more
- Added `test_memento.py`, `test_observer.py`, `test_calculator_config.py`, and `test_repl.py`

## Project Structure

```
mod5_assignment/
├── .github/
│   └── workflows/
│       └── tests.yml
├── app/
│   ├── __init__.py
│   ├── calculation.py       # Calculation ABC, CalculationFactory, operation subclasses
│   ├── calculator.py        # Calculator with history, undo/redo, and observer support
│   ├── calculator_config.py # Singleton config loaded from environment variables
│   ├── memento.py           # CalculatorMemento for undo/redo snapshots
│   ├── observer.py          # Subscriber base class, CalculationSubscriber, AutoSaveSubscriber
│   ├── operations.py        # Static arithmetic operations
│   └── repl.py              # Interactive REPL
├── tests/
│   ├── test_calculation.py
│   ├── test_calculator.py
│   ├── test_calculator_config.py
│   ├── test_memento.py
│   ├── test_observer.py
│   ├── test_operations.py
│   └── test_repl.py
├── main.py
├── .env
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

## Configuration

Settings are read from environment variables at startup. Copy the values below into a `.env` file and adjust as needed.

| Variable                    | Default          | Description                                      |
|-----------------------------|------------------|--------------------------------------------------|
| `CALCULATOR_BASE_DIR`       | project root     | Base directory for logs and history              |
| `CALCULATOR_MAX_HISTORY_SIZE` | `100`          | Maximum number of calculations kept in memory    |
| `CALCULATOR_AUTO_SAVE`      | `true`           | Persist history to disk on shutdown              |
| `CALCULATOR_PRECISION`      | `5`              | Decimal places used in calculations              |
| `CALCULATOR_MAX_INPUT_VALUE`| `1000`           | Maximum allowed input value                      |
| `CALCULATOR_DEFAULT_ENCODING` | `utf-8`        | File encoding for history and log files          |

Example `.env`:

```
CALCULATOR_BASE_DIR='.'
CALCULATOR_MAX_HISTORY_SIZE='100'
CALCULATOR_AUTO_SAVE='true'
CALCULATOR_PRECISION='9'
CALCULATOR_MAX_INPUT_VALUE='1000'
CALCULATOR_DEFAULT_ENCODING='utf-8'
```

## Usage

```bash
python main.py
```

```
   ______      __           __      __                ____  __________  __ 
  / ____/___ _/ /______  __/ /___ _/ /_____  _____   / __ \/ ____/ __ \/ / 
 / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/  / /_/ / __/ / /_/ / /  
/ /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /     / _, _/ /___/ ____/ /___
\____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     /_/ |_/_____/_/   /_____/

Type 'exit' to quit.
Enter an operation and two numbers, or 'exit' to quit.
Enter 'help' to see available operations or 'history' to see previously ran operations.
>>> add 5 3
Result: 8.0
>>> subtract 10 4
Result: 6.0
>>> history
1. Addition(a = 5.0, b = 3.0, result = 8.0)
2. Subtraction(a = 10.0, b = 4.0, result = 6.0)
>>> undo
History has been undone.
>>> redo
History has been redone.
>>> save
History saved to disk.
>>> exit
Exiting calculator... Goodbye ~
```

## Commands

| Command              | Description                                          |
|----------------------|------------------------------------------------------|
| `<op> <a> <b>`       | Perform a calculation, e.g. `add 5 3`                |
| `history`            | Display all calculations in the current session      |
| `undo`               | Revert the last calculation                          |
| `redo`               | Re-apply the last undone calculation                 |
| `save`               | Persist the current history to disk                  |
| `load`               | Reload history from disk, replacing in-memory state  |
| `clear`              | Clear in-memory history without touching the file    |
| `help`               | List all commands and supported operations           |
| `exit`               | Shut down the REPL                                   |

## Supported Operations

| Operation | Example          |
|-----------|------------------|
| `add`     | `add 5 3`        |
| `subtract`| `subtract 10 4`  |
| `multiply`| `multiply 3 4`   |
| `divide`  | `divide 10 2`    |
| `power`   | `power 2 8`      |
| `modulus` | `modulus 10 3`   |

## Running Tests

```bash
pytest --cov=app --cov-report=term-missing --cov-fail-under=100
```

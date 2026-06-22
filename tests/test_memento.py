import datetime
import pytest
import os
from unittest.mock import patch
from app.calculator import Calculator
from app.memento import CalculatorMemento
from app.calculator_config import CalculatorConfig

@pytest.fixture(autouse=True)
def reset_singleton():
    CalculatorConfig._instance = None
    yield
    CalculatorConfig._instance = None

@pytest.fixture(autouse=True)
def config(tmp_path, reset_singleton):
    (tmp_path / "logs").mkdir()
    (tmp_path / "history").mkdir()
    with patch.dict(os.environ, {
        'CALCULATOR_AUTO_SAVE': 'false',
        'CALCULATOR_BASE_DIR': str(tmp_path),
        'CALCULATOR_LOG_DIR': str(tmp_path / "logs"),
        'CALCULATOR_HIST_DIR': str(tmp_path / "history"),
        'CALCULATOR_HISTORY_FILE': str(tmp_path / "history"/ "history.csv"),
        "CALCULATOR_LOG_FILE": str(tmp_path / "logs" / "calculator.log")
    }):
        yield CalculatorConfig()

@pytest.fixture
def calculator(config):
    return Calculator(config)

def test_memento_get_history(calculator):
    calculator.calculate('add', 1, 1)
    calculator.calculate('subtract', 1, 2)
    print(calculator.get_history())
    cm = CalculatorMemento(calculator)
    assert len(cm.get_history()) == 2

def test_memento_get_timestamp(calculator):
    before = datetime.datetime.now()
    cm = CalculatorMemento(calculator)
    after = datetime.datetime.now()
    ts = cm.get_timestamp()
    assert isinstance(ts, datetime.datetime)
    assert before <= ts <= after

def test_memento_is_snapshot(calculator):
    calculator.calculate('add', 1, 1)
    cm = CalculatorMemento(calculator)
    calculator.calculate('subtract', 1, 1)
    assert len(cm.get_history()) == 1
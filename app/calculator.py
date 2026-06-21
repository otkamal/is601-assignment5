import logging
from app.calculation import Calculation, CalculationFactory
from app.calculator_config import CalculatorConfig

class Calculator():

    def __init__(self, config: CalculatorConfig):
        self.config = CalculatorConfig() \
            if config is None else config
    
        self._history: list[tuple[Calculation, float]] = []
        self._LOG_FILE = "calculator.log"
        self._init_logging()
        self._log_config()

    def calculate(self, calc: Calculation):
        result = calc.execute()
        if len(self._history) > self.config.history_size:
            self._history.pop()
        self._history.append((calc, result))
        return result

    def _init_logging(self):
        logging.basicConfig(
            filename=self.config.log_file,
            encoding=self.config.encoding,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info(f"logging initialized at {self.config.log_file}")

    def _log_config(self):
        logging.info(f"history size set to {self.config.history_size}")
        logging.info(f"precision set to {self.config.precision}")
        logging.info(f"encoding set to {self.config.encoding}")
        logging.info(f"max value set to {self.config.max_value}")
        logging.info(f"auto-save set to {self.config.auto_save}")
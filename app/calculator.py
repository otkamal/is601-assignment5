import logging
from app.calculation import Calculation, CalculationFactory
from app.observer import Subscriber, CalculationSubscriber, AutoSaveSubscriber
from app.calculator_config import CalculatorConfig

class Calculator():

    def __init__(self, config: CalculatorConfig = None):
        self.config = CalculatorConfig() \
            if config is None else config
    
        self._history: list[Calculation] = []
        self._subscribers: list[Subscriber] = []
        self._init_logging()
        self._init_history()
        self._log_config()
        self._add_subscriber(CalculationSubscriber())
        self._add_subscriber(AutoSaveSubscriber())

    def calculate(self, calc: Calculation):
        calc.execute()
        if len(self._history) == self.config.history_size:
            logging.info(
                f"max history size hit -> removing {self._history.pop(0)}"
        )
        self._history.append(calc)
        self.update_subscribers()
        return calc.result

    def _init_logging(self) -> None:
        logging.basicConfig(
            filename=self.config.log_file,
            encoding=self.config.encoding,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info(f"logging initialized at {self.config.log_file}")

    def _init_history(self) -> None:
        if self.config.history_file.exists():
            self._load_history()
        elif self.config.auto_save:
            self.config.history_file.touch()

    def _log_config(self) -> None:
        logging.info(f"history size set to {self.config.history_size}")
        logging.info(f"precision set to {self.config.precision}")
        logging.info(f"encoding set to {self.config.encoding}")
        logging.info(f"max value set to {self.config.max_value}")
        logging.info(f"auto-save set to {self.config.auto_save}")

    def _add_subscriber(self, sub: Subscriber) -> list[Subscriber]:
        logging.info(f"adding {sub.__class__.__name__}")
        self._subscribers.append(sub)
        return self._subscribers

    def _load_history(self) -> None:
        pass

    def get_last_calculation(self) -> Calculation:
        return self._history[-1] if len(self._history) > 0 else None
    
    def update_subscribers(self):
        logging.info(f"notifying {len(self._subscribers)} subscribers")
        for sub in self._subscribers:
            sub.update(self)

    def show_history(self) -> None:
        pass

    def save_history(self) -> None:
        logging.info(f"saved {len(self._history)} calculatons to disk")

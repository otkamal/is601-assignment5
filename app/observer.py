import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.calculator import Calculator

class Subscriber(ABC):
    @abstractmethod
    def update(self, calculator: Calculator):
        pass

    def update_on_shutdown(self, calculator: Calculator):
        pass

class CalculationSubscriber(Subscriber):
    def update(self, calculator: Calculator):
        c = calculator.get_last_calculation()
        if c is not None:
            logging.info(
                f"calculation performed -> {c}"
            )

    def update_on_shutdown(self, calculator):
        pass

class AutoSaveSubscriber(Subscriber):
    def update(self, calculator: Calculator):
        pass

    def update_on_shutdown(self, calculator):
        calculator.save_history()

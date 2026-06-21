from dotenv import load_dotenv
from app.calculator import Calculator
from app.calculator_config import CalculatorConfig
from app.repl import start_repl

if __name__ == "__main__":
    load_dotenv()
    config = CalculatorConfig()
    config.setup_directories()
    calculator = Calculator(config)
    start_repl(calculator)

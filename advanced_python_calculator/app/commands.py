# app/commands.py

from app.calculator import Calculator
from app.history_manager import HistoryManager

class CommandManager:
    def __init__(self):
        self.calculator = Calculator()
        self.history_manager = HistoryManager()

    def execute(self, operation, num1, num2):
        if operation == "add":
            result = self.calculator.add(num1, num2)
        elif operation == "subtract":
            result = self.calculator.subtract(num1, num2)
        elif operation == "multiply":
            result = self.calculator.multiply(num1, num2)
        elif operation == "divide":
            result = self.calculator.divide(num1, num2)
        else:
            raise ValueError(f"Unknown operation: {operation}")

        # Log the operation in history
        self.history_manager.add_to_history(operation, num1, num2, result)
        return result

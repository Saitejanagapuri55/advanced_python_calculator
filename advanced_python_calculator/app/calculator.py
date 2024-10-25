# app/calculator.py

from app.history_manager import HistoryManager

class Calculator:
    def __init__(self):
        super().__init__()
        self.history_manager = HistoryManager()
        self.history_manager.load_history()  # Load history on initialization

    def add(self, a, b):
        result = a + b
        self.history_manager.add_to_history(f"Add: {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history_manager.add_to_history(f"Subtract: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history_manager.add_to_history(f"Multiply: {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.history_manager.add_to_history(f"Divide: {a} / {b} = {result}")
        return result

# app/plugins/subtract_plugin.py

from app.calculator import Calculator

class SubtractPlugin:
    def execute(self, num1, num2):
        calculator = Calculator()
        return calculator.subtract(num1, num2)

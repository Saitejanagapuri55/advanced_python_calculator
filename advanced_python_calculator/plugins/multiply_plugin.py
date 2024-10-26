# app/plugins/multiply_plugin.py

from app.calculator import Calculator

class MultiplyPlugin:
    def execute(self, num1, num2):
        calculator = Calculator()
        return calculator.multiply(num1, num2)

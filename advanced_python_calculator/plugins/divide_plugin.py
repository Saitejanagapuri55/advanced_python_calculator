# app/plugins/divide_plugin.py

from app.calculator import Calculator

class DividePlugin:
    def execute(self, num1, num2):
        calculator = Calculator()
        return calculator.divide(num1, num2)

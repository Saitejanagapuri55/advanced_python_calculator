# app/plugins/add_plugin.py

from app.calculator import Calculator

class AddPlugin:
    def execute(self, num1, num2):
        calculator = Calculator()
        return calculator.add(num1, num2)

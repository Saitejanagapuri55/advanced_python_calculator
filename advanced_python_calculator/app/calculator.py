# app/calculator.py

import argparse
from app.history_manager import log_operation

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def add(self, a, b):
        result = a + b
        log_operation('add', a, b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        log_operation('subtract', a, b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        log_operation('multiply', a, b, result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        log_operation('divide', a, b, result)
        return result

def main():
    parser = argparse.ArgumentParser(description='Simple Calculator')
    parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'],
                        help='The operation to perform')
    parser.add_argument('a', type=float, help='First operand')
    parser.add_argument('b', type=float, help='Second operand')

    args = parser.parse_args()

    calc = Calculator()
    result = None

    if args.operation == 'add':
        result = calc.add(args.a, args.b)
    elif args.operation == 'subtract':
        result = calc.subtract(args.a, args.b)
    elif args.operation == 'multiply':
        result = calc.multiply(args.a, args.b)
    elif args.operation == 'divide':
        result = calc.divide(args.a, args.b)

    print(f'The result of {args.operation} {args.a} and {args.b} is: {result}')

if __name__ == '__main__':
    main()

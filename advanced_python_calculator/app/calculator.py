# app/calculator.py

from app.history_manager import log_operation

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    print("Welcome to the Calculator!")
    while True:
        try:
            operation = input("Enter operation (add, subtract, multiply, divide) or 'quit' to exit: ")
            if operation == 'quit':
                break
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if operation == 'add':
                result = add(a, b)
            elif operation == 'subtract':
                result = subtract(a, b)
            elif operation == 'multiply':
                result = multiply(a, b)
            elif operation == 'divide':
                result = divide(a, b)
            else:
                print("Invalid operation.")
                continue

            print(f"Result: {result}")
            # Log the operation
            log_operation(operation, a, b, result)

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

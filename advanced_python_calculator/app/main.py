import sys
from app.history_manager import HistoryManager

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 -m app.main <operation> <num1> <num2>")
        return

    operation = sys.argv[1]
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Num1 and Num2 must be numbers.")
        return

    # Initialize the History Manager
    history_manager = HistoryManager()

    # Perform the operation
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Unknown operation. Supported operations: add, subtract, multiply, divide.")
        return

    print(f"Result: {result}")

    # Add to history
    history_manager.add_to_history(operation, num1, num2, result)

    # Print the current history
    print("Current History:")
    print(history_manager.get_history().to_string(index=False))

if __name__ == "__main__":
    main()

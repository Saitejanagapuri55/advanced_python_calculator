# app/history_manager.py

def log_operation(operation: str, a: float, b: float, result: float):
    with open("history.txt", "a") as f:
        f.write(f"{operation}: {a} and {b} = {result}\n")

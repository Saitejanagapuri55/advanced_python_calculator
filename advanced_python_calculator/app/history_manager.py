# app/history_manager.py

import os

# Define a log file path
LOG_FILE_PATH = 'operation_history.txt'

def log_operation(operation: str, a: float, b: float, result: float):
    """Logs the operation details into a file."""
    with open(LOG_FILE_PATH, 'a') as f:
        f.write(f"{operation}: {a}, {b} = {result}\n")

def get_history():
    """Reads the operation history from the log file."""
    if os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, 'r') as f:
            return f.readlines()
    return []

# app/history_manager.py

class HistoryManager:
    def __init__(self):
        self.history = []

    def load_history(self):
        """Load history from a file."""
        try:
            with open("history.txt", "r") as file:
                self.history = file.readlines()
        except FileNotFoundError:
            self.history = []  # Start with an empty history if the file doesn't exist

    def add_to_history(self, operation):
        """Add an operation to history."""
        self.history.append(operation)
        with open("history.txt", "a") as file:
            file.write(operation + "\n")

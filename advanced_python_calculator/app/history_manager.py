import pandas as pd
import os

class HistoryManager:
    def __init__(self):
        self.history_file = "history.txt"  # Define the history file path
        # Load existing history from the file if it exists
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file, sep=",")
        else:
            # Initialize the history DataFrame with appropriate column names
            self.history = pd.DataFrame(columns=["Operation", "Num1", "Num2", "Result"])

    def add_to_history(self, operation, num1, num2, result):
        # Create a new record for the operation
        new_record = pd.DataFrame({
            "Operation": [operation],
            "Num1": [num1],
            "Num2": [num2],
            "Result": [result]
        })

        # Drop any all-NA columns in the new record
        new_record = new_record.dropna(axis=1, how='all')

        # Append the new record to the history DataFrame
        self.history = pd.concat([self.history, new_record], ignore_index=True)

        # Write the updated history to the history.txt file
        self.write_to_file()

    def get_history(self):
        return self.history

    def write_to_file(self):
        # Save the history DataFrame to a text file without index and without header duplication
        self.history.to_csv(self.history_file, index=False, header=True)

# Example of how to use the HistoryManager
if __name__ == "__main__":
    manager = HistoryManager()
    manager.add_to_history("add", 2, 3, 5)
    manager.add_to_history("multiply", 6, 5, 30)
    print(manager.get_history())

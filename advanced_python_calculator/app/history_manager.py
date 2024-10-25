# app/history_manager.py

"""
This module manages the history of calculations performed by the calculator.
"""

import os
import json

class HistoryManager:
    """
    A class to manage the history of calculations.
    """

    def __init__(self, history_file='history.json'):
        """
        Initialize the HistoryManager with a specified history file.

        Parameters:
        history_file (str): The path to the history file.
        """
        self.history_file = history_file
        self.history = self.load_history()

    def load_history(self):
        """
        Load the calculation history from a file.

        Returns:
        list: A list of calculation history entries.
        """
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    def save_history(self):
        """
        Save the current calculation history to a file.
        """
        with open(self.history_file, 'w', encoding='utf-8') as file:
            json.dump(self.history, file)

    def add_entry(self, entry):
        """
        Add a new entry to the calculation history.

        Parameters:
        entry (dict): The entry to add to the history.
        """
        self.history.append(entry)
        self.save_history()

    def clear_history(self):
        """
        Clear the calculation history.
        """
        self.history = []
        self.save_history()

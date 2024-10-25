# tests/test_history_manager.py
import pytest
from app.history_manager import HistoryManager  # Ensure this is the correct class

def test_add_entry():
    history_manager = HistoryManager()
    history_manager.add_entry("2 + 2 = 4")
    assert history_manager.get_history() == ["2 + 2 = 4"]

def test_clear_history():
    history_manager = HistoryManager()
    history_manager.add_entry("2 + 2 = 4")
    history_manager.clear_history()
    assert history_manager.get_history() == []

# tests/test_logger.py
import pytest
from app.logger import Logger  # Ensure this is the correct class

def test_logger():
    logger = Logger()
    logger.log("Test message")
    assert logger.get_logs() == ["Test message"]  # Adjust based on actual method

def test_logging_multiple_messages():
    logger = Logger()
    logger.log("First message")
    logger.log("Second message")
    assert logger.get_logs() == ["First message", "Second message"]

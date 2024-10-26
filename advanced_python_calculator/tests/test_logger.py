# tests/test_logger.py

import os
import pytest
from app.logger import log

def test_logging_creates_logfile():
    log("Test log message")
    assert os.path.exists("logfile.log")

def test_logging_message():
    log("Another log message")
    with open("logfile.log", "r") as f:
        contents = f.read()
    assert "Another log message" in contents

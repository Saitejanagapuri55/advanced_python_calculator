# app/logger.py

import logging
import os

def setup_logger():
    """Sets up the logger configuration."""
    logging.basicConfig(
        filename='logfile.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def log(message):
    """Logs a message to the log file."""
    logger = logging.getLogger()
    logger.info(message)

    # Ensure the log file is created
    if not os.path.exists('logfile.log'):
        open('logfile.log', 'w').close()  # Create an empty file if it does not exist

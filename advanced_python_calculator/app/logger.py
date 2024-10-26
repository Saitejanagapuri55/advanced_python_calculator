# app/logger.py

import logging

# Configure the logger
logging.basicConfig(
    filename='logfile.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log(message):
    """Log a message."""
    logging.debug(message)

"""
This script aims to define a logger with a standard logging message configuration.
Logging messages are employed to track application behavior, errors, and events.
They facilitate debugging, provide insight into program flow, and aid in monitoring and diagnosing issues.
Logging enhances code quality, troubleshooting, and maintenance.
"""

"""
Importing the libraries.
"""

import logging
import os
from datetime import datetime


def setup_logger(log_dir="logs", log_filename=None, level="INFO"):
    """Configures the logging system."""

    if level == "INFO":
        logging_level = logging.INFO
    elif level == "DEBUG":
        logging_level = logging.DEBUG
    elif level == "WARNING":
        logging_level = logging.WARNING
    elif level == "ERROR":
        logging_level = logging.ERROR

    # Create the logs directory if it doesn't exist
    logs_dir = os.path.join(os.getcwd(), log_dir)
    os.makedirs(logs_dir, exist_ok=True)

    # Generate a log filename with date and time if none is provided
    if log_filename is None:
        log_filename = f"app_{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    else:
        log_filename = (
            f"{log_filename}_{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        )

    # Define the full log file path
    log_file_path = os.path.join(logs_dir, log_filename)

    # Configure logging settings
    logging.basicConfig(
        filename=log_file_path,
        format="[ %(asctime)s ] %(lineno)d %(filename)s - %(levelname)s - %(message)s",
        level=logging_level,
        filemode="a",
    )

    # Create a logger instance
    logger = logging.getLogger(__name__)
    return logger


# Example Usage:
# from logger_config import setup_logger

# logger = setup_logger(log_dir="logs", log_filename="my_log", level="DEBUG")

# logger.info("Logging system initialized successfully!")
# logger.error("An error occurred!")
# logger.warning("A warning message!")
# logger.debug("Debugging message!")

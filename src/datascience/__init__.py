# Import necessary modules
import os        # For creating directories and working with file paths
import sys       # For accessing stdout to display logs in the terminal
import logging   # For setting up logging system

# Define the logging format
# Example: [2025-05-05 16:00:00: INFO: myscript: This is a log message]
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory where log files will be stored
log_dir = "logs"

# Define the full path to the log file
log_filepath = os.path.join(log_dir, "logging.log")

# Create the log directory if it doesn't already exist
os.makedirs(log_dir, exist_ok=True)

# Set up the logging configuration
logging.basicConfig(
    level=logging.INFO,           # Set minimum level to INFO (DEBUG messages will be ignored)
    format=logging_str,           # Apply the format defined above
    handlers=[
        logging.FileHandler(log_filepath),    # Write logs to a file at 'logs/logging.log'
        logging.StreamHandler(sys.stdout)     # Also print logs to the console (standard output)
    ]
)

# Create a custom named logger (useful for modular projects)
logger = logging.getLogger("datasciencelogger")

# Example usage
if __name__ == "__main__":
    logger.info("Logging system is initialized.")
    logger.warning("This is a sample warning.")
    logger.error("This is a sample error.")

from loguru import logger

# Logger configuration
def setup_logger():
    # Clear existing handlers
    logger.remove()

    # Add console handler with formatting
    logger.add(sys.stdout, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")

    # Add file handler with formatting
    logger.add("logs/{time:YYYY-MM-DD}.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", rotation="1 day")

setup_logger()
import logging
import os

def setup_logging():
    """Configure logging to save metrics to a file."""
    log_file = os.path.join(os.path.dirname(__file__), '..', 'metrics.log')
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
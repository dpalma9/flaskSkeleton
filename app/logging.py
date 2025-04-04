import logging
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

def setup_logging():

    log_dir = os.getenv('LOG_FOLDER', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs'))
    os.makedirs(log_dir, exist_ok=True)

    # Configure file logger handler
    log_file = os.path.join(log_dir, 'app.log')
    file_handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Configure stream handler (stdout)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Get the root logger and set the level
    logger = logging.getLogger()
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    if log_level == 'DEBUG':
        logger.setLevel(logging.DEBUG)
    elif log_level == 'WARNING':
        logger.setLevel(logging.WARNING)
    elif log_level == 'ERROR':
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.INFO)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.info("Logging is set up.")
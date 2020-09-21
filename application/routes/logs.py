import logging
import os

LOG_DIR = 'logs'+os.sep


def setup_logger(name, log_file, level=logging.INFO):
    log_format = '%(levelname)s %(asctime)s - %(message)s'
    log_format = logging.Formatter(log_format)

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    file_path = LOG_DIR+log_file

    handler = logging.FileHandler(file_path)
    handler.setFormatter(log_format)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


error_logger = setup_logger('error', 'error.log', logging.ERROR)


def error_log(endpoint, method, msg):
    error_msg = 'ENDPOINT: {};'.format(endpoint)
    error_msg += 'METHOD: {};'.format(method)
    error_msg += 'MSG: {};'.format(msg)

    error_logger.error(error_msg)

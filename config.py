import logging
import colorlog

from flask import request
from logging.handlers import TimedRotatingFileHandler


class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)


def setup_logger():
    """Return a logger with a default ColoredFormatter."""

    stream_format = '%(log_color)s%(asctime)s - [ %(levelname)s ]%(reset)s %(message)s'
    file_format = '%(asctime)s - [ %(levelname)s ] %(message)s  (%(filename)s:%(lineno)d)'

    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)

    stream_formatter = colorlog.ColoredFormatter(
        stream_format,
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red',
        }
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(stream_formatter)

    file_formatter = logging.Formatter(file_format)
    file_handler = TimedRotatingFileHandler(
        filename='logs/example.log', when='midnight', backupCount=1)
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.INFO)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger

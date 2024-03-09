import logging
from logging.handlers import RotatingFileHandler

import requests
from constant import BASE_DIR, CONNECT, DT_FORMAT, LOG_FORMAT, UTF


def get_response(url: str):
    try:
        logging.info('Запрос по url!')
        response = requests.get(url)
        response.encoding = UTF
        return response

    except requests.RequestException as e:
        logging.error(f'{CONNECT}_{e}')


def configure_logging():
    '''Конфигурация для логирования.'''
    log_dir = BASE_DIR / 'logs'
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'parser_key.log'

    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=10 ** 6, backupCount=5,
        encoding=UTF
    )
    logging.basicConfig(
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler()),

    )
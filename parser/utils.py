import logging
from logging.handlers import RotatingFileHandler

import requests
from constant import BASE_DIR, CONNECT, UTF

DT_FORMAT = '%d.%m.%Y %H:%M:%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'


def get_response(url: str):
    try:
        logging.info('Подключение к ссылке!')
        response = requests.get(url)
        response.encoding = UTF
        return response

    except requests.RequestException as e:
        logging.error(f'{CONNECT}_{e}')


def configure_logging():
    '''Конфигурация для логирования.'''
    log_file = 'bs4_parser_key_rate/parser/logs/parser_key.log'

    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=10 ** 6, backupCount=5,
        encoding='utf-8'
    )
    logging.basicConfig(
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler()),

    )
import datetime as dt

DATETIME_FORMAT = '%Y-%m-%d'
now = dt.datetime.now()
FORMAT_TIME = now.strftime(DATETIME_FORMAT)
UTF = 'utf-8'
UNIX = 'unix'
BASE_DIR = 'bs4_parser_key_rate/parser/results/2024-02-26.csv'
MAIN_URL = 'https://cbr.ru/'
LXML = 'lxml'


class HTMLtag:
    DIV = 'div'
    CLASS = 'class'
    HOME = 'home-main_aside'
    VALUE = 'col-md-2 col-xs-9 _right mono-num'
    MAIN_VALUE = 'main-indicator_value'
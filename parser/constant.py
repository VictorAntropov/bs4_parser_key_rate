import datetime as dt

DATETIME_FORMAT = '%Y-%m-%d'
now = dt.datetime.now()
FORMAT_TIME = now.strftime(DATETIME_FORMAT)
UTF = 'utf-8'
UNIX = 'unix'
BASE_DIR = 'bs4_parser_key_rate/parser'
MAIN_URL = 'https://cbr.ru/'
CONNECT = 'Проверьте подключение к интернету, также, возможны проблемы на стороне ЦБ РФ'


class HTMLtag:
    DIV = 'div'
    CLASS = 'class'
    HOME = 'home-main_aside'
    VALUE = 'col-md-2 col-xs-9 _right mono-num'
    MAIN_VALUE = 'main-indicator_value'
    LXML = 'lxml'

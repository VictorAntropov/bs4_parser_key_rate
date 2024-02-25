import argparse


def configure_argument_parser(available_models):
    parser = argparse.ArgumentParser(description='Парсер ключевой ставки ЦБ и курс валют')
    parser.add_argument(
        '-o',
        '--output',
        choices=('file'),
        help='Вывод данных в файл'
    return parser
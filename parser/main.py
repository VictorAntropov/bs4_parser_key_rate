import csv
import logging
from typing import List, Optional

import telebot
# import schedule
from bs4 import BeautifulSoup
from constant import BASE_DIR, FORMAT_TIME, MAIN_URL, UNIX, UTF, HTMLtag
from settings import chat_id, token
from utils import configure_logging, get_response

bot = telebot.TeleBot(token=token)


def csv_output(result_list: List[str]) -> str:
    '''Запись в файл.'''

    dir_file = BASE_DIR / 'results/2024-02-26.csv'

    try:
        with open(dir_file, 'a', encoding=UTF) as csvfile:
            writer = csv.writer(csvfile, dialect=UNIX)
            writer.writerow(result_list)
            logging.info('Запись в файл завершена!')

        send_telegram_message(dir_file)
    except FileNotFoundError as e:
        logging.error(f'Файл для записи отсутствует_{e}')

    return 'Парсинг прошел успешно!'


def parser_the_bank() -> Optional[str]:
    '''Получаем необходимые теги и их значения.'''
    response = get_response(MAIN_URL)

    if response is None:
        logging.error('Пустой ответ, повторите запрос позже!')
        return None

    logging.info('Парсинг ЦБ РФ!')
    soup = BeautifulSoup(response.text, features=HTMLtag.LXML)

    div_tag = soup.find(HTMLtag.DIV, attrs={HTMLtag.CLASS: HTMLtag.HOME})
    percent_value = div_tag.find_all(HTMLtag.DIV, class_=HTMLtag.MAIN_VALUE)
    value = div_tag.find_all(HTMLtag.DIV, attrs={HTMLtag.CLASS: HTMLtag.VALUE})

    percent_value = [(item.text.strip()) for item in percent_value]
    result_value = [(item.text.strip()) for item in value]

    result = percent_value + result_value[1::2]
    result.insert(0, FORMAT_TIME)

    return csv_output(result)


def send_telegram_message(file_path: str) -> None:
    '''Отправка файла в ТГ.'''

    with open(file_path, 'rb') as f:
        bot.send_document(chat_id, f)
        logging.info('Файл успешно отправлен в ТГ!')


def main() -> None:
    configure_logging()
    logging.info('Парсер запущен')
    print(parser_the_bank())
    # schedule.every().monday.do(parser_the_bank)
    # while True:
    #     schedule.run_pending()


if __name__ == '__main__':
    main()

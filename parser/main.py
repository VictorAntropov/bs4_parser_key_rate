import csv
from typing import List

import telebot
# import schedule
from bs4 import BeautifulSoup
from constant import BASE_DIR, FORMAT_TIME, MAIN_URL, UNIX, UTF, HTMLtag
from settings import chat_id, token
from utils import get_response

bot = telebot.TeleBot(token=token)


def csv_output(result_list: List[str]) -> str:
    '''Запись в файл.'''
    dir = BASE_DIR

    try:
        with open(dir, 'a', encoding=UTF) as csvfile:
            writer = csv.writer(csvfile, dialect=UNIX)
            writer.writerow(result_list)

        send_telegram_message(dir)
    except FileNotFoundError as e:
        print(f'{e}Файл для записи отсутствует!')

    return 'Файл отправлен, работа парсера завершена!'


def parser_the_bank() -> str:
    '''Получаем необходимые теги и их значения.'''
    response = get_response(MAIN_URL)

    if response is None:
        return

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


def main() -> None:
    print('Парсер запустился')
    print(parser_the_bank())
    # schedule.every().monday.do(parser_the_bank)
    # while True:
    #     schedule.run_pending()


if __name__ == '__main__':
    main()
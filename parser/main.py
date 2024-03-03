import requests
import csv
import telebot
import schedule
from bs4 import BeautifulSoup
from constant import (UTF, FORMAT_TIME, UNIX,
                      BASE_DIR, MAIN_URL, LXML, HTMLtag)
from utils import get_response


bot = telebot.TeleBot(token='5865043978:AAEawcnDACERjDdwuOQ9ovlq69hiPxHdhdY')


def csv_output(result_list):
    'Запись в файл.'
    dir = BASE_DIR

    with open(dir, 'a', encoding=UTF) as csvfile:
        writer = csv.writer(csvfile, dialect=UNIX)
        writer.writerow(result_list)

    send_telegram_message(dir)


def parser_the_bank() -> list:
    '''Получаем необходимые теги и их значения.'''
    response = requests.get(MAIN_URL)
    soup = BeautifulSoup(response.text, features=LXML)

    div_tag = soup.find(HTMLtag.DIV, attrs={HTMLtag.CLASS: HTMLtag.HOME})
    percent_value = div_tag.find_all(HTMLtag.DIV, class_=HTMLtag.MAIN_VALUE)
    value = div_tag.find_all(HTMLtag.DIV, attrs={HTMLtag.CLASS: HTMLtag.VALUE})

    percent_value = [(item.text.strip()) for item in percent_value]
    result_value = [(item.text.strip()) for item in value]

    result = percent_value + result_value[1::2]
    result.insert(0, FORMAT_TIME)

    return csv_output(result)


def send_telegram_message(file_path) -> None:
    '''Отправка файла в ТГ.'''
    chat_id = '1772370235'
    with open(file_path, 'rb') as f:
        bot.send_document(chat_id, f)


def main():
    print('Парсер запустился')
    print(parser_the_bank())
    # schedule.every().monday.do(parser_the_bank)
    # while True:
    #     schedule.run_pending()


if __name__ == '__main__':
    main()

import requests
import csv
import telebot
import schedule
from bs4 import BeautifulSoup
from constant import (UTF, FORMAT_TIME, UNIX, BASE_DIR, URL_CB, LXML)
from utils import get_response


bot = telebot.TeleBot(token='5865043978:AAEawcnDACERjDdwuOQ9ovlq69hiPxHdhdY')


def csv_output(result_list):
    dir = BASE_DIR

    with open(dir, 'a', encoding=UTF) as csvfile:
        writer = csv.writer(csvfile, dialect=UNIX)
        writer.writerow(result_list)

    send_telegram_message(dir)


def parser_the_bank():
    response = requests.get(URL_CB)
    soup = BeautifulSoup(response.text, features=LXML)
    div_tag = soup.find('div', attrs={'class': 'home-main_aside'})
    percent_value = div_tag.find_all('div', class_='main-indicator_value')
    value = div_tag.find_all('div', attrs={'class': 'col-md-2 col-xs-9 _right mono-num'})
    percent_value = [(item.text.strip()) for item in percent_value]
    result_value = [(item.text.strip()) for item in value]

    result = percent_value + result_value[1::2]
    result.insert(0, FORMAT_TIME)

    return csv_output(result)


def send_telegram_message(file_path):
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
    'Запуск'
    main()

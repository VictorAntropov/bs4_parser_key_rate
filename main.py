import requests
import csv
import telebot
import schedule
import time

from bs4 import BeautifulSoup
from pathlib import Path
import datetime as dt


BASE_DIR = Path(__file__).parent
DATETIME_FORMAT = '%Y-%m-%d'
now = dt.datetime.now()
format_time = now.strftime(DATETIME_FORMAT)
bot = telebot.TeleBot(token='5865043978:AAEawcnDACERjDdwuOQ9ovlq69hiPxHdhdY')


def csv_output(results, result_list):
    dir = BASE_DIR / 'results'
    file_path = dir / '2024-02-26.csv'

    with open(file_path, 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, dialect='unix')
        writer.writerow(result_list)

    send_telegram_message(file_path)


def parser_the_bank():
    a = []
    b = []
    now = dt.datetime.now()
    format_time = now.strftime(DATETIME_FORMAT)
    results = ['Дата', 'Цель по инфляции', 'Инфляция', 'Ключевая ставка', 'Ставка RUOINIA', 'CNY', 'USD', 'EUR']
    response = requests.get('https://cbr.ru/')
    soup = BeautifulSoup(response.text, features='lxml')
    div_tag = soup.find('div', attrs={'class': 'home-main_aside'})
    div_tag_2 = div_tag.find_all('div', class_='main-indicator_value')
    div_tag_3 = div_tag.find_all('div', attrs={'class': 'col-md-2 col-xs-9 _right mono-num'})

    for i in div_tag_2:
        b.append(i.text.strip())

    for i in div_tag_3:
        a.append(i.text.strip())

    result_list = b + a[1::2]
    result_list.insert(0, format_time)
    print(result_list)
    csv_output(results, result_list)


def send_telegram_message(file_path):
    chat_id = '1772370235'
    with open(file_path, 'rb') as f:
        bot.send_document(chat_id, f)


# schedule.every(10).seconds.do(parser_the_bank)

# while True:
#     schedule.run_pending()


def main():
    print('Парсер запустили')
    # schedule.every(10).seconds.do(parser_the_bank)
    # while True:
    #     schedule.run_pending()
    if __name__ == '__main__':
        main()
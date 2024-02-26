import requests
import csv
import telebot
import schedule
from bs4 import BeautifulSoup
from pathlib import Path
import datetime as dt
from src import constants as const


BASE_DIR = Path(__file__).parent
# DATETIME_FORMAT = '%Y-%m-%d'
# now = dt.datetime.now()
# FORMAT_TIME = now.strftime(DATETIME_FORMAT)
# UTF = 'utf-8'

bot = telebot.TeleBot(token='5865043978:AAEawcnDACERjDdwuOQ9ovlq69hiPxHdhdY')


def csv_output(result_list):
    dir = const.BASE_DIR / 'results'
    file_path = dir / '2024-02-26.csv'

    with open(file_path, 'a', encoding=const.UTF) as csvfile:
        writer = csv.writer(csvfile, dialect='unix')
        writer.writerow(result_list)

    send_telegram_message(file_path)


def parser_the_bank():
    response = requests.get('https://cbr.ru/')
    soup = BeautifulSoup(response.text, features='lxml')
    div_tag = soup.find('div', attrs={'class': 'home-main_aside'})
    percent_value = div_tag.find_all('div', class_='main-indicator_value')
    value = div_tag.find_all('div', attrs={'class': 'col-md-2 col-xs-9 _right mono-num'})
    percent_value = [(item.text.strip()) for item in percent_value]
    result_value = [(item.text.strip()) for item in value]

    result = percent_value + result_value[1::2]
    
    result.insert(0, const.FORMAT_TIME)

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

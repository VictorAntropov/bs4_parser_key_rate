import requests
from bs4 import BeautifulSoup
import re


reg = r'[0-9,%]$'


def parser_the_bank():
    a = []
    b = []
    response = requests.get('https://cbr.ru/')
    soup = BeautifulSoup(response.text, features='lxml')
    div_tag = soup.find('div', attrs={'class': 'home-main_aside'})
    div_tag_2 = div_tag.find_all('div', class_='main-indicator_value')
    div_tag_3 = div_tag.find_all('div', attrs={'class': 'col-md-2 col-xs-9 _right mono-num'})

    for i in div_tag_2:
        b.append(i.text.strip())
    print(b)

    for i in div_tag_3:
        a.append(i.text.strip())
    print(a)


    # results = [('Цель по инфляции', 'Инфляция', 'Ключевая ставка', 'Ставка RUOINIA', 'CNY', 'USD', 'EUR')]
    


print(parser_the_bank())


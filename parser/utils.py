from constant import CONNECT

import requests
from requests import RequestException


def get_response(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException as e:
        print(f'{CONNECT} {e}')

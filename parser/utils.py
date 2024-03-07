import requests
from requests import RequestException

from constant import CONNECT, UTF


def get_response(url):
    try:
        response = requests.get(url)
        response.encoding = UTF
        return response
    except RequestException as e:
        print(f'{CONNECT}_{e}')

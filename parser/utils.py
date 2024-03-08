import requests
from constant import CONNECT, UTF


def get_response(url: str):
    try:
        response = requests.get(url)
        response.encoding = UTF
        return response

    except requests.RequestException as e:
        print(f'{CONNECT}_{e}')

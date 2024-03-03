from requests import RequestException


def get_response(session, url):
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException as e:
        print(f'У нас проблемы {e}')

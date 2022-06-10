from time import sleep
from random import uniform, choice

from fake_headers import Headers


def get_headers():
    headers = Headers(headers=True).generate()
    return headers


with open(r'C:\DiskD\PyProjects\ParserProxy\good_proxy.txt') as file:
    data = ''.join(file.readlines()).strip().split('\n')


def get_random_proxy():
    proxy = choice(data)
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

    return proxies


def wait():
    return sleep(uniform(2, 6))

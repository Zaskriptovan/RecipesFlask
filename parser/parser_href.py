import re
from random import choice

import requests
from bs4 import BeautifulSoup

from config import url, headers, random_proxy, data


def get_tags_a(page):
    print(random_proxy(choice(data)))
    response = requests.get(url=f'{url}?page={page}', headers=headers, proxies=random_proxy(choice(data)))
    soup = BeautifulSoup(response.text, 'lxml')
    tags_a = soup.find_all('a', class_='title', href=re.compile("/recipes/"))

    return tags_a


def get_hrefs(page):
    tags_a = get_tags_a(page)
    hrefs_one_page = []
    for i in tags_a:
        recipes_href = i['href']
        hrefs_one_page.append(url + recipes_href)

    return hrefs_one_page

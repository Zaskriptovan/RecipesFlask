import re

from bs4 import BeautifulSoup
import requests

from config import url, headers

session = requests.Session()


def get_recipes_href(all_a):
    all_recipes_hrefs = []
    for i in all_a:
        recipes_href = i['href']
        all_recipes_hrefs.append(url + recipes_href)

    return all_recipes_hrefs


def get_recipes_a(page):
    response = session.get(url=f'{url}?page={page}', headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    recipes_a = bs.find_all('a', class_='title', href=re.compile("/recipes/"))

    return recipes_a

import re

from bs4 import BeautifulSoup
import requests

from config import url, headers

session = requests.Session()


def get_recipe_title(bs):
    recipes_title = bs.find('h1', class_="title").text

    return recipes_title


def get_content(hrefs):
    titles = []
    for hr in hrefs:
        response = session.get(url=hr, headers=headers)
        bs = BeautifulSoup(response.text, 'lxml')

        tit = get_recipe_title(bs)
        titles.append(tit)

    return titles


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

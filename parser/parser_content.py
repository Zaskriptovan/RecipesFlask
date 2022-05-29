from bs4 import BeautifulSoup
import requests

from config import headers

session = requests.Session()


def get_ingredients(bs):
    ingredients = bs.find('table', class_="ingr").find_all('span', class_='')
    return ingredients


def get_recipe_title(bs):
    recipes_title = bs.find('h1', class_="title").text
    return recipes_title


def get_content(hrefs):
    content = dict()
    for hr in hrefs:
        response = session.get(url=hr, headers=headers)
        bs = BeautifulSoup(response.text, 'lxml')

        title = get_recipe_title(bs)
        ingredients = get_ingredients(bs)
        recipe_text = 0

        content[title] = [ingredients, recipe_text]

    return content

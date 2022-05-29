from bs4 import BeautifulSoup

from config import headers
from parser_href import session


def get_recipe_text(bs):
    try:
        recipe_text = bs.find('div', class_="step_images_n").find_all('p')
    except AttributeError:
        recipe_text = False

    return recipe_text


def get_ingredients(bs):
    ingredients = bs.find('table', class_="ingr").find_all('span', class_='')
    all_ingredients = []
    for i in ingredients:
        ing = i.text
        all_ingredients.append(ing)

    return all_ingredients


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
        recipe_text = get_recipe_text(bs)

        if recipe_text:
            content[title] = [ingredients, recipe_text]

    return content

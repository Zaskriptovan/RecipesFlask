from random import choice

import requests
from bs4 import BeautifulSoup

from config import headers, pause, random_proxy, data


def get_recipe_text(soup):
    try:
        tags_p = soup.find('div', class_="step_images_n").find_all('p')
        recipe_text = ''
        for p in tags_p:
            recipe_text += p.text.replace("\n", "") + ' '
    except AttributeError:
        recipe_text = False

    return recipe_text.replace("...", "")


def get_ingredients(soup):
    spans = soup.find('table', class_="ingr").find_all('span', class_='')
    ingredients = []
    for span in spans:
        ing = span.text
        ingredients.append(ing)

    return ingredients


def get_recipe_title(soup):
    recipes_title = soup.find('h1', class_="title").text
    return recipes_title


def get_content(hrefs_one_page):
    count = 1
    content_dict = dict()
    for hr in hrefs_one_page:
        print(random_proxy(choice(data)))
        response = requests.get(url=hr, headers=headers, proxies=random_proxy(choice(data)))
        soup = BeautifulSoup(response.text, 'lxml')

        title = get_recipe_title(soup)
        ingredients = get_ingredients(soup)
        recipe_text = get_recipe_text(soup)

        if title and ingredients and recipe_text:
            content_dict[title] = [ingredients, recipe_text]

            print('Добавлен', count, 'рецепт')
            count += 1

        pause()

    return content_dict

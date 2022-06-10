import re

import requests
from bs4 import BeautifulSoup

from immunity import get_headers, get_random_proxy, wait


class Request:
    @classmethod
    def do_request(cls, url):
        response = requests.get(url=url, headers=get_headers(), proxies=get_random_proxy())
        return response


class SaveToDatabase:
    @classmethod
    def save_to_database(cls, title, ingredients, recipe_text):
        print(title)
        print(ingredients)
        print(recipe_text)


class Parser:
    @classmethod
    def create_soup(cls, response):
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    @classmethod
    def get_tags_a(cls, page, home_url):
        response = Request.do_request(url=f'{home_url}?page={page}')
        soup = cls.create_soup(response)
        tags_a = soup.find_all('a', class_='title', href=re.compile("/recipes/"))

        return tags_a

    @classmethod
    def get_hrefs(cls, page, home_url):
        tags_a = cls.get_tags_a(page, home_url)
        hrefs_one_page = []
        for i in tags_a:
            recipes_href = i['href']
            hrefs_one_page.append(home_url + recipes_href)

        return hrefs_one_page

    @classmethod
    def get_recipe_text(cls, soup):
        try:
            tags_p = soup.find('div', class_="step_images_n").find_all('p')
            recipe_text = ''
            for p in tags_p:
                recipe_text += p.text.replace("\n", "") + ' '
        except AttributeError:
            recipe_text = False

        return recipe_text.replace("...", "")

    @classmethod
    def get_ingredients(cls, soup):
        spans = soup.find('table', class_="ingr").find_all('span', class_='')
        ingredients = []
        for span in spans:
            ing = span.text
            ingredients.append(ing)

        return ingredients

    @classmethod
    def get_recipe_title(cls, soup):
        recipes_title = soup.find('h1', class_="title").text
        return recipes_title

    @classmethod
    def get_content(cls, hrefs_one_page):
        count = 1
        for hr in hrefs_one_page:
            response = Request.do_request(url=hr)
            soup = cls.create_soup(response)

            title = cls.get_recipe_title(soup)
            ingredients = cls.get_ingredients(soup)
            recipe_text = cls.get_recipe_text(soup)

            if title and ingredients and recipe_text:
                SaveToDatabase.save_to_database(title, ingredients, recipe_text)

                print('Добавлен', count, 'рецепт')
                count += 1
            wait()

    @classmethod
    def run(cls, pages_quantity, home_url):
        for page in range(1, pages_quantity + 1):
            hrefs_one_page = cls.get_hrefs(page, home_url)
            wait()
            cls.get_content(hrefs_one_page)

            print(f'Обработал {page}/{pages_quantity} страниц')

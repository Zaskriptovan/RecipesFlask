import re

import requests
from bs4 import BeautifulSoup

from immunity import get_headers, get_random_proxy, wait


class Request:
    @staticmethod
    def do_request(url):
        while True:
            proxies = get_random_proxy()
            try:
                response = requests.get(url=url, headers=get_headers(), proxies=proxies)
                return response
            except:
                print(f'>>>>>Прокси не сработал {proxies}<<<<<')
                continue


class SaveToDB:
    @staticmethod
    def save_to_db(title, ingredients, recipe_text):
        print(title)
        print(ingredients)
        print(recipe_text)


class Parser:

    def __init__(self, pages_quantity, home_url):
        self.pages_quantity = pages_quantity
        self.home_url = home_url

    @staticmethod
    def create_soup(response):
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def get_tags_a(self, page):
        response = Request.do_request(url=f'{self.home_url}?page={page}')
        soup = self.create_soup(response)
        tags_a = soup.find_all('a', class_='title', href=re.compile("/recipes/"))

        return tags_a

    def get_hrefs(self, page):
        tags_a = self.get_tags_a(page)
        hrefs_one_page = []
        for i in tags_a:
            recipes_href = i['href']
            hrefs_one_page.append(self.home_url + recipes_href)

        return hrefs_one_page

    @staticmethod
    def get_recipe_text(soup):
        try:
            tags_p = soup.find('div', class_="step_images_n").find_all('p')
            recipe_text = ''
            for p in tags_p:
                recipe_text += p.text.replace("\n", "") + ' '
        except AttributeError:
            recipe_text = False

        return recipe_text.replace("...", "")

    @staticmethod
    def get_ingredients(soup):
        spans = soup.find('table', class_="ingr").find_all('span', class_='')
        ingredients = []
        for span in spans:
            ing = span.text
            ingredients.append(ing)

        return ingredients

    @staticmethod
    def get_recipe_title(soup):
        recipes_title = soup.find('h1', class_="title").text
        return recipes_title

    def get_content(self, hrefs_one_page):
        count = 1
        for hr in hrefs_one_page:
            response = Request.do_request(url=hr)
            soup = self.create_soup(response)

            title = self.get_recipe_title(soup)
            ingredients = self.get_ingredients(soup)
            recipe_text = self.get_recipe_text(soup)

            if title and ingredients and recipe_text:
                SaveToDB.save_to_db(title, ingredients, recipe_text)

                print('===Добавлен', count, 'рецепт===')
                count += 1
            wait()

    def run(self):
        for page in range(1, self.pages_quantity + 1):
            hrefs_one_page = self.get_hrefs(page)
            wait()
            self.get_content(hrefs_one_page)

            print(f'Обработал {page}/{self.pages_quantity} страниц')
import re

import requests
from bs4 import BeautifulSoup

from immunity import get_headers, get_random_proxy, wait


class CheckText:

    @staticmethod
    def check_str(text):
        pattern = '[а-яА-Яa-zA-Z]'
        if re.search(pattern, text):
            return True


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


class Parser:

    def __init__(self, home_url, pages_quantity):
        self.home_url = home_url
        self.pages_quantity = pages_quantity

    @staticmethod
    def _create_soup(response):
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def _get_tags_a(self, page):
        response = Request.do_request(url=f'{self.home_url}?page={page}')
        soup = self._create_soup(response)
        tags_a = soup.find_all('a', class_='title', href=re.compile("/recipes/"))

        return tags_a

    def _get_hrefs(self, page):
        tags_a = self._get_tags_a(page)
        hrefs_one_page = []
        for i in tags_a:
            recipes_href = i['href']
            hrefs_one_page.append(self.home_url + recipes_href)

        return hrefs_one_page

    @staticmethod
    def _get_recipe_description(soup):
        try:
            tags_p = soup.find('div', class_="step_images_n").find_all('p')
            recipe_description = ''
            for p in tags_p:
                recipe_description += p.text.replace("\n", "") + ' '
        except AttributeError:
            recipe_description = False

        return recipe_description.replace("...", "")

    @staticmethod
    def _get_ingredients_and_quantity(soup):
        spans = soup.find('table', class_="ingr").find_all('span', class_='')
        ingredients = dict()
        for span in spans:
            ing = span.text
            if CheckText.check_str(ing):
                try:
                    result = re.split(r'[-—]', ing, maxsplit=1)
                    ingredients[result[0].strip()] = result[1].strip()
                except:
                    pass
        return ingredients

    @staticmethod
    def _get_recipe_title(soup):
        recipes_title = soup.find('h1', class_="title").text
        return recipes_title

    def get_content(self):
        content_dict = dict()
        for page in range(1, self.pages_quantity + 1):
            hrefs_one_page = self._get_hrefs(page)
            wait()
            count = 1
            for hr in hrefs_one_page:
                response = Request.do_request(url=hr)
                soup = self._create_soup(response)

                title = self._get_recipe_title(soup)
                ingredients = self._get_ingredients_and_quantity(soup)
                description = self._get_recipe_description(soup)

                if title and ingredients and description:
                    content_dict[title] = [ingredients, description]
                    print(f'=== Спарсил рецептов: {count} ===')
                    count += 1
                wait()

            print(f'Обработал {page}/{self.pages_quantity} страниц')

        return content_dict


class WriteRecipesToDB:

    @staticmethod
    def save_to_db(recipes):
        for title, ing_and_description in recipes.items():
            print(title)
            print(ing_and_description[0])
            print(ing_and_description[1])
            print('--------------------------------------------------------------')

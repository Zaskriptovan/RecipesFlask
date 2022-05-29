import time
from random import randint

from parser_href import *
from parser_content import *

PAGES_QUANTITY = 1


def main():
    for page in range(1, PAGES_QUANTITY + 1):
        as_some_page = get_recipes_a(page)
        hrefs_some_page = get_recipes_href(as_some_page)
        content = get_content(hrefs_some_page)

        for key, value in content.items():
            print(key, ':', value)

        print(f'Обработал {page}/{PAGES_QUANTITY} страниц')
        time.sleep(randint(2, 5))


if __name__ == '__main__':
    main()

from parser_href import *
from parser_content import *
from config import pause

PAGES_QUANTITY = 2


def main():
    for page in range(1, PAGES_QUANTITY + 1):
        hrefs_one_page = get_hrefs(page)
        content_one_page = get_content(hrefs_one_page)

        for key, value in content_one_page.items():
            print(f'{key}:\n{value[0]}')
            print(value[1], '\n-----------------------------------------')

        print(f'Обработал {page}/{PAGES_QUANTITY} страниц\n====================================')
        pause()


if __name__ == '__main__':
    main()

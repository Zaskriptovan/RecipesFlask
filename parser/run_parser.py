from config import home_url
from parser import Parser

PAGES_QUANTITY = 2

if __name__ == '__main__':
    Parser.run(PAGES_QUANTITY, home_url)

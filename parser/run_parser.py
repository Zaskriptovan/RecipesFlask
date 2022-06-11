from config import home_url
from parser import Parser

PAGES_QUANTITY = 2

if __name__ == '__main__':
    parser = Parser(PAGES_QUANTITY, home_url)
    parser.run()

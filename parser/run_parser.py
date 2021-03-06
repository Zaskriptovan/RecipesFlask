from config import home_url
from parser import Parser, WriteRecipesToDB

PAGES_QUANTITY = 5

if __name__ == '__main__':
    parser = Parser(home_url, PAGES_QUANTITY)
    recipes_dict = parser.get_content()

    WriteRecipesToDB.save_to_db(recipes_dict)

import time
from random import randint

from bs4 import BeautifulSoup
import requests

url = 'https://www.russianfood.com/?page='

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/'
              'avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.59'
}

session = requests.Session()

for page in range(1, 3):
    response = session.get(url=url + str(page), headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')

    all_rec_url = bs.find_all('a', class_='title')

    for i in all_rec_url:
        rec_url = i.get('href')
        print(rec_url)

    print(f'Обработал {page} страницу')
    time.sleep(randint(2, 5))  # задержка перехода по страницам сайта

# response = session.get(url=url, headers=headers)
#
# bs = BeautifulSoup(response.text, 'lxml')
# pagination = int(bs.find('table', class_='page_selector').find_all('a')[-2].text)

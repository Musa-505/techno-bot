from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import datetime
import requests
import io
import csv
import openpyxl

# aw = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
# now = "kaspi.storefront.cookie.city=750000000;"
# "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"

def collect_data(city_code='750000000'):
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    us = UserAgent()

    headers = {
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    	'User-Agent': us.random
    }

    cookies = {
    	'kaspi.storefront.cookie.city': f'{ city_code}'
    }

    # response = requests.get(url='https://kaspi.kz/shop/c/smartphones/brand-apple/', headers=headers, cookies=cookies)

    # with io.open(f'index.html', 'w', encoding="utf-8") as file:
    # 	file.write(response.text)
    with open("index.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    city = soup.find('a', class_='current-location')

    card_name = soup.findAll('a', class_='item-card__name')
    card_price = soup.findAll('span', class_='item-card__prices-price')

    card_as = soup.findAll('span', class_='item-card__prices-title')

    card_prices = soup.findAll('div', class_='item-card__debet')
    card_inc = soup.findAll('div', class_='item-card__instalment')

    for noneco in card_prices:
        none = noneco.text

    for incd in card_inc:
        inc = incd.text

    card_price_p = soup.findAll('div', class_='item-card__instalment')

    card_info = soup.findAll('span', class_='item-card__add-info') 
    
    def create_xlsx():
        row = 2
        book = openpyxl.Workbook()

        sheet = book.active

        sheet['A1'] = "Name object"
        sheet['B1'] = "Price object"
        sheet['C1'] = "Price object"

        for name in card_name:
            sheet[row][0].value = name.text
            for price in card_prices:
                sheet[row][1].value = none
                for iop in card_inc:
                    sheet[row][2].value = inc
            row += 1
            
        

        book.save("my_book.xlsx")
        book.close()
    
    create_xlsx()

def main():
    collect_data(city_code='750000000')

if __name__ == '__main__':
    main()

# def collect_data(city_code='750000000'):
#     cur_time = datetime.datetime.now().strftime
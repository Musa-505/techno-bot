from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import lxml

city_code='750000000'
us = UserAgent()

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'User-Agent': us.random
}

cookies = {
	'kaspi.storefront.cookie.city': f'{ city_code}'
}

for page in range(11):
	page = page

	response = requests.get(url='https://kaspi.kz/shop/c/smartphones/brand-apple/'+'?{page}', headers=headers, cookies=cookies)

	src = (response.text)

	soup = BeautifulSoup(src, 'lxml')

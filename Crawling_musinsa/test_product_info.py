import re
import math
from bs4 import BeautifulSoup
from urllib import request
#https://store.musinsa.com/app/product/detail/1627609/0
html = request.urlopen('https://store.musinsa.com/app/product/detail/1466038/0')
soup = BeautifulSoup(html, 'lxml')

brand = soup.select_one('#product_order_info > div.explan_product.product_info_section > ul > li:nth-child(1) > p.product_article_contents > strong > a').text

season = soup.select_one('#product_order_info > div.explan_product.product_info_section > ul > li:nth-child(2) > p.product_article_contents > strong').text
season = re.compile(r'\s+').sub('', season)

name = soup.select_one('#page_product_detail > div.right_area.page_detail_product > div.right_contents.section_product_summary > span').text
name = re.compile(r'\s+').sub('', name)

sex = soup.select_one('#product_order_info > div.explan_product.product_info_section > ul > li:nth-child(2) > p.product_article_contents > span.txt_gender > span').text

price = soup.select_one('#goods_price').text
price = re.compile(r'\s+').sub('', price)
price = re.compile(',').sub('', price)

print(brand)
print(season)
print(name)
print(sex)
print(price)
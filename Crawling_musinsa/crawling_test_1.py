from bs4 import BeautifulSoup
import re
import urllib.request

url = 'https://store.musinsa.com/app/items/lists/017'

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, 'lxml')

print(html)
print(soup.select_one('body > div.wrap > div.right_area.page_items_lists > form > div:nth-child(29) > dl > dd > ul > li:nth-child(1) > a')['href'])

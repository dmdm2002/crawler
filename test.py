from bs4 import BeautifulSoup
import urllib.request
import re

site_url = 'https://search.musinsa.com/category/017009?d_cat_cd=017009&a_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=90&page=1&list_kind=small&free_dlv=&sale_goods=&price=&color=&size=&campaign_yn=&bwith_yn=&popup='
a = '#goods_list > div.boxed-list-wrapper > div.pagingNumber-box.box > span > span.totalPagingNum'
html = urllib.request.urlopen(site_url)
soup = BeautifulSoup(html, 'lxml')

z = soup.select_one(a).text
print(z)
for i in range(1, int(z)):
    count = i - 1
    print(count)
    print(i)
    site_url = re.compile(f'&page={i-1}').sub(f'&page={i}', site_url)
    print(site_url)

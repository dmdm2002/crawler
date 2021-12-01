from setting.Page import page
from Crawling_musinsa.product_info import Product_info
from Crawling_musinsa.img_info import image_info
import re
import math
from bs4 import BeautifulSoup
from urllib import request

class Product_list(page):
    def __init__(self, url):
        super(Product_list, self).__init__(url)

    def find_proCount(self):
        total_product = self.soup.select_one('#contentsItem_list > div.boxed-list-wrapper > div.thumbType_box.box > span.counter.box_num_goods > label').text
        # 해당 카테고리 전체 상품 갯수에서 필요없는 문자 제거
        total_product = re.compile(' ').sub('', total_product)
        total_product = re.compile('[가-힣]+').sub('', total_product)
        total_product = re.compile(':').sub('', total_product)
        total_product = re.compile(',').sub('', total_product)
        print(total_product)

        pageCount = math.ceil(int(total_product) / 90)

        return pageCount

    def through_page_crawling(self, pageCount, category):
        now_page_url = self.url
        for i in range(1, pageCount + 1):
            # 해당 페이지 상품들의 url list
            page_product_list_url = []
            print(f'------------------page{i}------------------')
            # 현재 페이지의 url
            if i == 1:
                pass
            else:
                now_page_url = re.compile(f'page={i-1}').sub(f'page={i}', now_page_url)

            html = request.urlopen(now_page_url)
            soup = BeautifulSoup(html, 'lxml')

            # 상품의 url 정보를 전부 받아온다.(각 상품에 대한 href 만 있는 것이 아닌 필요없는 정보도 모두 포함되어 있다.)
            page_product_list_url = soup.select('#searchList > li > div.li_inner > div.list_img > a')
            if page_product_list_url is None:
                print('상품이 없는 페이지')
            else:
                pass

            for j in range(0, len(page_product_list_url)):
                # page_product_list_url 의 정보중 href 를 추출한다.
                product_url = page_product_list_url[j]['href']
                product_url = self.site_url + product_url

                pi = Product_info(product_url)
                img = image_info(product_url)

                pi.crawling_product_info(category)
                fin = self.db.db_get('fin', 'clothes_product', 'url', product_url)
                if fin == '1': pass
                else:
                    product_id = self.db.db_get('id', 'clothes_product', 'url', product_url)
                    img.crawling_image(product_id)

    def crawling_product_list(self, category):
        pageCount = self.find_proCount()
        self.through_page_crawling(pageCount, category)
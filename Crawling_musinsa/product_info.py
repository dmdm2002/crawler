from setting.Page import page
import re
import math

class Product_info(page):
    def __init__(self, url):
        super(Product_info, self).__init__(url)

    def crawling_product_info(self, category):
        try:
            brand = self.soup.select_one(
                '#product_order_info > div.explan_product.product_info_section > ul > li:nth-child(1) > p.product_article_contents > strong > a').text

            season = self.soup.select_one(
                '#product_order_info > div.explan_product.product_info_section > ul > li:nth-child(2) > p.product_article_contents > strong')
            if season is not None:
                season = season.text
                season = re.compile(r'\s+').sub('', season)
            else:
                pass

            name = self.soup.select_one(
                '#page_product_detail > div.right_area.page_detail_product > div.right_contents.section_product_summary > span').text
            name = re.compile(r'\s+').sub('', name)

            sex = self.soup.select_one(
                '#product_order_info > div.explan_product.product_info_section > ul > li:nth-child(2) > p.product_article_contents > span.txt_gender > span').text

            price = self.soup.select_one('#goods_price').text
            price = re.compile(r'\s+').sub('', price)
            price = re.compile(',').sub('', price)

            product_info = [brand, name, price, season, sex, self.url, category]
            self.db.db_insert('clothes_product', ['brand', 'name', 'price', 'season', 'sex', 'url', 'category'], product_info)

            print(product_info)
        except:
            pass
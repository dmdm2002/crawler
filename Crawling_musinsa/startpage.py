from setting.Page import page
from Crawling_musinsa.product_list import Product_list

class StartPage(page):
    def __init__(self, url):
        super(StartPage, self).__init__(url)

    def crawling_site(self):

        for i in range(1, 3):
            href = self.soup.select(
                f'body > div.wrap > div.right_area.page_items_lists > form > div.division_box.hover_box.box_division_group > dl > dd > ul > li:nth-child({i}) > a')
            temp = href[0]['href']
            crawling_href_list = self.site_url + temp
            print(crawling_href_list)
            if i == 1 :
                tmep = 'https://search.musinsa.com/category/017009'
            else:
                tmep = 'https://search.musinsa.com/category/017010'

            category = self.db.db_get('id', 'clothes_category', 'url', tmep)
            pl = Product_list(crawling_href_list)
            pl.crawling_product_list(category)
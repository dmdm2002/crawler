from setting import database
from bs4 import BeautifulSoup
from pymysql.err import DataError
import urllib.request
import socket
import urllib.error


class page(object):

    def __init__(self, url):
        self.url = url
        self.site_name = 'musinsa'
        self.db = database.DBset('cupit_db')
        self.site_url = 'https://store.musinsa.com/'
        try :
            html = urllib.request.urlopen(url)
            self.soup = BeautifulSoup(html,'lxml')
        except urllib.error.URLError :
            self.err_product(0, 'urlerror', self.url, 0, f'urlerror {self.url}')
        self.timeout = 10
        socket.setdefaulttimeout(self.timeout)

    def err_product(self, category, err_type, url, product_id=-1, etc='NULL'):
        err_col = ['category', 'product_id', 'error_code', 'status', 'etc', 'url']
        try:
            if product_id < 0:
                product_id = 'NULL'
            err_val = [category, product_id, err_type, 'not solved', etc, url]
            self.db.db_insert('err_product', err_col, err_val)
        except DataError:
            etc = etc[:50]
            etc_val = [category, product_id, err_type, 'not solved', etc, url]
            self.db.db_insert('err_prodcut', err_col, etc_val)
        else:
            pass

        return


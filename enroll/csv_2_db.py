import pandas as pd
import numpy as np
from setting.Page import page

class Csv_2_db(page):
    def __init__(self, url):
        super(Csv_2_db, self).__init__(url)
        self.site_name = 'musinsa'
    def csv_2_db(self):
        print(self.site_name)
        enroll_df = pd.read_csv(f'../categoryCSV/{self.site_name}_category.csv', encoding='utf-8')
        url_df = enroll_df.url
        text_df = enroll_df.text
        url_arr = np.array(url_df).tolist()
        text_arr = np.array(text_df).tolist()
        self.db.db_insert('clothes_site', ['name', 'url'], [self.site_name, self.url])
        print(text_arr)
        print(url_arr)
        for i in range(0, len(url_arr)):
            site = self.db.db_get('id', 'clothes_site', 'url', self.url)
            self.db.db_insert('clothes_category', ['site_id', 'name', 'url'], [site, text_arr[i], url_arr[i]])
        self.db.db_update('clothes_site', 'setting', 'True', 'url', self.url)
        # print(csv_df.iloc['number'])

url = 'https://store.musinsa.com/'
a = Csv_2_db(url)
a.csv_2_db()
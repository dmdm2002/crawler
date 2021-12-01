from setting.Page import page
import setting.img_func as pi
import re

class image_info(page):
    def __init__(self, url):
        super(image_info, self).__init__(url)

    def crawling_image(self, product_id):
        try:
            src = self.soup.select_one('#bigimg')['src']
            img_src = f'https:{src}'
            print(f'image({img_src}) save to file and DB')
            di = f'./image/{self.site_name}/{product_id}'

            # image table 과 image_mapping table 에 넣을 column 들
            img_col = ['product_id', 'img_src', 'file_path', 'file_name', 'extension']
            # <$$$> jpg - png 자주 바꿈
            extension = 'jpg'

            file_path = di + '/'
            img_order = self.db.is_duplication('clothes_image', 'product_id', product_id) + 1
            file_name = f'{str(img_order).zfill(3)}.{extension}'
            abs_path = file_path + file_name
            img_val = [product_id, img_src, file_path, file_name, extension]

            # DB 에 집어 넣어. 유니크키 중복나면 알아서 안 들어가니깐
            self.db.db_insert('clothes_image', img_col, img_val)
            # 이미지 파일도 저장
            print('Save images')
            # 폴더 만들기 <$$$> 이 부분 조작하면 된다
            pi.mkdir_img(di)
            pi.down_img(img_src, abs_path)
        except:
            pass
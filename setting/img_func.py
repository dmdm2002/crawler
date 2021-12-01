import os
import urllib.request
import urllib.error
from setting.database import DBset

def mkdir_img(dir):
    try:                           #해당 이름을 가진 폴더가 없으면 생성
        if not(os.path.isdir(dir)):
            os.makedirs(os.path.join(dir))
    except OSError :
        print("Failed to create dir")
        raise

def down_img(img_src, path): #path_name = 저장 경로, 파일이름
    ret = 0
    try:
        urllib.request.urlretrieve(img_src, path)
    except urllib.error.HTTPError:
        print("Http error")
        ret = -1
    except:
        pass
    return ret
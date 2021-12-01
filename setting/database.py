import pymysql
from pymysql import IntegrityError
from pymysql import DataError
import pandas as pd
import re

class DBset(object) :
    #db생성자
    def __init__(self,db_name: object) -> object :
        self.db_name = db_name
        return

    #db 연결
    def db_connect(self):
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='vnttkrhk15!', db = self.db_name,charset='utf8')
        return db


    def db_coursor(self, sql):
        db = self.db_connect()
        print(sql)
        try:
            with db.cursor() as cursor:
                cursor.execute(sql) #db가져와서 데이터 프레임으로 변환
                print(sql)
                fetch = cursor.fetchall() #db 조회(select)
            db.commit()
        finally:
            db.close()
        return fetch

        # 중복데이터 확인
    def is_duplication(self, table_name, col, val):
        sql = f'SELECT * FROM {self.db_name}.{table_name} where {col} = {repr(val)};'
        fetch = self.db_coursor(sql)
        return len(fetch)


    def db_get(self, need_col,table_name, where_col,value ):
        #select 데이터 from 위치 where 조건
        sql = f'SELECT {need_col} FROM {table_name} WHERE {where_col} = {repr(value)};'
        #db로 부터 정보 가져오기
        fetch = self.db_coursor(sql)
        if len(fetch) == 0:
            return None
        return fetch[0][0]

    def db_insert(self,table_name,col,val):
        db = self.db_connect()

        # col, val 을 sql문에 넣기위해 스트링으로 만들어준다
        col_str = re.compile('\'').sub('', repr(tuple(col)))
        val_str = re.compile("'NULL'").sub("NULL", repr(tuple(val)))
        print(col_str)
        if len(col) == 1:
            col_str = re.compile(',(?=\\))').sub('', col_str)
            val_str = re.compile(',(?=\\))').sub('', val_str)

        sql = f'INSERT INTO {table_name} {col_str} VALUES {val_str};'
        sql2 = 'SELECT LAST_INSERT_ID();'
        print(sql)

        try:
            with db.cursor() as cursor:
                cursor.execute(sql)
                cursor.execute(sql2)
                f = cursor.fetchone()
            db.commit()
        except IntegrityError:  # code 가 같은 경우 : 코드를 유니크키 설정해놓으면 이런 에러가 난다
            print(f'{table_name}으로 insert: 유니크키 중복 or 외래키 검사 실패')
            return -1
        finally:
            db.close()
        return f[0]

    #db업데이트
    def db_update(self,table_name,up_col,up_val,where_col,where_val):
        if up_val is None:
            up_val = 'NULL'
        else :
            up_val = repr(up_val)
        sql = f'UPDATE {table_name} SET {up_col} = {up_val} WHERE {where_col}={repr(where_val)};'
        self.db_coursor(sql)
        return
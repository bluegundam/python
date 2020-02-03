import pandas as pd
from datetime import datetime
import os

import pymysql
from sqlalchemy import create_engine

def insert_db(target_file_full_path):
    #log_file = 'D:/1.업무/2019 ~/004.보안/005.nginx_accesslog_tls/access_sample.log'
    # log_file = 'D:/1.업무/2019 ~/004.보안/005.nginx_accesslog_tls/access.log.2020-01-27'
    log_file = target_file_full_path

    print("File To DataFrame 생성 시작")
    data = pd.read_csv(log_file,
                sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
                engine='python',
                usecols=[0, 3, 4, 5, 6, 7, 8, 9],
                names=['ip', 'time', 'request', 'raw_protocol','status', 'size', 'referer', 'user_agent'],
                na_values='-',
                header=None
                    )

    print("File To DataFrame 생성 종료")

    list_raw = data['raw_protocol'].values.tolist()
    
    print("raw protocol 가공 시작")

    list_protocol = []
    list_cipher = []

    for item in list_raw:
        tmp = item.split('/')
        list_protocol.append(tmp[0])
        list_cipher.append(tmp[1])

    print("raw protocol 가공 종료")

    data["protocol"] = list_protocol
    data["cipher"] = list_cipher

    print("DataFrame에 컬럼 추가 종료")

    # print(data.head)

    pymysql.install_as_MySQLdb()

    engine = create_engine("mysql://root:passwd@localhost/***")
    data.to_sql(name = 'access_log', con = engine, if_exists='append', index=False)

    print("DB 저장 종료")


def split_test():
    str = 'TLSv1.2/ECDHE-RSA-AES128-SHA256'
    sp_str = str.split('/')
    print(sp_str)

def list_dir(path):
    path_dir = path

    file_list = os.listdir(path_dir)

    # print(file_list.sort())
    # print(file_list)

    return file_list

#split_test()
# insert_db()
path = "D:/1.업무/2019 ~/004.보안/005.nginx_accesslog_tls/127.0.0.1/"
# path = "D:/1.업무/2019 ~/004.보안"

items = list_dir(path)
items.sort()

for item in items:
    print('{} 진행'.format(path+item))
    insert_db(path+item)
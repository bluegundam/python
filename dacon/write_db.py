import pandas as pd
from datetime import datetime

# data = pd.read_csv('E:/GitHub/python/dacon/data/train_2002_result_20200106_230851.csv', encoding = 'ms949')
data = pd.read_csv('E:/GitHub/python/dacon/data/train_2002_result_20200106_234537.csv', encoding = 'UTF-8')

print(data)

print('start_time : ' + str(datetime.today())[:19])

import pymysql
from sqlalchemy import create_engine

pymysql.install_as_MySQLdb()

engine = create_engine("mysql://root:qkdtlf1003@localhost/dacon")
data.to_sql(name = 'pandas_data', con = engine, if_exists='append', index=False)

print('end_time : ' + str(datetime.today())[:19])
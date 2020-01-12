
#######################################

import pandas as pd
target_file_path = "dacon/data/predict_gcp_10.csv"

df1 = pd.read_csv(target_file_path, encoding = 'MS949')

print('행수 : ', len(df1))
print('열수 : ', len(df1.columns))

##########################################

import convert_util as cu

value = 0.9999091625213623
print(cu.convE2Float(value))

value = '0.9999091625213623'
print(cu.convE2Float(value))

value = 1.1843565062008565e-06
print(cu.convE2Float(value))

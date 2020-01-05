import pandas as pd
from datetime import datetime
import math

start_time = datetime.today().strftime("%Y%m%d_%H%M%S")

filter_file_path = "dacon/data/filter.csv" 
# target_file_path = "dacon/data/train_2002.csv"
# result_file_path = f"dacon/data/train_2002_result_{start_time}.csv"

target_file_path = "dacon/data/train-UTF_bangsil.csv"
result_file_path = f"dacon/data/train-UTF_bangsil_{start_time}.csv"

df1 = pd.read_csv(filter_file_path, encoding = 'UTF-8')
pattern_data = df1['FILTER']


# print(pettern_data['FILTER'].loc[0])

### 1. 필터 CSV 읽어 필터컬럼 정보 읽어오기
# idx = 0
# for pattern_item in pattern_data['FILTER']:
#     print(idx, ' | ',  pattern_item)
#     idx = idx + 1 


###2.  타겟 CSV 파일을 읽어오기
target_data = pd.read_csv(target_file_path)
target_text = target_data['text']

# idx = 0
# for target_item in target_data['text']:
#     print(idx, ' | ', target_item)
#     idx = idx + 1

target_idx = 0
for target_item in target_text :

    match_yn = False
    match_cnt = 0
    match_word = ''

    # print(target_item)
    # print(pd.isnull(target_item))

    if (pd.isnull(target_item)) != True:
        for pattern_item in pattern_data :
            # print(target_item)
            # print(pattern_item)

            if pattern_item in target_item :
                match_yn = True
                match_cnt = match_cnt + 1
                if len(match_word) == 0 : 
                    match_word = pattern_item
                else :
                    match_word = match_word + ', ' + pattern_item

    if match_yn == True:
        target_data['match_yn'].loc[target_idx] = 1
        target_data['match_cnt'].loc[target_idx] = match_cnt
        target_data['match_word'].loc[target_idx] = match_word

    else :
        target_data['match_yn'].loc[target_idx] = 0
        target_data['match_cnt'].loc[target_idx] = 0
        target_data['match_word'].loc[target_idx] = ''

        # print(f'row {target_idx} no match')
    
    target_idx = target_idx + 1

    if (target_idx % 100) == 0:
        print(f'processing : {target_idx}')

# print(target_data.loc[:,['text', 'smishing', 'filter match yn' , 'match word']])


### 3. 특정 컬럼 정보 수정
# print(target_data['filter match yn'].loc[0])
# print(target_data['match word'].loc[0] )

# target_data['filter match yn'].loc[0] = 'manli'
# target_data['match word'].loc[0] = 'hong'

# print(target_data)


fw_time = datetime.today().strftime("%Y%m%d_%H%M%S")
### 4. CSV 파일로 쓰기

# target_data.to_csv(result_file_path, encoding = 'UTF-8')
target_data.to_csv(result_file_path, encoding = 'ms949')
###

end_time = datetime.today().strftime("%Y%m%d_%H%M%S")

print(f'시작시간 : {start_time}')
print(f'기록시간 : {fw_time}')
print(f'종료시간 : {end_time}')
print("End")





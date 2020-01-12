import pandas as pd
from datetime import datetime
import math
from req_gcp_sample import get_prediction_text as predict_gcp
from convert_util import convE2Float as etof

<<<<<<< HEAD
=======
#api key : 
>>>>>>> b8165b545d7d4a14c95aeae70731a2cc743f7582

start_time = datetime.today().strftime("%Y%m%d_%H%M%S")
start_time2 = datetime.now()


# target_file_path = "dacon/data/predict_gcp_10.csv"
# result_file_path = f"dacon/data/predict_gcp_10_result_{start_time}.csv"

target_file_path = "dacon/data/predict_gcp_full.csv"
result_file_path = f"dacon/data/predict_gcp_full_result_10000_{start_time}.csv"

gcp_model_2000  = "projects/724413311684/locations/us-central1/models/TCN7180158375051657216"
gcp_model_10000 = "projects/724413311684/locations/us-central1/models/TCN4545974805504983040"
gcp_model_full  = "projects/724413311684/locations/us-central1/models/TCN2523858572815630336"

df1 = pd.read_csv(target_file_path, encoding='MS949')

total_cnt = len(df1)

# print(df1['id'])
# print(df1['year_month'])
# print(df1['text'])

idx = 0
df1['predict_model_2000_0'] = 'Nan'
df1['predict_model_2000_1'] = 'Nan'
df1['predict_model_10000_0'] = 'Nan'
df1['predict_model_10000_1'] = 'Nan'
df1['predict_model_full_0'] = 'Nan'
df1['predict_model_full_1'] = 'Nan'

for content in df1['text']:
  # print(content)

  if pd.isnull(content) != True:
    
    if idx > 0:
      progress = (idx / total_cnt) * 100
      processing_time = datetime.now()
      print("진행율 : ", round(progress),'%', " idx : ", idx ," total : " , total_cnt, '진행시간 : ', processing_time - start_time2)


    # ### GCP 판정모델 1 호출  
    # response = predict_gcp(content, gcp_model_2000)

    # for result in response.payload:
    #   # print("Predicted class name: {}".format(result.display_name))
    #   # print("Predicted class score: {}".format(result.classification.score))

    #   if result.display_name == '0':
    #     # df1['predict_model_2000_0'].loc[idx] = 0.001 + idx
    #     df1['predict_model_2000_0'].loc[idx] = etof(result.classification.score)

    #   elif result.display_name == '1':
    #     # df1['predict_model_2000_1'].loc[idx] = 0.002 + idx
    #     df1['predict_model_2000_1'].loc[idx] = etof(result.classification.score)

    # ### GCP 판정모델 2 호출

    # # df1['predict_model_10000_0'].loc[idx] = 0.03 + idx
    # # df1['predict_model_10000_1'].loc[idx] = 0.04 + idx

    # response = predict_gcp(content, gcp_model_10000)

    # for result in response.payload:
    #   # print("Predicted class name: {}".format(result.display_name))
    #   # print("Predicted class score: {}".format(result.classification.score))

    #   if result.display_name == '0':
    #     df1['predict_model_10000_0'].loc[idx] = etof(result.classification.score)

    #   elif result.display_name == '1':
    #     df1['predict_model_10000_1'].loc[idx] = etof(result.classification.score)

    ### GCP 판정모델 3 호출

    # df1['predict_model_full_0'].loc[idx] = 0.5 + idx
    # df1['predict_model_full_1'].loc[idx] = 0.6 + idx

    response = predict_gcp(content, gcp_model_full)

    for result in response.payload:
      # print("Predicted class name: {}".format(result.display_name))
      # print("Predicted class score: {}".format(result.classification.score))

      if result.display_name == '0':
        df1['predict_model_full_0'].loc[idx] = etof(result.classification.score)

      elif result.display_name == '1':
        df1['predict_model_full_1'].loc[idx] = etof(result.classification.score)
  idx = idx + 1


### 결과 CSV 파일 저장
fw_time = datetime.today().strftime("%Y%m%d_%H%M%S")

df1.to_csv(result_file_path, encoding = 'MS949')

end_time = datetime.today().strftime("%Y%m%d_%H%M%S")

print(f'시작시간 : {start_time}')
print(f'기록시간 : {fw_time}')
print(f'종료시간 : {end_time}')
print("End")

df1 = pd.read_csv(result_file_path, encoding='MS949')
print(df1)
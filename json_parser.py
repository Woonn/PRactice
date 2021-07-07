import json # import json module
import os
import glob
from glob import iglob
# import pandas as pd
# with statement

'''
한 영상의 배열의 keypoint를 numpy배열로
shape = (프레임수, keypoint, xyconfidence)
'''

# 경로의 모든 파일 불러오기
data_path = 'C:\\python\\KDT\\keypoint\\NIA_SL_SEN0001_REAL01_D'# 윈도우 경로
# path = os.getenv("HOME")+"/hdata/morpheme"

#재귀적으로 하위의 모든 파일 불러오기
# for filename in glob.iglob('**/*.json', recursive=True):
#     print(filename)

files = glob.glob(data_path+'\\*.json')
# prin
# t(files)
for idx, file in enumerate(files[:3]):
    with open(file) as json_file:
        json_data = json.load(json_file)# 파일명으로 하나 불러와서
    # 단어 뽑기
    # print('\n', json_data['data'])
    for part in json_data['people']:
        li = []
        print(part)
        print(json_data['people'][part])


        # li.append(part)
        # print(li)
        # for i in li:
        #     for confidence in part[i]:
            #     print(confidence)

                

            # print(word['name'])
    # print(file, word['name'])
    # df['filename'][idx] = file
    # df['word'][idx] = word['name']




# print(json_data)




# cnt = 0
# for i in glob.iglob(path+"/*.json"):
#     cnt+=1
# print(cnt)



#파일명, 레이블 csv
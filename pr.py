import json # import json module
import os
import glob
from glob import iglob
import pandas as pd
# with statement

path = os.getenv("HOME")+"/hdata/morpheme"
files = glob.glob(path+'/*.json')
df = pd.DataFrame(columns = ['filename', 'word'])

for idx, file in enumerate(files[:3]):
    with open(file) as json_file:
        json_data = json.load(json_file)# 파일명으로 하나 불러와서
    # 단어 뽑기
    # print('\n', json_data['data'])
    for val in json_data['data']:
        for word in val['attributes']:
            print(word['name'])
    print(file, word['name'])
    df['filename'][idx] = file
    df['word'][idx] = word['name']


fin_data = 

to_csv(fin_data)


# print(json_data)




# cnt = 0
# for i in glob.iglob(path+"/*.json"):
#     cnt+=1
# print(cnt)



#파일명, 레이블 csv
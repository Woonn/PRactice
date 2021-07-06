'''
sentence generate
1. 단어를 받아서 형태소 파악
2. 해당 형태소를 일반적인 한글의 위치로 정렬
3. 적절한 조사를 사용하여 문장 생성
'''

'''
matching system
1. 단어를 입력으로 받아서
2. 대응되는 문장을 출력
'''

input = ["나", "밥", "먹다"]

# 형태소 분석 실시()
morp = ["S", "O", "V"]
tags = ['S', 'H', 'O', 'V', 'NN', "JF"]# mecab.morphs(input)
print(len(tags))
# 위치 지정
result = [0]*len(tags)


print(result)
for tag in tags:
    if tag in morp: #해당 위치의 태그가 존재하면
        if tag == "S":
            result[0] = tag
        elif tag == "O":
            result[1] = tag
        elif tag == "V":
            result[2] = tag
        else:
            print("규격외")
            result.pop()
         #   continue
print(result)
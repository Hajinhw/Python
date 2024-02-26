# with 문
# with open(파일명, 모드) as 파일객체:
#     수행문장들

# with open('data/study_data2.txt', 'r') as f:
    # text = f.read()
    # print(text)

# with open('data/file1.txt', 'a', encoding='utf-8') as f:
    # f.write(text)

# scores.txt : 공백으로 구분한 데이터 파일
with open('data/scores.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    print(data)


# scores2.txt : ,으로 구분한 데이터 파일
with open('data/scores2.txt', 'r', encoding='utf-8') as f:
    data2 = f.readlines()
    print(data2)

print(len(data2))

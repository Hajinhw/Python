# 텍스트파일 읽기 : read(), readline(), readlines(), seek()

# 텍스트파일 생성 : 메모장을 이용해서
# study_data.txt : 한글
# study_data.txt2 : 영문

# 1단계 : 파일 열기 (open)
# f = open('study_data.txt', 'r', encoding='utf-8')
# 오류 : UnicodeDecodeError: 'cp949' codec

f = open('data/study_data3.txt', 'r')

# 2단계 : 파일처리(읽기)
# text = f.read()
# text = f.readline()
# print(text)
# text2 = f.readline()
# print(text2)

# while True:
    # text = f.readline()
    # if not text:
        # break
    # print(text)

# print(f.readlines())
# for textline in f.readlines():
    # print(textline, end='')

for textline in f:
    print(textline, end='')

# 3단계 : 파일 닫기(close)
f.close()

# 영문으로 된 텍스트파일 읽기
# f1 = open('study_data2.txt', 'r')
# text = f1.read()
# print(text)
# f1.close()


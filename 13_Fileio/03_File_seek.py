# seek(offset, whence) : 내 탐색 위치 지정

print('파일 내에서 검색 : seek() ----')
f = open('data/seek_test_data.txt', 'r', encoding='utf-8')

# f.seek(0,0)    # 시작위치 : 0 (파일 처음)
# lines = f.readlines()
# print(lines)

f.seek(7,0)    # 시작위치 : 7
lines = f.readlines()
print(lines)

f.seek(16,0)    # 시작위치 : 16   # utf-8은 3바이트
lines = f.readlines()
print(lines)

f.close()

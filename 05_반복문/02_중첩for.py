# 다중 for를 이용

for x in range(3):
    for y in range(1, 5):
        print(y+4*x, end=' ')
    print()

# 2~9단 구구단 출력

for dan in range(2,10):
    for n in range(1,10):
        print(f'{dan}*{n}={dan*n:>2}') # 자리 정렬 맞춤
    print()

# 2차원 튜플 생성

t = ((1,2,3), (4,5,6), (7,8,9))
print(t)

# 2차원 튜플의 요소를 행렬의 테이블 형식으로 출력
for i in t:
    for x in i:
        print(x, end = ' ')
    print()

# t[0][1]

for i in range(len(t)):
    lt1,lt2,lt3=t[i]
    print(lt1,lt2,lt3)
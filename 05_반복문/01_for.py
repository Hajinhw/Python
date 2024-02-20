# 반복문 for

# 1~10 사이의 정수를 더하기
'''
total = 0
total = total + 1
total = total + 2
total = total + 3
...
total = total + 10


total = 0
for num in range(1, 11):
    total = total + num

print(total)


# 1부터 10사이의 홀수 더하기

total = 0
for num in range(1,11,2):
    total = total + num

print(total)


# 값을 시작값, 끝값을 입력받아 이 사이에 있는 정수 더하기


ins1 = int(input('시작값 : '))
ins2 = int(input('끝값 : '))

total = 0

for num in range(ins1, ins2+1):
    total = total + num

print(total)
'''

# 합격 >=60, 불합격 <60 . 5명의 점수 입력받아 출력.

for _ in range(5):
    jumsu = int(input('0~100사이 점수입력 : '))
    if jumsu >= 60:
        print(f'{jumsu} 합격')
    else:
        print(f'{jumsu} 불합격')

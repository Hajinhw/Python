# 1부터 100 사이의 숫자 출력
'''
num = 1
while num <= 100:
    print(num, end=',')
    num += 1

print('------------------------')
# 1부터 100 사이 3의 배수들의 합

total = 0
for num in range(3, 101, 3):
    total += num
print('1~100사이의 3의 배수 합: ', total)

print('------------------------')

total = 0
num = 3
while num <= 100:
    if num % 3 == 0:
        total += num
    num += 1
print('1~100사이의 3의 배수 합 : ', total)

print('------------------------')

total = 0
num = 3
while num <= 100:
    total += num
    num += 3
print('1~100사이의 3의 배수 합 : ', total)

print('------------------------')

# 7을 입력할 때까지 계속 입력하는 프로그램

num = int(input('숫자 입력 : '))

while num != 7:
    num = int(input('다시 입력 : '))
print('7 입력! 종료')
'''
# 연습문제 if 1번 문제 : 십진수를 이진수로

dec = int(input('십진수 입력 : '))
bin_ = ' '
while dec > 0:
    r = dec % 2
    dec = dec // 2
    bin_ = str(r) + bin_
print('0b' + bin_)
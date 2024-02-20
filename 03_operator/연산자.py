# 연산자

# 1. 산술연산자 : +, -. *, /, %, //, **

# divmod(x, y) : x를 y로 나눈 몫과 나머지 반환

# 문제 1. 10000초는 몇시간 몇분 몇초인가?

time = 10000
hours = time //3600
temp = time % 3600
minutes = temp // 60
seconds = temp % 60
print(f'{time}초는 {hours}시간 {minutes}분 {seconds}초입니다.')

# 2. 관계 연산자 : > < >= <= == !=

a = 100
b = 5

print(f'{a}=={b}의 결과는 {a == b}')
print(f'{a}=={b}의 결과는 {a != b}')
print(f'{a}=={b}의 결과는 {a > b}')

# 3. 논리 연산자 : and or not

print ( a > 200 and a < 300 )
print ( not(a>200))

# 4. 비트 연산자 : $ | ^ ~ << >>

print(f'~{a} : {~a}')
print(f'{b}<<1 : {b<<1}')
print(f'{b}<<3 : {b<<3}')
print(f'{b}>>1 : {b>>1}')
print(f'{b}>>2 : {b>>2}')

# 대입연산자 : += -= *= /= //= %=
print('a=',a)
a+=10
print('a+=10 :', a)

# 실습문제 1. 지폐교환기

m = int(input('지폐로 교환할 돈은 얼마?'))
a = m // 50000
m %= 50000
print(f'50000원짜리 => {a}장')
b = m // 10000
m %= 10000
print(f'10000원짜리 => {b}장')
c = m // 5000
m %= 5000
print(f'5000원짜리 => {c}장')
d = m // 1000
m %= 1000
print(f'10000원짜리 => {d}장')
print(f'지폐로 바꾸지 못한 돈 => {m}원')

# 함수
# 재사용 / 자주 사용하는 기능들을 위한 코드 집합
# 경제적, 관리 용이
# 내장함수(built-in function) / 사용자 정의 함수

# 함수 정의 및 호출
'''
# 이름, 나이, 연락처 출력하는 함수 show_info()
def show_info():
    print('이름 : 홍길동')
    print('나이 : 20')
    print('연락처 : 010-1111-1111')

show_info()

def show_info1():
    name = input('이름 입력 : ')
    age = input('나이 입력 : ')
    phone = input('연락처 입력 : ')
    print(f'이름 : {name}')
    print(f'나이 : {age}')
    print(f'연락처 : {phone}')

show_info1()

# 문제. 두 정수를 입력받아 더하고 그 결과를 출력하는 함수 add() 정의하기

def add():
    num1 = int(input('숫자 입력1 : '))
    num2 = int(input('숫자 입력2 : '))
    sum = num1 + num2
    print(f'두 숫자의 합은 {sum}입니다.')

result = add()
print(result)
'''
# 반환값이 있는 함수 정의

def add2():
    num1 = int(input('숫자 입력1 : '))
    num2 = int(input('숫자 입력2 : '))
    sum = num1 + num2
    print(f'두 숫자의 합은 {sum}입니다.')
    return sum

result = add2()
print(result)
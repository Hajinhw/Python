# 함수의 매개변수(parameter)와 인수(argument)

# 함수로 전달되는 값을 갖는 변수

# 매개변수 : 함수를 정의할 때 함수로 전달되는 값을 갖는 변수
# 인수 : 함수를 호출할때 전달되는 값
'''
def get_area(width, height):
    result = width * height
    print(f'사각형 가로={width}, 세로={height}, 면적은 {result}')
    return result

print(get_area(10,20))

# 문제. 사칙연산을 수행하는 함수 정의
# add(a,b) : 두 수 더하기
# sub(a,b) : 뺄셈
# mul(a,b) : 곱셈
# div(a,b) : 나눗셈

def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    if num2 is 0:
        print('0으로 나눌 수 없습니다.')
    else:
        return num1 / num2


a = 2
b = 3
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
'''
# 디폴트 매개변수
# 매개변수의 기본값이 지정되어 있는 경우
# 디폴트 매개변수는 마지막에 있어야 함. 앞에서 설정 불가

def greet(name, msg='Hello'):
    print(name + ',' + msg)

greet('홍길동','hi')
greet('홍길동')
#  TypeError: greet() missing 1 required positional argument: 'msg'

# 위치 매개변수(positional parameter)
# 매개변수의 위치가 실인수로 전달받을 때 동일한 위치의 변수에 저장됨

# 함수에 여러 개의 자료(리스트,딕서녀리 등) 전달
def show_names(names):
    for name in names:
        print(name, end=' ')
show_names(['홍길동', '심청이','강감찬'])
print()
def show_info(info):
    print(info)
    for n in info.keys():
        print(info[n])

info = {'이름':'홍길동','나이':20}
show_info(info)

# 가변길이 매개변수
# 매개변수의 길이가 정해지지 않는 경우 여러개의 값을 전달 받을 때 사용
# *args 또는 **kwargs=> key=value

print('hi','ho', end=' ')

# *args 매개변수
def my_sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(my_sum(1,2))
print(my_sum(1,2,3))

# **kewargs 매개변수
def show_info(**kewargs):
    for key in kewargs.keys():
        print(key, end=' ')
    for value in kewargs.values():
        print(value, end=' ')

show_info(id='abc',name='hong')

# 키워드 인수(keyword arguments)
# 인수들 앞에 키워드를 두어서 인수를 구별
# 인수의 위치가 매개변수의 위치와 달라도 됨
def my_print(a,b,c):
    print(a)
    print(b)
    print(c)

my_print(10,30,40)
my_print(a=5, c=10, b=30)

# *args는 **kwargs 앞에 반드시 와야 함

# 위치인수와 키워드인수를 함께 사용하는 경우 키워드 인수가 위치 인수 뒤로
# 함수정의 : 위치 매개변수 뒤에 디폴트 매개변수 위치
# 지역변수(local variable)와 전역변수(global variable)
# 지역변수 : 함수 내부에서 정의된 변수, 함수 안에서만 사용 가능
#          함수 호출 시 생성되고, 함수 종료되면 소멸되어 더 이상 사용불가


a = 10
print(a)

def show_info(name):
    age = 10
    print(name,age)

show_info('age')

def show():
    a = 1        # 지역변수
    a = a+ 1
    print(f'지역변수 a : {a}', id(a))


show()
print(f'전역변수 a : {a}', id(a))

def show1():
    a = a+ 1     # 지역변수를 찾음 : 오류발생
    print(f'지역변수 a : {a}', id(a))


def show2():
    b = a+1      # a : 전역변수 사용
    print(f'지역변수 a : {a}', id(a))


def show3():
    global a      # 전역변수 사용
    a = a + 1
    print(f'지역변수 a : {a}', id(a))

# 지역변수명과 전역변수명이 같은 경우 지역변수가 우선한다.


def sub(x,y):
    global b
    a = 7
    x,y=y,x
    b=3
    print(a,b,x,y)

a,b,x,y = 1,2,3,4
sub(x,y)
print(a,b,x,y)

def show_list(my_list):
    cpy_list = my_list.copy()
    cpy_list[-1] = 100
    print(cpy_list, id(cpy_list))

my_list = [1,2,3,4]
show_list(my_list)
print(my_list, id(my_list))
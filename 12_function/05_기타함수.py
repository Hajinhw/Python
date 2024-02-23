# 재귀함수(recursive function)
# 함수 내부에서 자신의 함수로 다시 호출

# 1~n 까지의 합을 계산하는 재귀함수
def my_sum(n):
    if n == 1:
        return 1
    return n + my_sum(n-1)

print(my_sum(10))

# 1*2*3.....*n : n! 계산하는 재귀함수

def my_fact1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def my_fact2(n):
    if n <= 1:
        return 1
    return n * my_fact2(n-1)

print(my_fact1(5))
print(my_fact2(5))

# 내부함수

def outfunc(x,y):
    def infunc(a,b):
        return a+b
    return infunc(x,y)

print(outfunc(10,30))

# 람다(lambda) 함수
# 한줄짜리 함수, return문을 사용하지 않음
# 변수명 = lambda <인수들>:<반환할 식>
# 람다함수는 함수 참조를 반환
# 변수로 람다함수 객체를 받아서 함수 호출

f = lambda:1
print(f())

f = lambda x,y:x+y
print(f(2,3))

f = lambda x,y=30:x+y
print(f(10))
print(f(10,50))
print(f(y=10,x=500))

# 람다 표현식 : 함수 이름을 명명하지 않고(변수에 할당하지 않고) 바로 호출
# (lambda <매개변수들> : 식) (인수들)

print((lambda x : x+10)(10))

# 람다표현식 안에서는 변수 생성 불가
# (lambda x : y=10; x+y)(10)

def plus_ten(x):
    return x + 10

lambda x:x+10

# [1,2,3,4,5] + 10
new = []
for n in [1,2,3,4,5]:
    new.append(n+10)
print(new)

print(list(map(plus_ten, [1,2,3,4,5])))
print(list(map(lambda x:x+10, [1,2,3,4,5])))

# 두 개의 리스트 요소 더하기

def add_list(x,y):
    new_list = []
    for i in range(len(x)):
        new_list.append(x[i]+y[i])
    return new_list

a = [1,2,3,4]
b = [10,11,12,13]
print(add_list(a,b))

# map(func, iterable data) 함수
def add_two(x,y):
    return x+y
print(list(map(add_two, a, b)))
print(list(map(lambda x,y:x+y, a, b)))
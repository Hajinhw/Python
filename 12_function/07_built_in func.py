# 내장함수들

# abs() : 절대값
print(abs(-10))

# all(iterable) : 모두 True인 경우 True
# any(iterable) : 하나라도 True인 경우 True
print(all([0,1,2,3]))
print(any([1,0,'',[]]))

# chr(), ord() : 아스키 코드값
print(chr(65))
print(ord('A'))

# divmod(), pow()
# min(), max()
print(max([1,2,3,4,-10]))
print(min([1,2,3,4,-10]))
print(sum([1,2,3,4,-10]))

# round(number, ndigits) : 반올림
print(round(3.141592712345))
print(round(3.141592712345, 2))

# enumerate() : 인덱스값을 포함한 enumerate 객체 반환
print(list(enumerate(['kim','lee','choi'])))
data = ['kim','lee','choi']

for item in enumerate(data):
    print(item)
for idx,value in enumerate(data):
    print(idx,value)

for idx,value in enumerate('Hello world!'):
    print(idx,value)

# eval(표현식) : 표현식을 그대로 실행
print(eval('10'))
print(eval('10*10'))
print(eval('10'+'10'))

# filter() : 반복가능한 자료에 어떤 함수를 적용하여 True인 결과만 추출
def positive(x):
    return x>0

print(positive(10))

print(list(map(positive, [1,2,-1,10,-5])))
print(list(filter(positive, [1,2,-1,10,-5])))

def even(x):
    if x % 2==0:
        return x


print(list(filter(even, [1,2,-1,10,-5])))

# help() : 도움말 시스템 호출
# help(print)
# help(filter)
# help(sum)

# int(), float(), str()
# bin(), hex(), oct()
# input(), print()
# zip(), map()
# range()
# len()
# list(), tuple(), dict(), set()
# id(), type()
# lambda
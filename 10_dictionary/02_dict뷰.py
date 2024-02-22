# 뷰(view)
# keys(), values(), items()

d = {'one':1, 'two':2, 'three':3}

# keys() 뷰
keys = d.keys()
print(keys, type(keys))

print(list(keys))

# 키들에 대한 값들을 출력
for key in d.keys():
    print(key, d[key])

# values() 뷰
values = d.values()
print(values, type(values), list(values))
print(len(values))

for value in d.values():
    print(value, end = ',')
print()

# items() 뷰
items = d.items()
print(items, type(items))
print(list(items))

for item in d.items():
    print(item, type(item))

for key, item in d.items():
    print(key, item)

d = {'학번':1000, '이름':'홍길동', '학과':'컴퓨터학과'}

d['연락처'] = '010-1111-1111'
print(d)
d['학과'] = '파이썬학과'
print(d)
del(d['학과'])
print(d)
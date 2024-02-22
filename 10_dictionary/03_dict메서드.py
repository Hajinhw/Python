# 1. get() 메서드
d = {'one':1, 'two':2, 'three':3}
print(d['two'])

print(d.get('two'))

# print(d['four']) # KeyError발생 : 없는 키 발생
print(d.get('four')) # key가 없는 경우 None 반환
print(d.get('four', 4)) # key가 없는 경우 두번째 인수를 반환

# 2. setdefault() 메서드
print(d)
d.setdefault('two', 22)
d.setdefault('four', 4)
print(d)

# 3. pop(), popitem() 메서드
print(d.popitem())
key, value = d.popitem()
print(key, value)
print(d)

d['six'] = 6
d['ten'] = 10
print(d)

result = d.pop('two')
print(result)
print(d)

# 4. copy() 메서드
d2 = d.copy()
print(d, id(d))
print(d2, id(d2))
d2['four'] = 4
print(d)
print(d2)

# 5. update() 메서드
d3 = {'five':5, 'two':2, 'seven':7}
print(d3)
d3.update(d2)
print(d3)

# 6. clear() 메서드
print(d, id(d))
d.clear()
print(d, id(d))

print(d2, id(d2))
d2 = {}
print(d2, id(d2))
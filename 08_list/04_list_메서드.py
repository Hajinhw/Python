# 리스트 메서드 (함수)
'''
# 1. append() : 리스트 맨 뒤에 항목을 추가
a = []
a.append('apple')
a.append('hotdog')
print(f'alist : {a}')

# 2. pop([index=-1]) : 리스트의 맨 마지막 요소를 추출하고 요소를 제거(꺼내다)
value = a.pop()
print(f'alist : pop 적용 {a}, value = {value}')
a.append('melon')

# 3. sort() : 리스트의 요소들을 정렬하여 정렬된 리스트로 변경
b = [6, 3, 5, 1, -3]
print(f'blist: {b}')
b.sort()
print(f'sort 적용 후 : {b}')

# 3.1. sort(key=str.lower)
char = ['b', 'B', 'A', 'a', 'z']
print(f'charList: {char}')
char.sort()
print(f'charList sort() 적용 후 : {char}')
char.sort(key=str.lower)
print(f'charList sort() 적용 후 : {char}')

# 4. reverse() : 리스트를 역순으로 변경
b.reverse()
print(f'reverse 적용 후 : {b}')

# 5. index() : 리스트에서 지정한 값의 위치를 반환. 값이 없는 경우 ValueError 발생
c = ['홍길동', '강감찬', '성춘향', '변학도']
idx = c.index('강감찬')
print(f'{idx}')

# 6. insert(위치, 값) : 리스트에 값(요소) 삽입
c.insert(-1, '원빈')
print(f'insert 후 {c}')
c.insert(2, '피카소')
print(f'insert 후 {c}')

# 7. remove(값) : 지정한 값을 리스트에서 제거. 첫번째 값만 제거
c.remove('강감찬')
print(f'c.remove("강감찬") 후 : {c}')

# 8. count(값) : 리스트에서 지정한 값의 개수 반환
# for i in range(c.count('강감찬')):
#   c.remove()

# 9. extend() : 리스트에 리스트를 추가(확장) => 하나의 리스트로 변경
print(f'blist : {b}')
b.extend([10,11,12])
print(f'extend([10,11,12]) 적용 후 : {b}')

# 10. sorted() 내장 함수 : 리스트를 정렬한 새로운 리스트를 반환
a = [3, 1, -10, 11, 2]
print(f'alist : {a}')
new_a = sorted(a, reverse=True)
print(f'sorted(a) 함수 적용 후 alist : {a}')
print(f'sorted()로 생성된 {new_a}')

# 11. copy() : 리스트 복사
cpy_a = a.copy()
print(cpy_a)
cpy_a.sort()
print(cpy_a)

# 12. clear() : 리스트를 비우기 (빈 리스트로)
cpy_a.clear()           # cpy_a[:] = [] 동일한 기능
print(cpy_a)

# 13. del() : 리스트 요소 지우기, 리스트 전체 지우기
del cpy_a
# del(cpy_a[3::])
# print(cpy_a) # 메모리에서 제거되기 때문에 오류 발생.

# 14. len() : 리스트의 길이 반환
print(len(b))

# 15. max() : 최대값을 반환하는 내장 함수
# 16. min() : 최소값을 반환하는 내장 함수

ex_list = [100, 7, -2, 99, 30]
ex_list = ['hello', 'Exit', 'Zoo', 'hI', 100, 7, -2, 99, 30]

print(ex_list)
print(f'최대값 {max(ex_list)}')
print(f'최소값 {min(ex_list)}')

# 17. in, not  in 연산자
num = [1,2,3,4,5]
result = 10 in num
print(result)
result = 10 not in num
print(result)
'''
# 18. > < >= <= == != : 리스트 일치 검사
list1 = [1,2,3]
list2 = [5,6,7]
list3 = [1,2,3]

print(list1 < list2)
print(list1 == list3)
print(list1 > list3)

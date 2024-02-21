# 리스트 컴프리헨션
# 새로운 리스트 = [문장 for 변수 in 반복범위 [if 조건식]]

num_list = []
for num in range(1,6):
    num_list.append(num)
print(num_list)

num_list = [num for num in range(1,6)]
print(num_list)

num_list2 = [num*2 for num in range(1,6)]
print(num_list2)

num_list3 = [num*num for num in range(1,6)]
print(num_list3)

# 문제. 1~20의 정수 중 짝수만으로 구성된 리스트 생성

even = [num for num in range(2,21,2)]
print(even)

even = [num for num in range(1,21) if num %2 ==0]
print(even)

# 문제. 1~20의 정수 중 3의 배수로 구성된 리스트 생성

num_list4 = [num for num in range(3,21,3)]
print(num_list4)

num_list4 = [num for num in range(1,21) if num %3 == 0]
print(num_list4)

list1 = [1,2,3,4,10,11,12]
num_list5 = [num for num in list1 if num %3 == 0]
print(num_list5)

foods = ['떡볶이', '짜장면', '라면', '피자']
sides = ['단무지', '김치', '피클']

for food, side in zip(foods, sides):
    print(food,'---',side)


for item in zip(foods, sides):
    print(item)

name = ['홍길동', '강감찬', '성춘향', '방자']
sex = ['남', '남', '여', '남']
addr = ['서울', '한양', '독도', '부산']

print(list(zip(name,sex,addr)))
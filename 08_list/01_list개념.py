# n개의 정수 입력받아 합계와 평균 출력

n = 4
total = 0
num_list = [] # num_list = list()

for i in range(4):
    num = int(input(f'{i+1}번째 숫자입력: '))
    num_list.append(num)
    total += num
avg = total / 4
print(f'합계:{total}, 평균:{avg}')
print('num_list=', num_list)


for num in num_list:
    print(num)

lists = [1,2,3,[1,2,3],[5,6]]
print(lists)
print(lists[0], lists[-1])

# 리스트 생성 : []. list()
# 리스트 요소 추가 : append()
# 리스트 길이 : len(리스트)

# 리스트의 요소 출력
for i in range(len(num_list)):
    print(num_list[i])
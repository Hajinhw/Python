# 1. 리스트 요소 추가 : append(), insert()
'''
name = []

name1 = input('회원 입력 : ')
name.append(name1)
name2 = input('회원 입력 : ')
name.append(name2)
name3 = input('회원 입력 : ')
name.append(name3)

print(name)


name_list = []

for i in range(10):
    name = input('회원 입력 : ')
    name_list.append(name)

print(name_list)


i = 0
while i < 10:
    name = input('회원 입력 : ')
    name_list.append(name)
    i += 1

print(name_list)


# 회원 명단 출력

for name in name_list:
    print(name, end=' ')
print()


# 2. 5명의 성적 입력, 총점, 평균 계산

total = 0
score_list = []

for i in range(1,6):
    score = int(input(f'학생{i} 점수 입력 : '))
    score_list.append(score)

for score in score_list:
    total += score

avg = total / len(score_list)
print(f'총점 : {total}')
print(f'평균 : {avg:.2f}')

cnt = 0
for score in score_list:
    if score >= 80:
        cnt += 1               # 두 for문을 합쳐도 됨.

print(f'80점 이상 학생 : {cnt}명')
'''

# 문제. 4명의 국어,영어,수학 점수 2차원 리스트를 이용하여 학생별 총점과 평균 출력

score_list = [[90,85,70], [88,79,92], [100,100,100], [90,60,70]]

print("---성적표 (점수)---")
for row in score_list:
    print(row)
print()

print("---성적표 (점수,총점,평균)---")
for row in score_list:
    total = 0
    for col in row:
        total += col
    avg = total / len(row)
    print(f'{row}, {total}, {avg:.1f}')
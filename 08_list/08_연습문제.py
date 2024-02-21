
'''
name_list = []
for i in range(3):
    name = input(f'회원 입력 : ')
    name_list.append(name)
print('회원 명단 :',end=" ")
for name in name_list:
    print(name,end = " ")


score_list = []
total = 0
cnt = 0

num = int(input('학생 수 입력 : '))
for i in range(1,num+1):
    std = int(input(f'학생{i} 점수 입력 : '))
    score_list.append(std)

for x in score_list:
    total += x
    if x >= 80:
        cnt += 1
avg = total / num

print(f'총점 : {total}')
print(f'평균 : {avg:.2f}')
print(f'80점 이상 학생 : {cnt}명')


list_a = []
i = 0
while i < 10:
    ins = input('상품 등록 (엔터키 누르면 종료) : ')
    list_a.append(ins)
    i += 1
    if ins == '':
        break
print('등록된 상품 :', end=' ')
for x in list_a:
    print(x, end= ' ')


score_list = []
total = 0
cnt = 0

num = int(input('학생 수 입력 : '))
for i in range(1,num+1):
    std = int(input(f'학생{i} 점수 입력 : '))
    score_list.append(std)

for x in score_list:
    total += x
    if x >= 80:
        cnt += 1
avg = total / num
new_list = sorted(score_list, reverse=True)
print(f'총점 : {total}')
print(f'평균 : {avg:.2f}')
print(f'80점 이상 학생 : {cnt}명')
print(f'점수 내림차순 정렬 : {new_list}')
'''
import random

a = ['개과천선', '구사일생', '군계일학', '무용지물', '동고동락', \
    '유비무환', '입신양명', '괄목상대', '막역지우', '고장난명']
b = ['잘못을 고치고 옳은 길에 들어섬', '죽일 고비를 여러 번 겪으며 살아나다', '평범한 사람 가운데 뛰어난 사람', '아무짝에나 쓸모 없는 것', '고통과 즐거움을 함께 한다', '미리 준비해두면 근심 걱정이 없다', '사회적으로 인정받고 출세하여 이름을 세상에 드날림', '다른 사람의 학식이나 업적이 크게 진보한 것을 말함', '생사를 같이 할 수 있는 친밀한 벗', '상대 없이 혼자서는 어떤 일을 이룰 수 없다']

print('사자성어 맞추기 게임을 시작합니다')
print('----------------------------')

from random import randint
d = int(randint(0,11))
i = 0
while i < 10:
    print(b[d])
    f = input('이말의 사자성어는? : ')
    if a.index(f) == d:
        print('\n맞습니다.. 게임을 종료합니다.')
        break
    else:
        print('\n틀렸습니다...다시 도전 !\n')
        continue




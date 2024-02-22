
'''
students = [
    {'name':'홍길동','korean':87,'math':98,'english':88,'science':95},
    {'name':'이몽룡','korean':92,'math':98,'english':96,'science':98},
    {'name':'성춘향','korean':87,'math':98,'english':88,'science':95},
    {'name':'변학도','korean':87,'math':98,'english':88,'science':95},
    {'name':'박지성','korean':87,'math':98,'english':88,'science':95},
    {'name':'류현진','korean':87,'math':98,'english':88,'science':95}
]

print(f'이름 총점 평균')
for i in students:
     total = i['korean']+i['math']+i['english']+i['science']
     print(i['name'], total, total / 4)

'''

i = 0
word = dict()
while i < 100:
    a = input('영어 단어 등록 (종료는 quit) : ')
    if a == 'quit':
        break
    elif a not in word:
        b= input(f'{a}의 뜻 입력 (종료는 quit) : ')
        word[a] = b
    else:
        print(f'{a}는 이미 등록된 단어입니다.')
        i += 1
print('\n')
while i < 100:
    c = input('검색할 단어 입력 (종료는 quit) : ')
    if c == 'quit':
        print('종료합니다.')
        break
    elif c in word:
        print(f'{c}의 뜻은 {word[c]}입니다.')
    else:
        print(f'{c}는 사전에 없는 단어입니다.')








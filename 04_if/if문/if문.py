# 조건문

# if문
'''
num = int(input('정수입력 : '))
if num > 10:
    print('10보다 크네요')


# if~else문
if num > 10:
    print('10보다 크네요')
else :
    print('10보다 작거나 같아요')


# 연습문제 1. 등록된 아이디와 비번 확인 로그인

id_input = input('아이디 입력 : ')
pw_input = input('비밀번호 입력 : ')


if id_input == 'flower' and pw_input == '1234':
    print('로그인 성공!')
else :
    print('로그인 실패!')


# 중첩 if : if 조건이 만족하는 경우 또 다른 조건에 따라 실행
# if 아래 if 존재

if id_input = 'flower':
    if pw_input = '1234'
    print('로그인 성공!')
    else :
        print('로그인 실패! : 비밀번호가 다릅니다.')
elif pw_input = '1234':
    print('로그인 실패! : 없는 아이디 입니다.')
else :
    print('로그인 실패! : 아이디와 비밀번호가 모두 다릅니다.')
'''

# 점수 입력(0~100)받아서 학점 출력
# 90점 이상 A
# 80점 이상 90점 미만 B
# 70점 이상 80점 미만 C
# 60점 이상 70점 미만 D
# 60 미만 F

scr = int(input('점수 입력:'))

if scr >= 90:
    print("A학점")
elif scr >=80:
    print("B학점")
elif scr >=70:
    print("C학점")
elif scr >=60:
    print("D학점")
else:
    print("F학점")


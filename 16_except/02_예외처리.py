# 예외처리 형식
# try:
#    예외발생가능한 문장들
# except:
#    예외처리
# else:
#    예외발생하지 않는 경우 처리 문장들
# finally:
#    예외발생과 상관없이 항상 처리
'''
try:
    # print(10/0)
    print('나이'+23+'살')
except:
    print('오류발생')


try:
    # print(10/0)
    print('나이'+23+'살')
except Exception:
    print('오류발생')
''' 

# 에러 종류에 따른 구체적인 오류 담당하는 에러클래스를 이용하여 처리
# 에러종류 명시
# 에러메시지 변수를 활용하여 출력 : 에러담당클래스 as 에러변수명
try:
    print(10/0)
    # print('나이'+23+'살')
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다', e)


try:
    num = int(input('숫자 입력 : '))
    print(num)
except ValueError as e:
    print('숫자가 아닙니다', e)
    # pass
else:
    num = num + 10
    print(num)
    print('오류가 없습니다')
finally:
    print('종료-------')
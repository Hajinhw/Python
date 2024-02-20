#
# 1. 문자열 정의

text1 = 'Python is great!'
text2 = 'Yes, it is.'
text3 = "It's not like any other"
text4 = "Don't walk."
text5 = "This is \
contain \
temp"
print(text5)
text6 = '''apple\n
banana
melon
'''
print(text6)
print(text6)

# 2. 문자열 포맷(서식) 지정
# 1) 포맷코드 '%d %f %s %c' % ()
# 2) '문자열 [위치인덱스]'.format(변수)
#    ' {0:.2f} {2:5d} {} '.format()
# 3) format(변수, '서식') : format(bmi, '.2f')
# 4) f'string : f'{변수} {변수:서식}'

# 3. 날짜 출력 포맷
# 주민번호 / 전화번호 / 우편번호 / 시간 / 날짜

# 모듈(module) : 함수나 변수를 모아놓은 파일
from datetime import date, datetime, timedelta

today = date.today()
print(today, type(today))
print(f'{today.year}년 {today.month}월 {today.day}일')
print(type(today.year))

# method : 메서드, field : 객체의 변수
curr_time = datetime.now().time()
print(curr_time, type(curr_time))
print(curr_time.hour, curr_time.minute, curr_time.second)

# timedelta() : 날짜 계산
print(today + timedelta(days=-1))
print(today + timedelta(weeks=1))

curr_datetime = datetime.now()
print(curr_datetime + timedelta(hours=-1))
print(curr_datetime + timedelta(days=2, hours=4))

# strftime() : 날짜, 시간 형식 지정
print(today.strftime('%Y-%m-%d %H:%M:%S'))

# 4. 문자열 정렬
# 왼쪽정렬 : <
# 오른쪽정렬 : >
# 가운데정렬 : ^
# 공백문자 지정 : -

text = 'Python is great!'

print('{0:<20}'.format(text), 'end')
print(f'{text:>20}')
print(f'{text:^20}')
print(f'{text:-^20}')
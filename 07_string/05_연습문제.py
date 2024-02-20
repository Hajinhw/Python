fact = 'Python is funny'
print(str(fact.count('n') + fact.find('n') + fact.rfind('n')))

text1 = 'Python is a programming language'
text2 = 'and integrate systems more effectively'
text1.lower()
print(text1[:7] + text2.split()[-1] + text1[-9:])

text = 'Python is a programming language'
temp = ''
for i in text.split():
    print(i)
    if i == 'language':
        temp = i.upper() + ' ' + temp
    else:
        temp = i + ' ' + temp
print(temp)

print('{0:>10s}'.format('python'))



x = 'PytHON'
print(x.upper())

from datetime import date

'''
d = input('날짜(연/월/일) 입력 : ')
year = d[:4]
month = d[5:7]
day = d[8:10]
plus = int(year) + 10
print(f'입력한 날짜의 10년 후 => {plus}년{month}월{day}일')
'''
num = input('숫자를 여러개 입력하세요 : ')
for i in num:
    print('\u2665' * int(i))

'''
print('\u2665' * int(num[0]))
print('\u2665' * int(num[1]))
'''
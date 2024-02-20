# 문자열의 모든 글자 뒤에 $를 붙여서 출력하기
'''
s = '파이썬짱!'

temp = ''
for ch in s:
    temp = temp + ch + '$'
print(temp)

# 문자열의 짝수번째 글자는 모두 #으로 변경하기

t = '파이썬은재미있어요'
temp = ''

for s in t[::2]:
    temp += s + '#'
print(temp)

temp = ''
for i in range(len(t)):
    ch = '#' if i % 2 != 0 else s[i]
    temp += ch
print(temp)
'''
# 입력받는 문자열을 거꾸로 출력하기

text = input('문자열을 입력하세요 : ')
print(text[::-1])
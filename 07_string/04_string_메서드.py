# 1. 문자열 대소문자 변환
# upper(), lower(), title(), capitalize(), swapcase()
text1 = 'Python is great!'
text2 = 'Yes, it is.'
text3 = "It's not like any other"

print('대문자로', text1.upper())
print('소문자로', text2.lower())
print('단어별로 시작문자 대문자로', text2.lower().title())
print('문장의 첫글자만 대문자로', text1.upper().capitalize())
print('swapcase()', text1.swapcase())


# 2. 문자열 검색
# count(단어), find(단어), rfind(), index(), rindex(), startswith()
text4 = "I like python, i like swimming, i like hotdog "
print(text1.count('Python'))
print(text4.count('like'))
print('find():', text4.find('like'))
print('rfind():', text4.rfind('like'))
print('startswith():', text4.startswith('i like'))
print('endswith():', text4.endswith('.'))

# 3. 문자열 치환, 편집
# strip(), rstrip(), lstrip() : 공백문자(지정문자) 제거
# replace() : 문자치환
text5 = '     ham haha hotdog!    '
text6 = '<><><haha>>>>>!'
print('strip():', text5.strip())
print('lstrip():', text5.lstrip())
print('rstrip():', text5.rstrip())
print('strip("<>"):', text6.strip('<>'))
print('strip(">"):', text6.strip('>'))
print('replace():', text5.replace('ham', 'hom'))

# 4. 문자열을 분리/결합
# split(), rsplit(), join(), splitlines()
print(text4)
print('split():', text4.split())
print('split(","):', text4.split(','))
print('rsplit():', text4.rsplit())

text8 = 'apple banana kiwi'
data = text8.split()
print(data)
print('join():', '-'.join(data))
print('join():', '/'.join(data))
print('join():', ''.join(data))

text9 = '''firstline
.. secondline
.. thirdline
'''
print(text9.split())
print(text9.split('\n', 1))
print(text9.splitlines())


# 5. 문자열 정렬
# center(), ljust(), rjust()
print('center():', text8.center(30))
print('ljust():', text8.ljust(30, '-'))
print('rjust():', text8.rjust(30, '-'))

# 6. 문자열 판단 : 숫자, 알파벳, ....
# isdig(), isdecimal(), isalpha(), ....
print('1234'.isdigit())
print('1234'.isalpha())
print('abc한글'.isalpha())
print('1234***'.isalnum())
print('hello'.islower())
print('Hello haha'.istitle())

# Unicode : \u0101
print('\u0101', '\u0011', '\u2665', '\u2668')
# zip() 함수

foods = ['떡볶이', '짜장면', '피자', '라면']
sides = ['김치', '단무지', '피클']

zip_list = list(zip(foods, sides))
zip_dic = dict(zip(foods, sides))
print(zip_list)
print(zip_dic)

# 리스트 컴프리헨션

xlist = [x*2 for x in range(1,11)]
print(xlist)

ylist = [x+y for x in range(1,11) for y in range(10,20)]
print(ylist, len(ylist))

foodlist = [(x,y) for x in ['밥', '국', '짜장면'] for y in ['김치','단무지']]
print(foodlist)

# 세트 컴프리헨션

yset = {x+y for x in range(1,5) for y in range(10,15)}
print(yset, len(yset))

# 딕셔너리 컴프리헨션

print({food:side for food in foods for side in sides})

stds = ['철수', '영희', '길동', '순희']
std_dic = {std:0 for std in stds}
print(std_dic)

stdu = {'철수':60, '영희':50, '길동':90, '순희':100}

std_scores = { name : 'pass' if score > 60 else 'non-pass' for name, score in stdu.items() }
print(std_scores)


std_scores2 = dict()
for name, score in stdu.items():
    if score > 60:
        std_scores2[name] = 'pass'
    else:
        std_scores2[name] = 'non-pass'
print(std_scores2)
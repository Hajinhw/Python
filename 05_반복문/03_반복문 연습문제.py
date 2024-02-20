# 숫자 10개를 입력받아서 양, 음, 0의 개수 출력
'''
p = 0
m = 0
z = 0

for num in range(1, 11):
    ins = int(input(f'숫자{num} 입력 : '))
    if ins > 0:
        p += 1
    elif ins < 0:
        m += 1
    else:
        z += 1
print('-----------------')
print('양의 개수 : ', p)
print('음의 개수 : ', m)
print('0의 개수 : ', z)

fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit == 'fruit':
    fruit = 'fruit'
else:
    fruit = fruit
print(fruit)

list_data_a = [1, 2]
list_data_b = [3, 4]
for i in list_data_a:
    for j in list_data_b:
        result = i + j
print(result)
'''
for star in range(5, 0, -1):
    print('*' * star)


for star in range(1, 10, 2):
    print('{0:^20}'.format('*' * star))

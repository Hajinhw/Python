'''
# 1번.

with open('data/s.txt', 'r') as f:
    data = f.readlines()
    new = sorted(data)
for i in new:
    print(i, end='')


# 3번.

def my_sum(filename, data_list='r'):
    with open(filename, 'r') as f:
        data = f.readlines()
    for i in data:
        s = i.split(' ')
        add = int(s[0]) + int(s[1])
        print(f'{s[0]}+{s[1]}={add}')

my_sum('data/mysum.txt', 'r')
'''

# 2번.

my_list1 = []
cnt = []
with open('data/yesterday.txt', 'r') as f:
    while True:
        text = f.readline()
        if not text:
            break
        word = text.lower().strip('\n').split(' ')
        for i in word:
            my_list1.append(i)
    my_list2 = sorted(my_list1)
    for k in range(my_list2.count('')):
        my_list2.remove('')


    my_list3 = []
    for j in my_list2:
        if j not in my_list3:
            my_list3.append(j)
        else:
            pass

    for p in my_list3:
        cnt.append(my_list2.count(p))


    for o in range(len(my_list3)):
        result = (f'"{my_list3[int(o)]}":{cnt[int(o)]}')
        print(result)


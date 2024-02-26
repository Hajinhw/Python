'''
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
my_list2 = []
cnt = []
with open('data/yesterday.txt', 'r') as f:
    data = f.readlines()
    for i in data:
        word = i.lower().strip('\n').split(' ')
        for x in word:
            my_list1.append(x)
            cnt.append(my_list1.count(x))

            if x not in my_list2:
                my_list2.append(x)
            else:
                pass
            list2 = sorted(my_list2)




print(list2,cnt)



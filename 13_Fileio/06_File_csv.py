# csv(comma separated value) 파일 읽기
# csv 모듈 임포트
# https://docs.python.org/ko/3/library/csv.html

import csv

# csv.reader()
path = 'data/scores2.csv'
with open(path, 'r', encoding='utf=8') as f:
    data = csv.reader(f)
    for x in data:
        print(x)

# obj = csv.writer(csvfile)
# obj.writerows(데이터) : 데이터는 csv파일에 쓸 객체
data_list = [['구', '전체', '내국인', '외국인'],
             ['관악구', 519864, 502889, 17775],
             ['강남구', 547602, 542498, 5014],
             ['송파구', 686181, 679247, 6934],
             ['강동구', 425846, 424345, 4312]]

print(data_list)
with open('data/pop.csv', 'w', encoding='utf-8', newline='') as f:
    obj = csv.writer(f, delimiter=',')
    obj.writerows(data_list)

def writecsv(filename, data_list, encoding):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        obj = csv.writer(f, delimiter=',')
        obj.writerows(data_list)

writecsv('data/pop1.csv', data_list, encoding='utf-8')


# 파이썬 객체를 파일에 저장(dump), 읽기(load)
# https://docs.python.org/ko/3/library/pickle.html

# import pickle
from pickle import dump, load

data_list = [['구', '전체', '내국인', '외국인'],
             ['관악구', 519864, 502889, 17775],
             ['강남구', 547602, 542498, 5014],
             ['송파구', 686181, 679247, 6934],
             ['강동구', 425846, 424345, 4312]]

with open('data/datalist.pickle', 'wb') as f:
    dump(data_list, f)

with open('data/datalist.pickle', 'rb') as f:
    data_pickle = load(f)

for item in data_pickle:
        print(item)

data_pickle.append(['종로구', 321673, 30000, 214549])

print(data_pickle)
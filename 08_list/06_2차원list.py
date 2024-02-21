# 2차원 리스트 : [행][열]

table = [[1,2,3,4], [7,8,9,10], [10,11,12,14]]
table2 = [[1,2,3,4], [7,8,10], [10,11,12,14]]
print(table)
print(len(table))
print(table[0])

for item in table:
    print(item, type(item), len(item))

for row in table:
    for col in row:
        print(col, end=' ')
    print()
'''
row_n = len(table)
col_n = len(table[0])

for r in range(row_n):
    for c in range(col_n):
        print(table[r][c], end=' ')
    print()
'''

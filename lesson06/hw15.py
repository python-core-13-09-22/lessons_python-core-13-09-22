# Змінити послідовність стовпців матриці так, щоб елементи її першого рядка були відсортовані за зростанням.
from pprint import pprint
from random import randint

# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7

# 1 3 7 5
# 1 3 7 5
# 1 3 7 5
# 1 3 7 5


N = 10
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(randint(0, 100))
    matrix.append(row)
pprint(matrix)

for i in range(N):
    for j in range(i + 1, N):
        if matrix[0][i] > matrix[0][j]:
            # print(matrix[0], end=f" => {i=} {j=} => ")
            for c in range(N):
                matrix[c][i], matrix[c][j] = matrix[c][j], matrix[c][i]
            # print(matrix[0])
pprint(matrix)

d = {2: [1, 2, 3], 3: [31, 32, 33]}
l = sorted(d.keys())
for key in l:
    print(key, end="\t")
print()
for i in range(len(d.get(l[0]))):
    for key in l:
        print(d.get(key)[i], end="\t")
    print()

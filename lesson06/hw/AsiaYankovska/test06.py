# 1
from random import randint
l = [randint(0, 10) for i in range(5)]
l2 = [int(input()) for i in range(5)]
l3 = sum(l + l2)
print(l)
print(l2)
print(l3)

# 2
import math
l = [int(input()) for i in range(5)]
print(l)
print(sum(l))
print(math.prod(l))

# 3
l= [randint(-5, 4) for i in range(20)]
neg = 0
pos = 0
for i in range(-5, 0):
    neg += l.count(i)
for i in range(1, 5):
    pos += l.count(i)
print(l)
print(l.count(0))
print(neg)
print(pos)

# 4  
neg = []
pos = []
for i in range(10):
    x = randint(-5, 5)
    if x < 0:
       neg.append(x)
    elif x > 0:
       pos.append(x)
print(neg)
print(pos)

# 5
l = [randint(-5, 5) for i in range(10)]
print(l)
l2 = [x for x in l if x > 0]
print(l2)

# 6
l = [randint(0, 10)]
l2 = []
for i in range(10):
    x = randint(0, 10)
    l.append(x)
    if l[i] % 2 == 0:
        l2.append(i)
print(l)
print(l2)

# 7
l = [randint(0, 10) for i in range(10)]
l2 = []
print(l)
for i in l:
    if l.count(i) == 1:
        l2.append(i)
print(l)
print(l2)

# 8
l = [randint(0, 20) for i in range(5)]
print(l)
x = l.index(max(l))
y = l.index(min(l))
for i in range(len(l)):
   l[x], l[y] = l[y], l[x]
print(l)

# 9
matrix = [[randint(0, 10) for a in range(5)],
          [randint(0, 10) for b in range(5)],
          [randint(0, 10) for c in range(5)]]
print(matrix)
suma1 = sum(matrix[0])
suma2 = sum(matrix[1])
suma3 = sum(matrix[2])
print(f"Сума 1 рядка = {suma1}, сума 2 рядка = {suma2}, сума 3 рядка = {suma3}")
suma4 = matrix[0][0] + matrix[1][0] + matrix[2][0]
print(f"Сума перших стопців = {suma4}")
suma5 = matrix[0][1] + matrix[1][1] + matrix[2][1]
print((f"Сума перших стопців = {suma5}"))
suma6 = matrix[0][2] + matrix[1][2] + matrix[2][2]
print((f"Сума перших стопців = {suma6}"))
matrix[0].append(suma1)
matrix[1].append(suma2)
matrix[2].append(suma3)
s = [suma4, suma5, suma6]
matrix.append(s)
print(matrix)

# 10

matrix = [randint(0, 999) for i in range(20)]
print(matrix)
s = 0
for element in matrix:
    if 9 < element < 100:
        s += 1
print(f"Кількість двозначних чисел = {s}")

# 11
matrix = []
matrix2 = []
for i in range(5):
    matrix2.append(matrix)
    for _ in range(3):
        matrix.append(int(input()))
    matrix.append(sum(matrix))
    matrix = []
for i in matrix2:
    print(i)

# 12
matrix = [[randint(0, 10) for a in range(3)],
          [randint(0, 10) for b in range(3)],
          [randint(0, 10) for c in range(3)]]
print(matrix)
for i in matrix:
    minimum = min(matrix[0][0], matrix[1][0], matrix[2][0])
    minimum2 = min(matrix[0][1], matrix[1][1], matrix[2][1])
    minimum3 = min(matrix[0][2], matrix[1][2], matrix[2][2])
    print(minimum, minimum2, minimum3)
    maximum = max(minimum, minimum2, minimum3)
    print(maximum)

# 13
l = []
l2 = []
l3 = []
for i in range(3):
    x = randint(0, 5)
    l.append(x)
print(l)
for i in range(3):
    x = randint(0, 5)
    l2.append(x)
print(l2)
for i in range(3):
    if l[i] > l2[i]:
        l3.append(l[i])
    else:
        l3.append(l2[i])
print(l3)

#14
matrix = []
m = []
for i in range(10):
    for j in range(10):
        x = randint(0, 10)
        m.append(x)
    matrix.append(m)
    m = []
print("Matrix")
for i in matrix:
    print(i)
y = 0
for i in range(10):
    matrix[i][y],matrix[i][9-y] = matrix[i][9-y],matrix[i][y]
    y += 1
print("Changed")
for i in matrix:
    print(i)

#15
l = []
matrix = []
a = []
b = []
x = 0
for _ in range(5):
    matrix.append(l)
    for _ in range(5):
        l.append(randint(0, 10) for i in range(5))
    l = []
print("Matrix")
for i in matrix:
    print(i)
for i in range(5):
    c = [a[i] for a in matrix]
    a.append(c)
    x = sorted(a)
for i in range(5):
    d = [a[i] for a in x]
    b.append(d)
for i in b:
    print(i)

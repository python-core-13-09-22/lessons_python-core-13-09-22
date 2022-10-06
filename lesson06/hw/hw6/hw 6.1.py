import random

l = int(input("Введіть кількість елементів в списках: "))

s1 = []
s2 = []
s3 = []

for i in range(l):
    i = i + 1
    x = random.randint(1, 100)
    s1.append(x)

print(f"Введіть {l} елементів списака:")

for i in range(l):
    i = i + 1
    a = int(input(f"Введіть {i} елемент списака: "))
    s2.append(a)

for i in range(l):
    b = int(s1[i]) + int(s2[i])
    s3.append(b)

print(s1)
print(s2)
print(s3)


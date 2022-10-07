import random

matrix = []

vysota = int(input("Введіть висоту матриці: "))
shyryna = int(input("Введіть ширину матриці:"))

for i in range(vysota):
    ryadok = []
    for j in range(shyryna):
        element = random.randint(-100, 100)
        ryadok.append(element)
    matrix.append(ryadok)

print(" Матриця: \n")
for i in matrix:
    print(i)
print("\n")

i = 0
nova_stroka = []
while i < shyryna:
    elementy_stovptsya = []
    for j in matrix:
        elementy_stovptsya.append(j[i])
    a = sum(elementy_stovptsya)
    nova_stroka.append(a)
    i += 1
matrix.append(nova_stroka)




for i in matrix:
    summa = sum(i)
    i.append(summa)

print("Оброблена матриця:\n")

for i in matrix:
    print(i)



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

minimalni = []
for i in range(shyryna):
    stovpets = []
    for j in matrix:
        el_st = j[i]
        stovpets.append(el_st)
    minimalni.append(min(stovpets))

print(max(minimalni))



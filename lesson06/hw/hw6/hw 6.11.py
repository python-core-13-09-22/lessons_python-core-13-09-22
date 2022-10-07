matrix = []

vysota = 4
shyryna = 5

for i in range(vysota):
    ryadok = []
    for j in range(shyryna):
        element = int(input(" Введіть елемент матриці: "))
        ryadok.append(element)

    matrix.append(ryadok)

newryadok = []
for i in matrix:
    a = sum(i)
    newryadok.append(a)

matrix.append(newryadok)

print(" Матриця: \n")
for i in matrix:
    print(i)
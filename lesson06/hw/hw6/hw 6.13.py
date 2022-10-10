matrix1 = []
matrix2 = []
matrix_x = []

vysota = int(input("Введіть висоту матриць: "))
shyryna = int(input("Введіть ширину матриць: "))

for i in range(vysota):
    ryadok1 = []
    for j in range(shyryna):
        element1 = int(input(" Введіть елемент матриці 1 : "))
        ryadok1.append(element1)
    matrix1.append(ryadok1)



for i in range(vysota):
    ryadok2 = []
    for j in range(shyryna):
        element2 = int(input(" Введіть елемент матриці 2: "))
        ryadok2.append(element2)
    matrix2.append(ryadok2)

print(" Матриця 1: \n")
for i in matrix1:
    print(i)

print(" Матриця 2: \n\n")
for i in matrix2:
    print(i)

for i in range(vysota):
    ryadok_x = []
    for j in range(shyryna):
        ryadok_x.append((matrix1[i])[j]) if (matrix1[i])[j] >= (matrix2[i])[j] else ryadok_x.append((matrix2[i])[j])
    matrix_x.append(ryadok_x)

print(" \nМатриця з більшими значеннями відповідних елементів: \n")
for i in matrix_x:
    print(i)


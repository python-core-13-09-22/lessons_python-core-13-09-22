matrix = []

vysota = 50
shyryna = 20
element = 0
for i in range(vysota):
    ryadok = []
    for j in range(shyryna):
        ryadok.append(element)
        element = element + 1
    matrix.append(ryadok)

print(" Матриця: \n")
for i in matrix:
    print(i)


dvuhsnachni = 0

for i in matrix:
    for j in i:
        j = str(j)
        if len(j) == 2:
            dvuhsnachni = dvuhsnachni + 1
        else:
            continue


print(f"\nДвухзначиних чисел в матриці: {dvuhsnachni}")

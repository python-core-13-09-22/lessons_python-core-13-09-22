import random

spysok = []

kilkist = int(input("Введіть бажану кількість елементів в списку: "))

for i in range(kilkist):
    chyslo = random.randint(-100, 100)
    spysok.append(chyslo)

print(spysok)

for i in spysok:
    for j in spysok:
        if j < 0:
            spysok.remove(j)
        else:
            continue
    continue

print(spysok)
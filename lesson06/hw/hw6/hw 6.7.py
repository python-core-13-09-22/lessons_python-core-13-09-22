import random

spysok = []


dovzyna = int(input("Введіть кількість елементів списку: "))

for i in range(dovzyna):
    element = random.randint(1, 100)
    spysok.append(element)

for i in spysok:
    x = spysok.count(i)
    if x == 1:
        print(f"Елемент '{i}' зустрічається один раз")
    else:
        continue

print(spysok)

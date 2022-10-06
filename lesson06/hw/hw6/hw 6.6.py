import random

spysok = []
spysok_ind = []

dovzyna = int(input("Введіть кількість елементів списку: "))

for i in range(dovzyna):
    element = random.randint(-100, 100)
    spysok.append(element)

for i in spysok:
    if i%2 == 0:
        spysok_ind.append(spysok.index(i))
    else:
        continue

print(f"Повний список: {spysok}")
print(f"Список індексів парних елементів: {spysok_ind}")


import random

spysok = []


dovzyna = int(input("Введіть кількість елементів списку: "))

for i in range(dovzyna):
    element = random.randint(-100, 100)
    spysok.append(element)

print(spysok)

maxymum = spysok[spysok.index(max(spysok))]
minimum = spysok[spysok.index(min(spysok))]
max_index = spysok.index(max(spysok))
min_index = spysok.index(min(spysok))

spysok[max_index] = minimum
spysok[min_index] = maxymum
print(maxymum)
print(minimum)

print(spysok)


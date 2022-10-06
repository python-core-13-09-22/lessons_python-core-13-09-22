
spysok = []

kilkist = int(input("Введіть бажану кількість елементів списку: "))

for i in range(kilkist):
    i = i + 1
    element = float(input(f" Введіть елемент номер {i}: "))
    spysok.append(element)
summa = 0.0
dobutok = 1.0
for i in spysok:
    summa = summa + i
    dobutok = dobutok * i

print(f"Ви ввели список: {spysok}")
print(f"Сумма елементів списку: {summa}")
print(f"Добуток елементів списку: {dobutok}")




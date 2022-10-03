from random import randint

x = randint(0, 100)
i = 10

while i != 0:
    i = i -1
    chyslo = int(input("Відгадайте число від 0 до 100: "))
    if chyslo < x:
        print(f"\nВаше число менше загаданого.\n \nУ Вас залишилось {i} спроб\n")
    elif chyslo > x:
        print(f"\nВаше число більше загаданого.\n \nУ Вас залишилось {i} спроб.\n")
    elif chyslo == x:
        print(f"\n Вітаю, ви відгадали. Загадане число {x}")
        break
    else:
        print(" Ви ввели щось не те. Спробуйте ще.")



i = 0
a = 0
while i != 10:
    i = i + 1
    x = input("Введіть число: ")
    if int(x) % 5 == 0:
        a = a + 1
        print("Число кратне 5")
    else:
        print("Число не кратне 5")

print(f"Кількість чисел кратних 5 = {a}")



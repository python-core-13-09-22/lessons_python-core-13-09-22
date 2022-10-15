# task 1
import random
num = random.randint(0, 100)
for i in range(10):
    x = int(input())
    if x == num:
        print("You guess the number!")
        break
    elif x > num:
        print("It's bigger")
    elif x < num:
        print("It's less")
print(f"Oops, you didn't guess! The number is {num}")

# task 2
num = 0
for i in range(10):
    x = int(input())
    if x > 2:
        if x % 5 == 0:
            num += 1
    else:
        print("Error")
print(num)

# task 3
for i in range(1, 11):
   j = i * 9
   print(9, "*", i, "=", j)

# task 4
for i in range(5):
    if i==0 or i==4:
        for j in range(20):
            print('N', end='')
    else:
        print('N', end='')
        for j in range(1,18):
            print('M', end='')
        else:
            print('M', end='')
        print('N', end='')
    print()
# task 5
P = random.randint(0, 100)
H = random.randint(0, 100)
a = 0
b = 1
c = 0
for i in range(5):
    n = int(input())
    if n < P:
        a += n
    elif n > H:
        b *= n
    elif n == P or n == P:
        break
    while P < H:
        if n > P and n < H:
            c += 1
print(f"P = {P}, H = {H}")
print(f"Сума = {a}, Добуток = {b}, Кількість в діапазоні від P до H = {c} ")


# task 6
x = 0
y = 0
for i in range(5):
    n = int(input())
    if n == 0:
        break
    elif n > 0:
        x += 1
    else:
        y += 1
    s = x + y
    positive_number = (x * 100) / s
    negative_number = (y * 100) /s
print(n)
print(f"Додатних чисел {positive_number} %, від\'ємних чисел {negative_number} %")

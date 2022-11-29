# 1. У програмі генерується випадкове ціле число від 0 до 100. Користувач повинен
# його відгадати не більше ніж за 10 спроб. Після кожної невдалої спроби повинно
# повідомлятися чи більше чи менше введене користувачем число, ніж те, що загадане.
# Якщо за 10 спроб число не відгадане, то вивести загадане число.
import random

a = random.randint(0, 100)
for i in range(10):
    b = int(input(f"Guess the number from 0 to 100: "))
    if b < a:
        print(f"Your number {b} is less then given number")
    elif b > a:
        print(f"Your number {b} is more then given number")
    else:
        break
print(f"The given number is {a}")

# 2. Вводяться десять натуральних чисел більше 2. Порахувати, скільки серед них чисел,
# що кратні 5-ти. (не використовувати лісти)

n = 0
for i in range(10):
    c = int(input(f"Input the number > 2: "))
    if c % 5 == 0:
        n += 1
print(f"Кількість чисел, що кратні 5-ти: {n}")

# 3. Вивести на екран таблицю множення (від 1 до 9).

table = []
j = 1
while j < 10:
    y = 1
    g = []
    while y < 10:
        k = y * j
        g.append(f"{y}x{j}={k}")
        y += 1
    table.append(g)
    j += 1
for row in table:
    for element in row:
        print(element, end="\t")
    print()

# 4. Вивести на екран «прямокутник» розміру N на M, утворений з двох видів символів.
# Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого.

m = int(input(f"Input the length: "))
n = int(input(f"Input the width: "))
rectangle = []
for s in range(m):
    line = []
    for v in range(n):
        if (s == 0 or s == (m - 1)) or (v == 0 or v == (n - 1)):
            line.append("S")
        else:
            line.append("V")
    rectangle.append(line)
for line in rectangle:
    for element in line:
        print(element, end=" ")
    print()

# 5. Дано число P  і число H. Користувач вводить послідовність чисел. Визначити: суму тих чисел,
# які менше P; добуток чисел, які більші за H; кількість чисел, що знаходяться  в діапазоні значень
# від P до H. При введенні числа рівного P або H, припинити обчислення та вивести результат.
# (не використовувати білдін функції)

P = 35
H = 62
sum = 0
mult = 1
num = 0
q = 0
while q != P or q != H:
    q = int(input(f"Input any number: "))
    if q < P:
        sum += q
    elif q > H:
        mult *= q
    elif q > P and q < H:
        num += 1
    else:
        print(f"The sum of numbers which are less then P: {sum}\n"
              f"The multitude of numbers which are more then P: {mult}\n"
              f"The quantity of numbers which are between P and H: {num}")
        break

# 6. Для чисел, що вводяться користувачем, визначити відсоток додатних та від’ємних чисел.
# При введенні числа 0 закінчити роботу.
positive = 0
negative = 0
number = ""
while number != 0:
    number = input(f"Input any positive or negative number: ")
    if int(number) > 0:
        positive += 1
        print(f"відсоток додатних чисел {positive*100/(positive+negative)}\n"
              f"відсоток від’ємних чисел {negative*100/(positive+negative)}")
    elif int(number) < 0:
        negative += 1
        print(f"відсоток від’ємних чисел {negative*100/(positive+negative)}\n"
              f"відсоток додатних чисел {positive*100/(positive+negative)}")
    else:
        print(f"The operation has finished!")
        break

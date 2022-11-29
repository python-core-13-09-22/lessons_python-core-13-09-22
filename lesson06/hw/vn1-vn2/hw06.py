# 1. Заповнити один список випадковими числами, інший - введеними з клавіатури числами,
# в третій записати суми відповідних елементів перших двох. Вивести вміст списків на екран.
import random
import math

list_1 = []
list_2 = []
list_3 = []
for i in range(10):
    list_1.append(random.randint(0, 100))
    list_2.append(int(input(f"Input any number from 0 to 100: ")))
    list_3.append(list_1[-1] + list_2[-1])
print(f"The list of random numbers: {list_1}\n"
      f"The list of typed numbers: {list_2}\n"
      f"The sum of numbers: {list_3}")

# 2. Заповнити список дійсними числами введенням з клавіатури. Порахувати суму і добуток елементів
# списку. Вивести на екран сам список, отримані суму і добуток його елементів.

list = []
sum = 0
mult = 1
for i in range(10):
    list.append(int(input(f"Input any number from 0 to 100: ")))
    sum += list[-1]
    mult *= list[-1]
print(f"The list: {list}\n"
      f"The sum of all elements in the list: {sum}\n"
      f"The multiplication of all elements in the list: {mult}")

# 3. Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список.
# Порахувати кількість додатних, від’ємних і нульових елементів. Вивести на екран елементи
# списку і пораховані кількості.

list = []
positive = 0
negative = 0
zero = 0
for i in range(20):
    list.append(random.randint(-5, 4))
    if list[-1] > 0:
        positive += 1
    elif list[-1] < 0:
        negative += 1
    elif list[-1] == 0:
        zero += 1
print(f"The list of random numbers from -5 to 4: {list}\n"
      f"The quantity of positive elements in the list: {positive}\n"
      f"The quantity of negative elements in the list: {negative}\n"
      f"The quantity of zero elements in the list: {zero}")

# 4. Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки
# додатні, у другий - тільки від’ємні. Числа, рівні нулю, ігнорувати. Вивести на екран всі
# згенеровані випадкові числа і елементи обох списків.

list =[]
positive_list = []
negative_list = []
for i in range(30):
    list.append(random.randint(-5, 5))
    if list[-1] > 0:
        positive_list.append(list[-1])
    elif list[-1] < 0:
        negative_list.append(list[-1])
print(f"The list of random numbers from -5 to 5: {list}\n"
      f"The list of positive numbers: {positive_list}\n"
      f"The list of negative numbers: {negative_list}")

# 5. Заповнити список випадковими додатними і від’ємними цілими числами. Вивести його на екран.
# Видалити з списку всі від’ємні елементи і знову вивести.

list =[]
for i in range(30):
    list.append(random.randint(-10, 10))
print(f"The list of random numbers from -10 to 10: {list}")
for element in list:
    if element < 0:
        list.remove(element)
print(f"The list of positive numbers: {list}")

# 6. У другому списку зберегти індекси парних елементів першого списку. Наприклад, якщо дано
# список зі значеннями 8, 3, 15, 6, 4, 2, то  другий треба заповнити значеннями 1, 4, 5, 6
# (або 0, 3, 4, 5 - якщо індексація починається з нуля), оскільки саме в цих позиціях першого
# масиву стоять парні числа.

list_1 = []
list_2 = []
for i in range(30):
    list_1.append(random.randint(0, 100))
print(f"Перший список: {list_1}")
for y in list_1:
    if y % 2 == 0:
        list_2.append(list_1.index(y))
print(f"Індекси парних елементів першого списку: {list_2}")

# 7. У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран.

list_1 = []
for i in range(30):
    list_1.append(random.randint(0, 10))
print(f"Cписок: {list_1}")
for y in list_1:
    c = list_1.count(y)
    if c == 1:
        print(f"{y} is a unique element")

# 8. У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.

list_1 = []
for i in range(30):
    list_1.append(random.randint(0, 100))
print(f"Cписок випадкових чисел: {list_1}")
min_number = min(list_1)
max_number = max(list_1)
list_1[list_1.index(min_number)] = max_number
list_1[list_1.index(max_number)] = min_number
print(f"Оновлений список випадкових чисел: {list_1}")

# 9. Порахувати суми кожного рядка і кожного стовпця матриці. Доповнити її стовпцем, який містить
# суми елементів рядків та рядком, елементами якого є суми елементів стовпців.

matrix = []
for i in range(11):
    row = []
    row_sum = 0
    if i == 10:
        for r in range(10):
            element_sum = 0
            for e in matrix:
                element_sum += e[r]
            row.append(element_sum)
    else:
        for y in range(11):
            if y == 10:
                row.append(row_sum)
            else:
                row.append(random.randint(0, 100))
                row_sum += row[-1]
    matrix.append(row)
for row in matrix:
    for element in row:
        print(element, end="\t")
    print()

# 10. Сформувати матрицю з чисел від 0 до 999, вивести її на екран. Порахувати кількість двозначних
# чисел в ній.

for i in range(10):
    row = []
    for y in range(10):
        row.append(random.randint(0, 999))
    matrix.append(row)
print("ORIGIN MATRIX")
count_elements = 0
for row in matrix:
    for element in row:
        if element > 0 and element < 100:
            count_elements += 1
        print(element, end="\t")
    print()
print(f"кількість двозначних чисел {count_elements}")

# 11. Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків). Програма
# повинна обчислювати суму введених елементів кожного рядка і записувати її в останній рядок.
# Наприкінці слід вивести отриману матрицю.

matrix = []
for i in range(4):
    row = []
    row_sum = 0
    for y in range(5):
        if y == 4:
            row.append(row_sum)
        else:
            row.append(int(input("Input any number: ")))
            row_sum += row[-1]
    matrix.append(row)
for row in matrix:
    for element in row:
        print(element, end="\t")
    print()

# 12. Знайти максимальний елемент серед мінімальних елементів стовпців матриці.

max_list = []
for x in range(5):
    min_list = []
    for l in matrix:
        min_list.append(l[x])
    max_list.append(min(min_list))
m = max(max_list)
print(f"The maximum number among the minimum numbers is {m}")

# 13. Дві матриці заповнюються введенням з клавіатури. В елементи третьої матриці такої ж
# розмірності записати більші з відповідних елементів перших двох.

matrix_1 = []
matrix_2 = []
matrix_3 = []
for i in range(5):
    row_1 = []
    row_2 = []
    row_3 = []
    for y in range(5):
        a = int(input("Input any number for matrix 1: "))
        b = int(input("Input any number for matrix 2: "))
        row_1.append(a)
        row_2.append(b)
        if a > b:
            row_3.append(a)
        else:
            row_3.append(b)
    matrix_1.append(row_1)
    matrix_2.append(row_2)
    matrix_3.append(row_3)
print("     MATRIX 1     ")
for row in matrix_1:
    for element in row:
        print(element, end="\t")
    print()
print("     MATRIX 2     ")
for row in matrix_2:
    for element in row:
        print(element, end="\t")
    print()
print("     MATRIX 3     ")
for row in matrix_3:
    for element in row:
        print(element, end="\t")
    print()

# 14. У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані відповідно на
# головній та бічній діагоналях.

matrix = []
for i in range(10):
    row = []
    for y in range(10):
        item = random.randint(0, 100)
        row.append(item)
    matrix.append(row)
print("ORIGIN MATRIX")
for row in matrix:
    for element in row:
        print(element, end="\t")
    print()
print("CHANGED MATRIX")
index_1 = 0
index_2 = 9
for row in matrix:
    if index_1 > index_2:
        row.insert(index_2, row[index_1])
        row[index_1 + 1] = row[index_2 + 1]
        row.pop(index_2 + 1)
    else:
        row.insert(index_1, row[index_2])
        row[index_2 + 1] = row[index_1 + 1]
        row.pop(index_1 + 1)
    index_1 += 1
    index_2 -= 1
    for element in row:
        print(element, end="\t")
    print()

# 15. Змінити послідовність стовпців матриці так, щоб елементи її першого рядка були відсортовані
# за зростанням.

N = 10
matrix = []
for i in range(N):
    row = []
    for y in range(N):
        item = random.randint(0, 100)
        row.append(item)
    matrix.append(row)
print("ORIGIN MATRIX")
for row in matrix:
    for element in row:
        print(element, end="\t")
    print()
for i in range(len(matrix[0])):
    for y in range(len(matrix[0])):
        if matrix[0][i] < matrix[0][y]:
            for r in range(len(matrix)):
                matrix[r][i], matrix[r][y] = matrix[r][y], matrix[r][i]
print("CHANGED MATRIX")
for row in matrix:
    for element in row:
        print(element, end="\t")
    print()

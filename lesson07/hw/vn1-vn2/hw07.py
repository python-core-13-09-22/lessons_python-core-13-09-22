# 1. Написати функцію `arithmetic`, яка приймає 3 аргументи: перші 2 - числа, третій - операцію,
# яка повинна бути здійснена над ними. Якщо третій аргумент +, додати їх; якщо -, то відняти;
# * - помножити; / - розділити (перше на друге). В інших випадках повернути рядок
# "Невідома операція".
import math


def arithmetic(a, b, o):
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    elif o == "*":
        return a * b
    elif o == "/":
        return a / b
    else:
        print("Unknown operation")

a = int(input("Input an integer a: "))
b = int(input("Input an integer b: "))
o = input("Input an operation (+ - * /): ")
print(arithmetic(a, b, o))

# 2. Написати функцію `is_year_leap`, приймає 1 аргумент - рік, і повертає True, якщо рік високосний,
# і `False` в іншому випадку.
import datetime

def is_year_leap(year):
    year = datetime.datetime(year, 12, 31)
    if int(year.strftime("%j")) == 366:
        return True
    else:
        return False

year = int(input("Input a year: "))
print(is_year_leap(year))

# 3. Написати функцію `square`, яка приймає 1 аргумент - сторону квадрата, і повертає 3 значення
# (за допомогою кортежу): периметр квадрата, площу квадрата і діагональ квадрата.

import math

def square(d):
    p = d * 4
    s = d * d
    l = d * math.sqrt(2)
    t = {p, s, l}
    return t

d = int(input("Введіть довжину сторони квадрата: "))
print(f"Периметр квадрата, площа квадрата і діагональ квадрата: {square(d)}")

# 4. Написати функцію `season`, яка приймає 1 аргумент - номер місяця (від 1 до 12), і повертає
# пору року, якій цей місяць належить (зима, весна, літо або осінь).

def season(month):
    months = {"Зима": [12, 1, 2],
              "Весна": [3, 4, 5],
              "Літо": [6, 7, 8],
              "Осінь": [9, 10, 11]}
    for key, value in months.items():
        for m in value:
            if m == month:
                return key

month = int(input("Введіть номер місяця: "))
print(f"Пора року - {season(month)}")

# 5. Користувач робить внесок в розмірі n гривень строком на years років під 10% річних
# (щороку розмір його внеску збільшується на 10%. Ці гроші додаються до суми вкладу, і на них в
# наступному році теж будуть відсотки).
# Написати функцію `bank`, яка приймає аргументи n і years, і повертає суму, яка буде на рахунку
# користувача.

def bank(money, years):
    for y in range(years):
        money += money * 10 / 100
    return money

money = int(input("Введіть сумму в гривнях: "))
years = int(input("Введіть кількість років: "))
print(f"Ваш вклад через {years} років буде дорівнювати {bank(money, years)} гривень")

# 6. Написати функцію `is_prime`, яка приймає 1 аргумент - число від 0 до 1000, і повертає True,
# якщо воно просте, і `False` - в іншому випадку.



# 7. Написати функцію `date`, яка приймає 3 аргументи - день, місяць і рік. Повернути True, якщо
# така дата є в нашому календарі, і `False` - в іншому випадку.

def date(d, m, y):
    try:
        if datetime.datetime(y, m, d):
            return True
    except:
        return False

d = int(input("Input a day: "))
m = int(input("Input a month: "))
y = int(input("Input a year: "))
print(date(d, m, y))

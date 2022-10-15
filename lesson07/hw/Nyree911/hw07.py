# 1. Написати функцію `arithmetic`, яка приймає 3 аргументи: перші 2 - числа, третій - операцію, яка повинна бути здійснена над ними.
#  Якщо третій аргумент +, додати їх; якщо -, то відняти; * - помножити; / - розділити (перше на друге).
#  В інших випадках повернути рядок "Невідома операція".

def arithmetic (x, y, z):
    if z == "*":
        res = x*y
        return (f"{x}*{y}={res}")
    elif z == "/":
        res = x/y
        return (f"{x}/{y}={res}")
    elif z == "+":
        res = x+y
        return (f"{x}+{y}={res}")
    elif z == "-":
        res = x-y
        return (f"{x}-{y}={res}")
    else:
        return "Unknown operation"

print (arithmetic(2,2,"*"))



# 2. Написати функцію `is_year_leap`, приймає 1 аргумент - рік, і повертає True, якщо рік високосний, і `False` в іншому випадку.

from calendar import isleap

def is_year_leap (year):
    return isleap(year)

print (is_year_leap(2001))

# 3. Написати функцію `square`, яка приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу): периметр квадрата, 
# площу квадрата і діагональ квадрата.

from math import sqrt
def square (side):
    return (side*4, side**2, side*sqrt(2) )

print(square(5))

# 4. Написати функцію `season`, яка приймає 1 аргумент - номер місяця (від 1 до 12), і повертає пору року, якій цей місяць 
# належить (зима, весна, літо або осінь).

def season (month):
    if month == 1 or month == 2 or month == 12:
        return ("It is Winter")
    if month == 3 or month == 4 or month == 5:
        return ("It is Spring")
    if month == 6 or month == 7 or month == 8:
        return ("It is Summer")
    if month == 9 or month == 10 or month == 11:
        return ("It is Autumn")

print(season(6))

# 5. Користувач робить внесок в розмірі n гривень строком на years років під 10% річних (щороку розмір його внеску збільшується на 10%. 
# Ці гроші додаються до суми вкладу, і на них в наступному році теж будуть відсотки).
# Написати функцію `bank`, яка приймає аргументи n і years, і повертає суму, яка буде на рахунку користувача.

def bank(amount, years):
    for _ in range(years):
        amount= amount * 1.1
    return amount

print(bank(1000, 3))

# 6. Написати функцію `is_prime`, яка приймає 1 аргумент - число від 0 до 1000, і повертає True, якщо воно просте, 
# і `False` - в іншому випадку.

def is_prime(num):
    if num == 0:
        return('It is 0')
    elif num == 1:
        return('it is 1')
    elif num == 2:
        return True
    for i in range (2,num):
        if num % i == 0:
            return False
        else:
            return True
print(is_prime(937))

# 7. Написати функцію `date`, яка приймає 3 аргументи - день, місяць і рік. Повернути True, якщо така дата є в нашому календарі, 
# і `False` - в іншому випадку.

import calendar
def date(day, month, year):
    monthrange = int(calendar.monthrange(int(year), int(month))[1])
    if  int(day) >0 and int(day) <= monthrange:
        day = True
    if  0< int(year):
        year = True
    if  1 <= int(month) <=12 :
        month = True
    if day == True and month == True and year == True:
        return True
    else:
        return False

print(date(31,2,2020))


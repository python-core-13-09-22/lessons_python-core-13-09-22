from calendar import Calendar
import math
import random


# 1. Написати функцію `arithmetic`, яка приймає 3 аргументи: перші 2 - числа, третій - операцію, яка повинна бути здійснена над ними. 
# Якщо третій аргумент +, додати їх; якщо -, то відняти; * - помножити; / - розділити (перше на друге). 
# В інших випадках повернути рядок "Невідома операція".

# def arithmetic (x, y , q):
#     if q == "+":
#         add = x + y
#         return (f"{x} {q} {y} = {add}")
#     elif q == "-":
#         sub = x - y
#         return (f"{x} {q} {y} = {sub}")    
#     elif q == "*":
#         mult = x * y
#         return (f"{x} {q} {y} = {mult}")         
#     elif q == "/":
#         div = x / y
#         return (f"{x} {q} {y} = {div}")
#     else:
#         return "unknown op"

# print(arithmetic(3, 4, "+"))


# 2. Написати функцію `is_year_leap`, приймає 1 аргумент - рік, і повертає True, якщо рік високосний, і `False` в іншому випадку.

# def is_year_leap (year):
#     return True if year % 4 == 0 else False

# print(is_year_leap(2000))


# 3. Написати функцію `square`, яка приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу): периметр квадрата, площу квадрата і діагональ квадрата.

# def square (side):
#     p = side * 4
#     s = side**2
#     d = math.sqrt(2) * side
#     return (p, s, d)
# print(square(4))

# 4. Написати функцію `season`, яка приймає 1 аргумент - номер місяця (від 1 до 12), і повертає пору 
# року, якій цей місяць належить (зима, весна, літо або осінь).

# def season (month):
#     if 0 < month >= 2 or month == 12:
#         return "It is winter"
#     elif 2 < month >= 5:
#         return "It is spring"
#     elif 5 < month >= 8:
#         return "It is summer"  
#     elif 8 < month >= 11:
#         return "It is autumn"
#     else:
#         print("is not correct")    

# print(season(2))              


# 5. Користувач робить внесок в розмірі n гривень строком на years років під 10% річних (щороку розмір його внеску збільшується на 10%. 
# Ці гроші додаються до суми вкладу, і на них в наступному році теж будуть відсотки).
# Написати функцію `bank`, яка приймає аргументи n і years, і повертає суму, яка буде на рахунку користувача.

# def bank (n, years):
#     for _ in range(years):
#         n = n * 1.1
#     return n 

# print(bank(100, 2))
    

# 6. Написати функцію `is_prime`, яка приймає 1 аргумент - число від 0 до 1000, і повертає True, якщо воно просте, і `False` - в іншому випадку.

# def is_prime(num):
#     if num == 0:
#         return('It is 0')
#     elif num == 1:
#         return('it is 1')
#     elif num == 2:
#         return True
#     for i in range (2,num):
#         if num % i == 0:
#             return False
#         else:
#             return True
# print(is_prime(77))


# 7. Написати функцію `date`, яка приймає 3 аргументи - день, місяць і рік. 
# Повернути True, якщо така дата є в нашому календарі, і `False` - в іншому випадку.

import calendar
def date(day, month, year):
    if 1 <= day <= 31 and 1 <= month <= 12 and 0 < year:
        return True
    else:
        return False
        
print(date(18,7,1999))




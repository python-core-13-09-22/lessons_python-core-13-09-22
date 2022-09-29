from ast import match_case
from curses.ascii import isalnum
import calendar
import math
import random
#                                   Task 1
# - Ввести значення(рік), вивести повідомлення `It's a leap year!` якщо рік 
# високосний і `This is not a leap year!` якщо ні.

# First solution
try:
    year = int(input("Please insert a year to check if it is leap year: "))
    if year % 4 == 0:
        print("It's a leap year!")
    else:
        print("This is not a leap year!")
except:
    ValueError 
    print("Please enter correct year")

# Second solution
# try:
#     year = int(input("Please insert a year to check if it is leap year: "))
#     checkYear = calendar.isleap(year)
#     if checkYear is True:
#         print("It's a leap year!")
#     else:
#          print("This is not a leap year!")
        
# except:
#     ValueError 
#     print("Please enter correct year")


#                                   Task 2
# - Ввести три значення (рік, місяць, день) у відповідні змінні. Визначити 
# чи введені дані відповідають коректному запису дати.
run = True
while run:
    year = input("Please enter correct year: ")
    if year.isdigit() and 0< int(year):
        print("Correct")
    else:
        print("Your input is incorrect")
        break
    month = input("Please enter correct month: ")
    if year.isdigit() and 1 <= int(month) <=12 :
        print("Correct")
    else:
        print("Your input is incorrect")
        break
    day = input("Please enter correct day: ")
    monthrange = int(calendar.monthrange(int(year), int(month))[1])
    if day.isdigit():
        if  int(day) >0 and int(day) <= monthrange:
            print("Correct")
            break
        else:
            print("Your day is out of range of month")
            break
    else:
        print("Your input is incorrect")
        break


#                                   Task 3
# - Для довільних дійсних чисел `a`, `b`, і `c` визначити, чи має рівняння 
# `ax2+bx+c=0` хоча б один дійсний корінь і якщо так, то видрукувати 
# його.
print("ax2 * bx * c=0")
a= float(input ("Insert 'a'"))
b= float(input ("Insert 'b'"))
c= float(input ("Insert 'c'"))
d = float(b*b - 4 * a* c)
if d>0:
    sqrtD = math.sqrt(d)
    x1 = (-b + sqrtD)/(a*2)
    x2 = (-b - sqrtD)/(a*2)
    print(f"This quadratic equation will have next roots: {x1}, {x2}")
elif d == 0:
    x=-b/2*a
    print(f"This quadratic equation will have next root: {x}")
else:
    print("There is no roots")
#                                   Task 4
# - Задано три довільних числа. Визначити, чи можна побудувати 
# трикутник з такими довжинами сторін; Якщо так, то видрукувати його 
# периметр та площу.
try:
    a = int(input("Please insert first side of triangle: "))
    b = int(input("Please insert second side of triangle: "))
    c = int(input("Please insert last side of triangle: "))
    per = a+b+c # Heron's formula
    p = per/2  #Half of perimetr
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    if a> b+c or b>a+c or c>b+a:
        print("Impossible to build a triangle")
    else:
        print (f"Your triangle with sides {a}, {b}, {c} will have:")
        print(f'Perimetr = {per}')
        print(f'Area = {s}')
except:
    ValueError 
    print("Please enter correct number")


#                                   Task 5
# - Нехай `k`- ціле від `1` до `365`. Присвоїти цілій змінній n значення 
# (понеділок, вівторок, …, суботу чи неділю) залежно від того , на який 
# день тижня припадає `k`-й день не високосного року, в якому 1 січня -
# понеділок.

k = random.randrange(1, 365)
if k % 7 == 0:
    n = "Sunday"
elif k % 7 == 1 or k == 1:
    n = "Monday"
elif k % 7 == 2 or k == 2:
    n = "Tuesday"
elif k % 7 == 3 or k == 3:
    n = "Wednesday"
elif k % 7 == 4 or k == 4:
    n = "Thursday"
elif k % 7 == 5 or k == 5:
    n = "Friday"
elif k % 7 == 6 or k == 6:
    n = "Saturday"
print (f' On {k} day will be {n}')

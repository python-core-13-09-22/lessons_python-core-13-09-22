# Ввести значення(рік), вивести повідомлення It's a leap year! якщо рік високосний і This is not a leap year! якщо ні.

year1 = input("write year: ")
if year1 is not int:
    print("write numb")
else:
    if int(year1) % 4 == 0:
        print("It's a leap year")
    else:
        print("This is not a leap year")

# Ввести три значення (рік, місяць, день) у відповідні змінні. Визначити чи введені дані відповідають коректному запису дати.
from curses.ascii import isdigit

import math 


year = input("write year: ") 
if year.isdigit():
    if int(year) > 0:
        print("correct")
    else:
        print("year is < 0")
else:
    print("write numb")

month = input("write month: ") 
if month.isdigit():
    if int(month) > 0 and int(month) <= 12:
        print("correct")
    else:
        print("not correct month")
else:
    print("not integer")

day = input("write day: ")
if day.isdigit():
    if int(day) > 0 and int(day) <= 31:
        print("correct")
    else:
        print("not correct day")
else:
    print("not integer")


# Для довільних дійсних чисел a, b, і c визначити, чи має рівняння ax2+bx+c=0 хоча б один дійсний корінь і якщо так, то видрукувати його.


# Задано три довільних числа. Визначити, чи можна побудувати трикутник з такими довжинами сторін; Якщо так, то видрукувати його периметр та площу.
a = int(input("value1:"))
b = int(input("value2:"))
c = int(input("value3:"))
if int(a) < int(b) + int(c) and int(b) < int(a) + int(c) and int(c) < int(b) + int(a):
    print("yes u can")
    perimetr = a + b + c
    hp = perimetr / 2
    area = math.sqrt((hp * (hp - a)*(hp - b)*(hp - c)))
    print(f"perimetr is {perimetr} and area is {area}") 

else:
    print("not correct velue")




# Нехай k- ціле від 1 до 365. Присвоїти цілій змінній n значення (понеділок, вівторок, …, суботу чи неділю) залежно від того , на який день тижня 
# припадає k-й день не високосного року, в якому 1 січня - понеділок.
k = input("1 - 365: ")
if int(k) > 0 and int(k) <= 365:
    if int(k) % 7 == 1 or k ==1:
        print("monday")
    elif int(k) % 7 == 2 or k == 2:
        print("tuesday")
    elif int(k) % 7 == 3 or k ==3:
        print("wednesday")
    elif int(k) % 7 == 4 or k ==4:
        print("thursday")
    elif int(k) % 7 == 5 or k ==5:
        print("friday")
    elif int(k) % 7 == 6 or k ==6:
        print("saturday")    
    elif int(k) % 7 == 0:
        print("sunday")
else:
    print("not correct value")        
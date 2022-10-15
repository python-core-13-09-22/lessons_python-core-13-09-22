import math
import random
# Task 1
# Написати функцію `arithmetic`, яка приймає 3 аргументи: перші 2 - числа, третій - операцію, яка повинна бути здійснена над ними.
# Якщо третій аргумент +, додати їх; якщо -, то відняти; * - помножити; / - розділити (перше на друге). В інших випадках повернути рядок "Невідома операція".
def arithmetic (a, b, c):
    if c == '+':
        result = a + b
        print(result)
    elif c == '-':
        result = a - b
        print(result) 
    elif c == '*':
        result = a * b   
        print(round(result, 2))
    elif c == '/' and b != 0: 
        result = a / b
        print(round(result, 2))  
    else:
        result = 'unknown operation'
        print(result)
a = float(input('a: '))
b = float(input('b: '))
c = input('c: ') 
arithmetic(a, b, c)  

#Task 2
# Написати функцію `is_year_leap`, приймає 1 аргумент - рік, і повертає True, якщо рік високосний, і `False` в іншому випадку.
def is_year_leap (year):
    if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 !=0):
        return True
    else:
        return False
year = int(input("Please Enter a year: "))          
print(is_year_leap(year))  

#Task 3
# Написати функцію `square`, яка приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу): 
# периметр квадрата, площу квадрата і діагональ квадрата.
l = []
def square (h):
    p = 4*h
    l.append(p)
    s = h*h
    l.append(s)
    d = round(h*math.sqrt(2), 2)
    l.append(d)
    t = tuple(l)
    print(t)
h = int(input("Please Enter h: "))     
square(h)


# Task 4
# Написати функцію `season`, яка приймає 1 аргумент - номер місяця (від 1 до 12), і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь).
def season (m) :
    list1 = [[12 , 1 , 2], [3 , 4 , 5],[6 , 7 , 8], [9 , 10 , 11]]
    if m in list1[0] :
        print ( "WINTER" )
    elif m in list1[1] :
        print ( "SPRING" )
    elif m in list1[2] :
        print ( "SUMMER" )
    elif m in list1[3] :
        print ( "AUTUMN" )
    else :
        print ( "Invalid Month Number" ) 
m = int(input("m: "))
season(m)


# Task 5
# Користувач робить внесок в розмірі n гривень строком на years років під 10% річних (щороку розмір його внеску збільшується на 10%.
# Ці гроші додаються до суми вкладу, і на них в наступному році теж будуть відсотки). Написати функцію `bank`, яка приймає аргументи 
# n і years, і повертає суму, яка буде на рахунку користувача.
def bank (n, years):
    for i in range(int(years)):
        n += (n*10)/100
    return n
n = int(input("money: "))
years = int(input("years: "))
print(bank(n, years))    
     
     
# # Task 6
# Написати функцію `is_prime`, яка приймає 1 аргумент - число від 0 до 1000, і повертає True, якщо воно просте, і `False` - в іншому випадку.
def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a
print(is_prime(int(input("Enter a number: "))))

# Task 6.1
def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
print(is_prime(int(input("Enter a number: "))))



# Task 7
# Написати функцію `date`, яка приймає 3 аргументи - день, місяць і рік. Повернути True, якщо така дата є в нашому календарі, і `False` - в іншому випадку.
def date (day, month, year):
    if day <= 0 or month <= 0 or year <= 0:
        return False
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 !=0): months[1] = 29        
        if day <= months[month - 1]:
            if month <= 12:
                return True
        return False 
day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))
print(date(day, month, year))    
      

            
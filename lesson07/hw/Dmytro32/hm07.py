from ast import Str
from math import sqrt

def get_number(text:str):
    while True:
        x=input(f"{text}:")
        if x.isdigit():
            break
        print("There is no number")
    return int(x)
def arithmetic(a:int,b:int,oper:str):
    match(oper):
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            if not(b==0):
                return round(a/b,2) 
            else:
                return "Error div on 0"
        case _:
            return "Operation no indefication"

def is_year_leap(year:int):
    if (year%4==0 and year%100!=0) or (year%100==0 and year%400==0):
        return True
    else:
        return False

def square(a:int):
    p=4*a
    d=round(sqrt(2)*a,2)
    s=a**2 
    t = (p,d,s)
    return t

def season(a:int):
    match(a):
        case 12|1|2:
            return "Winter"
        case 3|4|5:
            return "Spring"
        case 6|7|8:
            return "Summer"
        case 9|10|11:
            return "Autumn"
        case _:
            return "Out of range month"
def bank(year:int,n:int):
    res=n+n/10
    if year>1:
        res = bank(year-1,res)
    return round(res,2)

def is_prime(n:int):
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True

def date(year:int,month:int,day:int):
    if len(str(year)) ==4 and (month in (1,3,5,7,8,10,12) and 0<day<=31) or (month in (4,6,9,11) and 0<day<=30) or(month ==2 and ((((year%4==0 and year%100!=0) or (year%100==0 and year%400==0))or 0<day<=29)or 0<day<28)):
        return True
    else: 
        return False

print("Task1")
num1=get_number("Number 1 for operation")
num2=get_number("Number 2 for operation")
oper=input("Operation:")
print(arithmetic(num1,num2,oper))


print("Task2")
year=get_number("Year for checking")
print(is_year_leap(year))

print ("Task3")
a=get_number("Lenght of square")
res=square(a)
print(f"P={res[0]},d={res[1]},S={res[2]}")

print ("Task4")
month=get_number("Month for checking")
print(season(month))

print("Task5")
mon=get_number("Money in begin")
year=get_number("How much year")
print(bank (year,mon))

print("Task6")
a=get_number("What number")
print(is_prime(a))

print("Task7")
year=get_number("Year")
month=get_number("Month")
day=get_number("Day")
print(date(year,month,day))


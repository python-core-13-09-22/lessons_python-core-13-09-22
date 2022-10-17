# 1
import random
num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
function = input("Function ")
def arithmetic(num1, num2, function):
    if function == "+":
         s = num1 + num2
         print(f"Cума = {s}")
    elif function == "-":
         m = num1 - num2
         print(f"Різниця = {m}")
    elif function == "*":
         mul = num1 * num2
         print(f"Добуток = {mul}")
    elif function == "/":
         d = num1 / num2
         print(f"Частка = {d}")
    else:
        print("Невідома операція")
arithmetic(num1, num2, function)

# 2
def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
year = int(input("Enter the year "))
print(is_year_leap(year))

# 3
def square(a):
    p = a * 4
    s = a * a
    d = (2 * s) ** 0.5
    result = (p, s, d)
    print(result)
a = random.randint(0, 20)
square(a)

# 4
def season(month):
    if month <= 2 or month == 12:
        print("It's winter")
    elif month >= 3 and month <= 5:
        print("It's spring")
    elif month >= 6 and month <= 8:
        print("It's summer")
    elif month >= 9 and month <= 11:
        print("It's fall")
    else:
        print("Incorrect number")
month = int(input("Enter the month number "))
season(month)

# 5
def bank(n, years):
    for i in range(years):
        n += n * 0.1
    return n
n = int(input("Deposit "))
years = int(input("Years: "))
print(bank(n, years))

# 6
def is_prime(num):
    while num in range(0, 1000):
        for i in range(2, num+1):
            for j in range(2, i):
                if i % j == 0:
                    return True
                else:
                    return False
num = int(input("Enter the number "))
print(is_prime(num))

# 7
def date(day, month, year):
    if month == 2:
        if day <= 29 and year % 4 == 0 and year % 100 != 0:
            return True
        elif day == 29 and year % 4 != 0:
            return False
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 1 <= day <= 31 and 1 <= year <= 2022:
            return True
        else:
            return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day <= 30 and 1 <= year <= 2022:
            return True
        else:
            return False
    else:
        return False
day = int(input("Enter day "))
month = int(input("Enter month "))
year = int(input("Enter year "))
print(date(day, month, year))

#Написати функцію is_year_leap, приймає 1 аргумент - рік, і повертає True, якщо рік високосний,
# і False в іншому випадку.

def is_year_leap(a):
    if a % 4 == 0:
        print(True)
    else:
        print(False)

a = input("Введіть рік: ")

is_year_leap(int(a))
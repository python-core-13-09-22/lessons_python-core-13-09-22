# Написати функцію date, яка приймає 3 аргументи - день, місяць і рік. Повернути True,
# якщо така дата є в нашому календарі, і False - в іншому випадку.

def date(dd, mm, yy,):
    if yy % 4 == 0 and mm == 2:
        if 1 <= dd <= 31 and 1 <= mm <= 12 and 1 <= yy <= 2022:
            return True
        else:
            return False
    if 1 <= dd <= 31 and 1 <= mm <= 12 and 1 <= yy <= 2022:
        return True
    else:
        return False

d = int(input("Введіть день місяця: "))
m = int(input("Введіть місяць: "))
y = int(input("Введіть рік: "))

print(date(d, m, y))
# Записати в стрічку філософію Пайтона
txt = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the
rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced."""
print(txt)

# Знайти в заданій стрічці кількість входжень слів (better, never, is)
a = txt.count("better")
print(f"the number of 'better' is: {a}")
b = txt.count("never")
print(f"the number of 'never' is: {b}")
c = txt.count("is")
print(f"the number of 'is' is: {c}")

# Вивести весь текст у верхньому регістрі (всі великі літери)
print(txt.upper())

# Замінити всі входження символу “і” на “&”
print(txt.replace("i", "&"))

# Задано чотирицифрове натуральне число.
x = 2853
print(f"Задано чотирицифрове натуральне число {x}")
# Знайти добуток цифр цього числа.
g = 1
for i in str(x):
    s = x % 10
    g *= s
    x = (x - s) / 10
print(f"Добуток цифр цього числа = {int(g)}")

# Записати число в реверсному порядку.
x = 2853
rev_x = ""
for i in str(x):
    s = int(x % 10)
    rev_x += str(s)
    x = (x - s) / 10
print(f"число в реверсному порядку = {int(rev_x)}")

# Посортувати цифри, що входять в дане число
x = 2853
sort_x = ""
for i in str(x):
    h = min(str(x))
    sort_x += h
    x = str(x).replace(h, "")
print(f"Посортовані цифри = {int(sort_x)}")

# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
z = 20
y = 40
print(f"z = {z}")
print(f"y = {y}")
z = z + y
y = z - y
z = z - y
print(f"z = {z}")
print(f"y = {y}")

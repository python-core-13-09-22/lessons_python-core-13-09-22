#  Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000,
# і повертає True, якщо воно просте, # і False - в іншому випадку.

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
        else:
            return True




x = int(input("Введіть число: "))
print(is_prime(x))
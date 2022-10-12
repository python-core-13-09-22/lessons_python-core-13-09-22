# Написати функцію square, яка приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу):
# периметр квадрата, площу квадрата і діагональ квадрата.
import  math

def square(a):
    parametry = (f'Периетр: {a*4}', f'Площа: {a*a}', f'Діагональ: {math.sqrt(2 * (a * a))}')
    for i in parametry:
        print(i)
    print(f"Тип виведених даних: {type(parametry)}")

storona = int(input("Введіть сторону квадрата: "))

square(storona)

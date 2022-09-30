import math

# Високосний рік

#r = int(input("Введіть рік: "))
#print("This is not a leap year!") if r%4 != 0 else print("It's a leap year!")

#Ввести три значення (рік, місяць, день) у відповідні змінні.

#while True:
#    r = input("Введіть рік:  ")
#    if r.isdigit() and r.isnumeric() and len(r) < 5 and int(r)>0:
#       break
#    else:
#        print("Ви ввели не правильне значення! Спробуйте ще ;) ")

#while True:
#    m = input("Введіть місяць:  ")
#    if m.isdigit() and m.isnumeric() and len(m) < 3 and 12 >= int(m) > 0 :
#       break
#    else:
#        print("Ви ввели не правильне значення! Спробуйте ще ;) ")
#
#while True:
#    d = input("Введіть день: ")
#    if d.isdigit() and d.isnumeric() and len(d) < 3 and 31 >= int(d) > 0 :
#       break
#    else:
#        print("Ви ввели не правильне значення! Спробуйте ще ;) ")
#
#print(f"Дата {r}.{m}.{d} ")
#


# визначити, чи має рівняння `ax2+bx+c=0` хоча б один дійсний корінь
#a = float(input("a = "))
#b = float(input("b = "))
#c = float(input("c = "))

#dis = b**2 - 4 * a * c
#print(f"Дискримінант: {dis}")
#if dis > 0:
#    x1 = (-b + math.sqrt(dis)) / (2 * a)
#   x2 = (-b - math.sqrt(dis)) / (2 * a)
#    print(f"Дискримінант має 2 дійсних кореня: \nx1 = {x1} \nx2 = {x2}")
#elif dis == 0:
#    x = -b / (2 * a)
#    print(f"Дискримінант має 1 дійсний корінь: \nx = {x}")
#else:
#    print("Дійсних коренів немає ")



# Визначити, чи можна побудувати трикутник

print("Введіть значення сторін трикутника\n")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    p = a + b + c
    s = 0.5 * a * (a / 2 * (a / 2 * (math.sqrt((p*(p - a)*(p - b)*(p - c))))))
    print(f"Трикутник може бути побудований: \nПериметр ={p} \nПлоща ={s} ")
else:
    print("Трикутник не може бути побудований. \nСорян...)")
# task 1
y = int(input("Year "))
if y % 4 == 0 and y % 100 != 0:
    print("It's a leap year")
else:
    print("It is not a leap year")

# task 2
year = int(input())
month = int(input())
day = int(input())
if year <= 2022 and month <= 12 and day <= 31:
    print("Correct")
else:
    print("Incorrect")

# task 3

a = int(input())
b = int(input())
c = int(input())
d = (b ** 2) - (4 * a * c)
if d >= 0 and a != 0:
    root1 = (-b - (d**0.5)) / (2 * a)
    root2 = (-b + (d**0.5)) / (2 * a)
    print(root1)
    print(root2)
else:
    print("Error")

# task 4
a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < b + a:
    p = a + b + c
    print("Периметр трикутника = ", p)
    pp = p // 2
    s = (pp * (pp - a) * (pp - b) * (pp - c)) ** 0.5
    print("Площа трикутника = ", s)
else:
    print("Неможливо побудувати трикутник")
    
# task 5
k = int(input())
for k in range(1, 366):
    if k % 7 == 1 or k == 1:
        n = "Понеділок"
    elif k % 7 == 2 or k == 2:
        n = "Вівторок"
    elif k % 7 == 3 or k == 3:
        n = "Середа"
    elif k % 7 == 4 or k == 4:
        n = "Четвер"
    elif k % 7 == 5 or k == 5:
        n = "Пятниця"
    elif k % 7 == 6 or k == 6:
        n = "Субота"
    elif k % 7 == 0:
        n = "Неділя"
print(n)

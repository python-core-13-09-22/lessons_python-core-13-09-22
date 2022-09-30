# Task 1
year = int(input("Enter a year: "))
if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 !=0):
  print("It's a leap year")
else:
  print("This not a leap year")

# Task 2
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))
if ((0 < year <= 2022) and (1 <= month <=12) and (1 <= day <= 31)):
    print('year = ', year, 'month = ', month, 'day = ', day)
else:
    print('enter correct date')

# Task 3
import math
print('ax^2 + bx +c = 0')
a = float(input("Enter a:  "))
b = float(input("Enter b:  "))
c = float(input("Enter c:  "))
D = b ** 2 - 4 * a * c
print("D = ", D)
if D > 0:	
	x1 = (-b + math.sqrt(D)) / (2 * a)
	x2 = (-b - math.sqrt(D)) / (2 * a)
	print('x1 = ', x1, 'x2 = ', x2)
elif D == 0:
    x = -b / (2 * a)
    print('x = ', x)
else:
    print('there aren\'t roots')

# Task 4
import math
a = float(input("Enter a:  "))
b = float(input("Enter b:  "))
c = float(input("Enter c:  "))
if ((a, b, c > 0)  and (a + b) > c and (b + c) > a and (c + a) > b):
    P = a + b + c
    P = round(P, 2)
    print("P =  ", P)
    p = P / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    S = round(S, 2)
    print("S =  ", S)
else:
    print('It is impossible to construct a triangle')
    
    
# Task 5    
k = int(input("Enter k:  "))
for n in range(1, 365):
    if k % 7 == 0:    
        n = "Sunday"
    elif k == 1 or k % 7 == 1:
        n = "Monday"
    elif k == 2 or k % 7 == 2:     
        n = "Tuesday"          
    elif k == 3 or k % 7 == 3:     
        n = "Wednesday"     
    elif k == 4 or k % 7 == 4:    
        n = "Thursday" 
    elif k == 5 or k % 7 == 5:    
        n = "Friday"  
    elif k == 6 or k % 7 == 6:     
        n = "Saturday"    
print(n)           

import math
import random
#task1
print("task 1")
year = input("Year for task 1:")
if year.isdigit and len(year) == 4:
    year = int(year)
    if (year%4==0 and year%100!=0) or (year%100==0 and year%400==0):
         print("It's a leap year!")
    else:
       print(" It's not a leap year!")
else:
   print ("Not correct number")

#task2
print("task 2")
year = input ("Year for task 2:")
month = input ("Month:")
day = input("Day:")
if year.isdigit and month.isdigit and day.isdigit: 
    year=int(year)
    month=int(month)
    day=int(day)
    if len(str(year)) ==4 and (month in (1,3,5,7,8,10,12) and 0<day<=31) or (month in (4,6,9,11) and 0<day<=30) or(month ==2 and ((((year%4==0 and year%100!=0) or (year%100==0 and year%400==0))or 0<day<=29)or 0<day<28)):
        print("Everyting correct")
    else: 
        print("Someting wrong in data ")
else:
    print("Something not nummber")

#task3
print("task 3")
a=input("a:")
b=input("b:")
c=input("c:")
if a.isdigit and b.isdigit and c.isdigit:
    a=int(a)
    b=int(b)
    c=int(c)
    if a==0:
        x=-c/b 
        print(f"Solution:x={x:.2f}")
    else:
        D= b**2-4*a*c 
        if D<0:
            print ("No solution")
        else:
            if D!=0:
                x1 = (-b+ math.sqrt(D))/2*a 
                x2= (-b - math.sqrt(D))/2*a
                print(f"Solution : x1={x1:.2f}, x2={x2:.2f}")
            else: 
                x=-b/2*a
                print(f"Solution : x={x}")
else:
    print("No number")

#task4
print("task 4")
a=input("a:")
b=input("b:")
c=input("c:")
if a.isdigit and b.isdigit and c.isdigit:
    a=int(a)
    b=int(b)
    c=int(c)
    if a+b>c:
        p=a+b+c 
        s=math.sqrt(p/2*(p/2-a)*(p/2-b)*(p/2-c))
        print(f"triangle possible, perimeter {p}, area { s:.2f}")
    else:
        print("triangle is impossible")
else:
    print("No number")

#task5
print("task 5")
k=random.randint(1, 365)
if k== 1 or k%7==1:
     print(f"k={k}, Monday")
elif k==2 or k%7==2:
    print(f"k={k},Tuesday")
elif k==3 or k%7==3:
    print(f"k={k},Wednesday")
elif k==4 or k%7==4:
    print(f"k={k},Thursday")
elif k==5 or k%7==5:
    print(f"k={k},Friday")
elif k==6 or k%7==6:
    print(f"k={k},Saturday")
elif k%7==0:
    print(f"k={k},Sunday")
else:
    print(f"k={k},error")








 
                                                                                                  



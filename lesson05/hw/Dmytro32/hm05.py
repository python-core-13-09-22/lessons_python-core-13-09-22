import random

def GetNumber():
    while True:
        x= input()
        if x.isdigit():
            x=int(x)
            break
        print("There is no number")
    return x

def PosNegNumber():
    while True:
        x=input("Possitve or negative number:")
        if x.isdigit() or  (x.startswith("-") and x[1:].isdigit()):
            break
        print("There is no number")
    return x

def Task1():
    print("Task 1")
    y = random.randint(0,100)
    sym = '\u2116'
    for i in range(1,11):
        print ("Guess number:",end="")
        x= GetNumber()
        if (x<y):
            print (f"Number {x} is too low")
        elif (x>y):
            print (f"Number {x} is too large")
        else:
            print (f"Number {x} is correct")
            break
    else:
        print (f"The number was:{y}")

def Task2():
    print("Task 2")
    array = []

    for i in range(10):
        while True:
            print(f"Number {i} for task 2:",end ="")
            x=GetNumber()
            if x>2:
                break
            print("Number is less then 2")
        array.append(x)
    count=0
    for i in array:
        if i%5==0:
            count+=1
    print(f"Numbers that divide  by five={count}")

def Task3():
    print("Task 3")
    for i in range(1,10):
        for j in range(1,10):
            print(f"{j:<1} * {i:<1} = {i*j:<2};",end= " ")
        print()

def Task4():
    print("Task 4")
    print("M:",end="")
    m=GetNumber()
    print("N:",end="")
    n=GetNumber()
    for i in range(m):
        for j in range(n):
            if i==0 or i==m-1 or j==0 or j==n-1:
                print ("\u00AE" ,end="")
            else:
               print("\u00A9",end="")
        print()

def Task5():
    print("Task 5")
    P,H,mult,sums,count=5,7,1,0,0
    while True:
        print("Get number for task5:",end="")
        x=GetNumber()
        if x<P:
            sums+=x
        elif x>H:
            mult*=x
        elif P<x<H:
            count+=1
        elif x==P or x==H:
            break
    print(f"Sum is {sums} , Mult is {mult}, Numbers bettwen P and H:{count} ")

def Task6():
    print("Task 6")
    pCount=nCount=0

    while True:
        x=PosNegNumber()
        if x.startswith("-"):
            nCount+=1
        elif int(x)==0:
            break
        else:
            pCount+=1
    pPercent=pCount/(pCount+nCount)*100
    nPercent=nCount/(pCount+nCount)*100

    print (f"Possitive:{pPercent:.2f}%,Negative:{nPercent:.2f}%")
    pCount=nCount=0
 
Task1()
Task2()
Task3()
Task4()
Task5()
Task6()






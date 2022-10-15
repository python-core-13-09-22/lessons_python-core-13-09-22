import random


def GetNumber():
    while True:
        x=input("Number to  list:")
        if x.isdigit():
            break
        else:
            print("There is no number")
    return int(x)

def task1():
    print("task 1")
    l1,l2,l3=[],[],[]
    for i in range(6):
        l1.append(random.randrange(0,10))
    print(f"Genereted list is:{l1}")
    for i in range(len(l1)):
        l2.append(GetNumber())
        l3.append(l1[i]+int(l2[i]))
    print(f"result: {l3}")
    
def task2():
    print("task 2")
    l=[]
    for i in range(6):
        l.append(GetNumber())
    lsum=sum(l)
    lmul=1
    for i in l:
        lmul*=i
    print(f"list{l},sum={lsum},mul={lmul}")

def task3():
    print("task 3")
    l=[]
    pc,nc=0,0
    for i in range(20):
        l.append(random.randrange(-5,4))
    for i in range(-5,0):
        nc+=l.count(i)
    for i in range(1,5):
        pc+=l.count(i)
    zc=l.count(0)
    print(f"{l},possitive count={pc},negative={nc},zero-={zc}")
def task4():
    print("task 4")
    l, pos,neg=[], [], []
    new_line = '\n'

    for i in range(15):
        x=random.randrange(-5,5)
        l.append(x)
        if x>0:
            pos.append(x)
        elif x<0:
            neg.append(x)
    print(f"generated number:{l}{new_line} negative :{neg}{new_line} possitive :{pos}{new_line}")
def task5():
    print("task 5")
    l=[]
    for i in range(15):
        x=random.randrange(-10,10)
        l.append(x)
    print(l)
    k=0
    for i in range(len(l)):
        if l[k]<0:
            l.remove(l[k])
            k-=1
        if k+1>len(l)-1:
            break
        k+=1

    print(l)

def task6():
    print("task 6")
    l,l1=[],[]
    for i in range(15):
        x=random.randrange(-10,10)
        l.append(x)
    for i in range(len(l)):
        if l[i]%2==0:
            l1.append(i)
    print (f" base list: {l}")
    print (f" index list: {l1}")

def task7():
    print("task 7")
    l,l1=[],[]
    for i in range(15):
        x=random.randrange(-10,10)
        l.append(x)
    print(f"List:{l}")
    for i in l:
        if l.count(i)==1:
            l1.append(i)
    print(f"not repitet element:{l1}")

def task8():
    print("task 8")
    l=[]
    for i in range(15):
        x=random.randrange(-10,10)
        l.append(x)
    print(f"list:{l}")
    a=max(l)
    b=min(l)
    l[l.index(a)],l[l.index(b)]=l[l.index(b)],l[l.index(a)]
    print(f"list replace max amd min:{l}:{l.index(a)}:{l.index(b)}")

def task9():
    print("task 9")
    l=[]
    l1=[]
    for i in range(3):
        for j in range(3):
            x=random.randrange(-10,10)
            l1.append(x)
        l.append(l1)
        l1=[]
    print(f"list:{l}")
    sl=[]
    sh=[]
    for i in l:
        s=0
        for j in i:
            s+=j
        sl.append(s)
    for i in range(len(l)):
        s=0
        for j in range(len(l)):
            s+=l[j][i]
        sh.append(s)
    l.append(sh)
    k=0
    for i in l:

        i.append(sl[k])
        k=+1
    print(f"list sum lines and colums:{l}")

def task10():
    print("task 10")
    l=[]
    for i in range(1000):
        l.append(i)
    print("array")
    c=0
    for i in l:
        print(f"{i} ",end="")
        if i%2==0:
            c+=1
        if i%9==0 and not (i==0):
            print()
    print()
    print(f"count how many numbers div 2:{c}")

def task11():
    print("task 11")
    l=[]
    l1=[]
    sl=[]
    for i in range(5):
        s=0
        for j in range(3):
            x=GetNumber()
            s+=x
            l1.append(x)
        l.append(l1)
        l1=[]
        sl.append(s)
    l.append(sl)
    for i in l:
        print(f"{i} ")

def task12():
    print("task 12")
    l=[]
    l1=[]
    for i in range(5):
        for j in range(6):
            x=random.randrange(-10,10)
            l1.append(x)
        l.append(l1)
        l1=[]
    print(f"list:{l}")
    lmin=[]
    for i in range(6):
        hmin=0
        for j in range(5):
            if hmin<l[j][i]:
                hmin=l[j][i-1]
            elif hmin>l[j][i] or hmin==l[j][i] :
               hmin=l[j][i]
        lmin.append(hmin)
    print(f"Max of min numbers in is:{max(lmin)}")

def task13():
    print("task 13")
    l=[]
    d=[]
    r=[]
    M=6
    for i in range(M):
        x=GetNumber()
        l.append(x)
    for i in range(M):
        x=GetNumber()
        d.append(x)
    for i in range(M):
        if l[i]>d[i]:
            r.append(l[i])
        else:
            r.append(d[i])
    print(f"input list:{i}")
    print(f"rundom list:{d}")
    print(f"result compare:{r}")

def task14():
    print("task 14")
    l=[]
    l1=[]
    for i in range(10):
        for j in range(10):
            x=random.randrange(-10,10)
            l1.append(x)
        l.append(l1)
        l1=[]
    print("Created matrix 10X10:")
    for i in l:
        print(i)
    c=0
    for i in range(10):
        l[i][c],l[i][9-c]= l[i][9-c],l[i][c]
        c+=1
    print("Chanfed diagonal:")
    for i in l:
        print(i)

def task15():
    print("task 15")
    l=[]
    l1=[]
    for i in range(10):
        for j in range(10):
            x=random.randrange(-10,10)
            l1.append(x)
        l.append(l1)
        l1=[]
    print("Created matrix :")
    for i in l:
        print(i)
    for i in range(len(l[0])):
        for j in range(len(l[0])):
            if l[0][i]<l[0][j]:
                for k in range(len(l)):
                    l[k][i],l[k][j]=l[k][j],l[k][i]
    print("Sorted matrix :")
    for i in l:
        print(i)


task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()
task9()
task10()
task11()
task12()
task13()
task14()
task15()






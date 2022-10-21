import string
import random

class Berry():
    def __init__(self,name:int,color:str,vitamins:str):
        self.name = name
        self.color=color
        self.vitamins=vitamins
    def GetVitamins(self):
        return self.vitamins
class Compote():
    def __init__(self,name:str,quantity:int,berry:Berry):
        self.name = name
        self.quantity=quantity
        self.berry= berry
    def printV(self):
        res=""
        for i in self.berry:
            res+=i.GetVitamins()+";"
        return res[:-1]
class CheetSheet():
    def __init__(self,subject:str,number:int):
        self.subject=subject
        self.number=number

class Paper(CheetSheet):
    def __init__(self,size:int,place:str,subject:str,number:int):
        self.size=size
        self.place=place
        self.subject=subject
        self.number=number
class Electronical(CheetSheet):
    def __init__(self,device:str,subject:str,number:int):
        self.device=device 
        self.subject=subject
        self.number=number
class Student ():
    def __init__(self,initial:str,group:str,cheet_sheet:CheetSheet):
        self.initial=initial 
        self.group=group 
        self.cheet_sheet=cheet_sheet
    def __lt__(self,other):
        return self.cheet_sheet.subject<other.cheet_sheet.subject
    def __ge__(self,other):
        return False if self.cheet_sheet.number>=other.cheet_sheet.number else True
    def ShowElement(self):
        print(f"Student={self.initial},group={self.group},subject={self.cheet_sheet.subject},number={self.cheet_sheet.number}")

def GetStr(size:int):
    return ''.join(random.choices(string.ascii_lowercase ,k=size))
def GetInt(first:int,last:int):
    return random.randint(first,last)
def task1():
    color =["red","black","green","blue","pink"]
    b=[]
    c=[]
    for i in range(10):
        b.append(Berry(GetStr(GetInt(3,6)),color[GetInt(0,4)],GetStr(3)))
    print("Berry:")
    for i in range (10):
        print(f"name={b[i].name},color={b[i].color},vitamins={b[i].vitamins}")
    for i in color:
        l1=[]
        count=0
        for j in b:
            if j.color==i:
                count=+1
                l1.append(j)
        if count:
            c.append(Compote(i,count,l1))
    print("Compote by color with vitamins:")
    for i in c:
       print(f"{i.name} : {i.printV()}")

def task2():
    l=[]
    for i in range(20):
        if i%2==0:
            l.append(Student(f"{GetStr(1).upper()}.{GetStr(1).upper()}.{GetStr(1).upper()}.",f"{GetStr(2).upper()}-{GetInt(10,16)}",Paper(GetInt(10,40),GetStr(GetInt(5,7)),GetStr(GetInt(5,7)),GetInt(1,9))))
        else:
            if i%5==0:
                l.append(Student(f"{GetStr(1).upper()}.{GetStr(1).upper()}.{GetStr(1).upper()}.",f"{GetStr(2).upper()}-{GetInt(10,16)}",Electronical("comp",GetStr(GetInt(5,7)),GetInt(1,9))))
            else:
                l.append(Student(f"{GetStr(1).upper()}.{GetStr(1).upper()}.{GetStr(1).upper()}." ,f"{GetStr(2).upper()}-{GetInt(10,16)}",Electronical(GetStr(GetInt(3,5)),GetStr(GetInt(5,7)),GetInt(1,9))))
    print ("Student:")
    for i in l:
       i.ShowElement()
    l.sort()
    print("Sort by subject ")
    for i in l:
        i.ShowElement()
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if not(l[i]>=l[j]):
                l[i],l[j]= l[j],l[i]

    print("Sort by number ")
    for i in l:
        i.ShowElement()
        count=0
    for i in l:
        if type(i.cheet_sheet)==Electronical:
            if i.cheet_sheet.device=="comp":
                count+=1
    print(f"count comp device:{count}")
task1()
task2()





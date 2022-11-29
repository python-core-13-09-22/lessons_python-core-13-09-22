
import string
import random


def task1():
    class Phone():
        def __init__ (self,name:str,company:str,price:int):
            self,name=name
            self.company=company 
            self.price=price
    class MobilePhone(Phone):
        def __init__(self,name:str,company:str,price:int,color:str,memory:int):
            self.name=name
            self.company=company 
            self.price=price
            self.color=color
            self.memory=memory 
    class RadioPhone(Phone):
        def __init__(self,name:str,company:str,price:int,radius:int,check_answering:bool):
            self.name=name
            self.company=company 
            self.price=price
            self.radius= radius
            self.check_answering=check_answering
    files=["task1_company1.txt","task1_company2.txt"]
    l=[]
    for i in files:
        with open(i) as f:
            for line in f:
                words=line.split()
                if len(words)==5:
                    if  words[2].isdigit() and words[4].isdigit() :
                        l.append(MobilePhone(words[0],words[1],int(words[2]),words[3],int(words[4])))
                    elif  words[2].isdigit() and words[3].isdigit() and (words[4]=="True"or words[4]=="False"):
                        if words[4]=="True":
                            l.append(RadioPhone(words[0],words[1],int(words[2]),int(words[3]),True))
                        else:
                             l.append(RadioPhone(words[0],words[1],int(words[2]),int(words[3]),False))
                else:
                    print("Bad writing")
        for i in range(len(l)):
            for j in range(i,len(l)):
                if l[i].price>l[j].price:
                    l[i],l[j]=l[j],l[i]
        sum=0
        for i in l:
            sum=+i.price
    print("Sorted phone:")
    with open("task1_write.txt","w") as f:
        for i in l:
            if type(i)==MobilePhone:
                print(f"name={i.name},company={i.company},price={i.price},color={i.color},memory={i.memory}")
                f.write(i.name+','+i.company+','+str(i.price)+','+i.color+','+str(i.memory)+"\n")
            elif type(i)==RadioPhone:
                print(f"name={i.name},company={i.company},price={i.price},radius={i.radius},answering={i.check_answering}")
                f.write(i.name+','+ i.company+','+str(i.price)+','+str(i.radius)+','+str(i.check_answering)+"\n")
        f.write("all price:"+str(sum)+"\n")
    print("RadioPhone with answering:")
    with open("task1_answering.txt","w") as f:
        for i in l:
            if type(i)==RadioPhone:
                if i.check_answering=="True":
                    print(f"name={i.name},company={i.company},price={i.price},radius={i.radius},answering={i.check_answering}")
                    f.write(i.name+','+ i.company+','+i.price+','+i.radius+','+i.check_answering+"\n")

def task2():
    class Table():
        def __init__(self,size:int,material:str,price:int):
             self.size=size
             self.material=material
             self.price=price 
    class Chair():
        def __init__(self,material:str,price:int):
            self.material=material
            self.price=price
    class Furniture():
        def __init__(self,name,table,chair,quantity):
            self.name=name 
            self.table=table 
            self.chair=chair 
            self.quantity=quantity
        def GiveAll(self):
            return "name="+self.name+','+ "table size="+str(self.table.size)+','+"table material="+self.table.material+','+"table price="+str(self.table.price)+','+"chair material="+self.chair.material +','+"chair price"+str(self.chair.price) +','+"quantity="+str(self.quantity)
    def GetStr():
        return ''.join(random.choices(string.ascii_lowercase ,k=5))
    t,c,comb=[],[],[]
    with open ("task2_read.txt") as f:
        for line in f:
            words=line.split()
            if len(words)==3:
                if words[0].isdigit() and words[2].isdigit():
                    t.append(Table(int(words[0]),words[1],int(words[2])))
            elif len(words)==2:
                if words[1].isdigit():
                    c.append(Chair(words[0],int(words[1])))
        req=input("material:")
        number=""
        while not number.isdigit():
            number=input("number of chair:")
        size=""
        while not size.isdigit():
            size=input("size:")
        for i in range(len(t)):
            if t[i].material==req and t[i].size==int(size):
                comb.append(t[i])
                del t[i]
                break
        for i in range(len(c)):
            if c[i].material==req:
                comb.append(c[i])
                del c[i]
                break
        if len(comb)==2:
            res=Furniture(GetStr(),comb[0],comb[1],int(number))
            with open("teak2_req.txt","w") as f:
                print("request:" +res.GiveAll()+','+ str(res.table.price+res.chair.price*res.quantity))
                f.write (res.GiveAll()+','+ str(res.table.price+res.chair.price*res.quantity)+"\n")
        comb=[]
        for i in t:
            for j in c:
                if i.material==j.material:
                    comb.append(Furniture(GetStr(),i,j,random.randrange(2,5)))
        with open("task2_another.txt","w") as f:
            for i in comb:
                print(i.GiveAll())
                f.write (i.GiveAll()+"\n")





task1()
task2()


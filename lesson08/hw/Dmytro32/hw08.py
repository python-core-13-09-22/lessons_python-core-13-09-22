
class Person():
    def __init__(self,name,age):
        self.name= name
        self.age=age
    def compare_age(self,other):
        if self.age<other.age:
            return f"{other.name} is older than me"
        elif self.age>other.age:
            return f"{other.name} is younger than me"
        else:
            return f"{other.name} is the same age as me"

class Employee():
    def __init__(self,fname ,lname ):
        self.fullname = f"{fname } {lname }"
        self.email=f"{fname }.{lname }@company.com"

class Name():
    def __init__(self,fname,lname ):
        self.fname= fname
        self.lname= lname
    def fullname(self):
        return f"{self.fname} {self.lname}"
    def initials (self):
        return f"{self.fname[0]}.{self.lname[0]}"

print("Task1")
a=Person("Tom",43)
b=Person("Max",34)
c=Person("Deyv",43)

print(a.compare_age(b))
print(b.compare_age(a))
print(a.compare_age(c))

print("Task2")
a=Employee("Dmytro","Bidnyk")
print(f"fullname={a.fullname},email={a.email}")

print("Task3:")
e=Name("Dmytro","Bidnyk")
print(f"fullname={e.fullname()},initials={e.initials()}")

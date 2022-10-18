# 1
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def compare_age (self, other_person):
        if self.age < other_person.age:
            return(f"{other_person.name} is older than me")
        elif self.age > other_person.age:
            return f"{other_person.name} is younger than me"
        else:
            return f"{other_person.name} is the same age as me"

p1 = Person("Kate", 20)
p2 = Person("Ann", 37)
p3 = Person("Alex", 30)
me = Person("Anastasia", 30)
print(me.compare_age(p1))
print(me.compare_age(p2))
print(me.compare_age(p3))

# 2
class Employee():
    def __init__(self, firstname, lastname):
        self.fullname = firstname + ' ' + lastname
        self.email = firstname + '.' + lastname + "@company.com"
name = Employee("Anastasiia", "Yankovska")
print(f"{name.fullname}, {name.email}")

# 3
class Name():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def fullname(self):
        fullname = self.fname + ' ' + self.lname
        return fullname
    def initials(self):
        initials = self.fname[0]+ '.' + self.lname[0]
        return initials
 
n = Name("Anastasiia", "Yankovska")
print(f"{n.fullname()}, {n.initials()}")

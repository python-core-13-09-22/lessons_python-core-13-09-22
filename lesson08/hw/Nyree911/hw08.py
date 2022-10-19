# 1. В класі Person визначте метод `compare_age()`, який повертатиме результат порівняння віку людини з Вашим віком. 
# При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age, буде повертатися повідомлення наступного формату:
# {other_person} is {older than / younger than / the same age as} me.

class Person():
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def compare_age(self, my_age):
        if my_age>self.age:
            return f"{self.name} is younger than me"
        elif my_age<self.age:
            return f"{self.name} is older than me"
        else:
            return f"{self.name} is the same age as me"
p1 = Person("Nick", 23)
p2 = Person("Lily", 35)
p3 = Person("Kasandra", 10)

print(p2.compare_age(35))



# 2. Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
#    - В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
#    - В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи  ‘@company.com’ 
# наприкінці.

class Employee ():
    def __init__ (self, firstname, lastname):
        self.fullname = f" {firstname} {lastname}"
        self.email = f" {firstname}.{lastname}@company.com"
empl1 = Employee("Alex", "Smith")
empl2 = Employee("Pavlo", "Galushko")

print(empl1.email)
print(empl2.fullname)

# 3. В класі Name визначте:
#    - атрибути для first name та last name (fname та lname відповідно);
#    - атрибут fullname що повертає first і last names;
#    - атрибут initials який повертає ініціали (перші літери first та last name, розділених ‘.’ .

class Name():
    def __init__ (self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = f"{fname} {lname}"
        self.initials = f"{fname[0]}.{lname[0]}"

n1 = Name("Alex", "Smith")
n2 = Name("Pavlo", "Galushko")

print(n1.fullname)
print(n2.initials)
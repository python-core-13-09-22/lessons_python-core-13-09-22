# Task 1
#  В класі Person визначте метод `compare_age()`, який повертатиме результат порівняння віку людини з Вашим віком. 
# При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age, буде повертатися повідомлення наступного формату:
# {other_person} is {older than / younger than / the same age as} me.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def compare_age(self,other):
        if self.age < other.age:
            return f"{other.name} is older than me."
        elif self.age > other.age:
            return f"{other.name} is younger than me"
        else:
            return f"{other.name} is the same age as me"
p1 = Person("Marta", 45)
p2 = Person("Oleg", 37)
p3 = Person("Nataly", 40)
I = Person("Halyna", 40)
print(I.compare_age(p1))
print(I.compare_age(p2))
print(I.compare_age(p3))

# Task 2
# Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
#    - В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
#    - В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи  ‘@company.com’ наприкінці.

class Employee:
    def __init__(self,firstn,lastn):
        self.fullname = firstn + ' ' + lastn
        self.email = firstn + '.' + lastn + '@company.com'
fln = Employee("Halyna", "Petrenko")   
print(f"fullname: {fln.fullname}, email: {fln.email} ") 

# Task 3
# В класі Name визначте:
#    - атрибути для first name та last name (fname та lname відповідно);
#    - атрибут fullname що повертає first і last names;
#    - атрибут initials який повертає ініціали (перші літери first та last name, розділених ‘.’ .

class Name:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def fullname(self):
        return self.fname + ' ' + self.lname 
    def initials(self):
        return self.fname[0]+ '.' +self.lname[0]+ '.'
fln = Name("Halyna", "Petrenko") 
print(f"fullname: {fln.fullname()}, initials: {fln.initials()}")
     

    

           
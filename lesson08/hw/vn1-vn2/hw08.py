# 1. В класі Person визначте метод `compare_age()`, який повертатиме результат порівняння віку
# людини з Вашим віком. При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age,
# буде повертатися повідомлення наступного формату: {other_person} is {older than / younger than /
# the same age as} me.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self):
        if self.age < 45:
            return f"{self.name} is younger then me"
        elif self.age > 45:
            return f"{self.name} is older then me"
        else:
            return f"{self.name} is the same age as me"


p1 = Person("John", 30)
p2 = Person("Mark", 56)
p3 = Person("Sarah", 45)

print(p1.compare_age())
print(p2.compare_age())
print(p3.compare_age())

# 2. Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
#   - В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
#   - В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи
#   ‘@company.com’ наприкінці.

class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = self.fullname
        self.email = self.email

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def email(self):
        return f"{self.first_name}.{self.last_name}@company.com"


p4 = Employee("John", "Brown")

print(p4.fullname())
print(p4.email())

# 3. В класі Name визначте:
#   - атрибути для first name та last name (fname та lname відповідно);
#   - атрибут fullname що повертає first і last names;
#   - атрибут initials який повертає ініціали (перші літери first та last name, розділених ‘.’ .

class Name:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.fullname = self.fullname
        self.initials = self.initials

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def initials(self):
        return f"{self.fname[0]}. {self.lname[0]}."


p5 = Name("Mark", "White")

print(p5.fullname())
print(p5.initials())

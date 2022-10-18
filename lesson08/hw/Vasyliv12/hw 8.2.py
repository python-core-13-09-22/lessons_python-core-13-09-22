
class Employee:
    def __init__(self, first_name, last_name):
        self.fullname = f"{first_name} {last_name}"
        self.email = f"{first_name}.{last_name}@company.com"


p1fname = input("First name: ")
p1lname = input("Last name: ")
p1 = Employee(first_name=p1fname, last_name=p1lname)

print(p1.fullname)
print(p1.email)
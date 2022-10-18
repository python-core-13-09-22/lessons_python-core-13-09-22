class Name:
    def __init__(self, fname, lname):
        self.fullname = f"{fname} {lname}"
        self.initials = f"{fname[0]}.{lname[0]}"


person1 = Name(fname=input("First name: "), lname=input("Last name: "))

print(person1.fullname)
print(person1.initials)

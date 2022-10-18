class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self):
        if int(self.age) > 29:
            print("Other person is older than me")
        elif int(self.age) < 29:
            print("Other person is younger than me")
        elif int(self.age) == 29:
            print("Other person is the same age as me")


p1 = Person(name="Ivan", age=21)
p2 = Person(name="Vasyl", age=32)
p3 = Person(name="Roma", age=29)

p1.compare_age()
p2.compare_age()
p3.compare_age()
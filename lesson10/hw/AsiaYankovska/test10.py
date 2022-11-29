# 1
class Phone():
    def __init__(self, name, company, price):
        self.name = name
        self.firm = company
        self.price = price
class Mobile(Phone):
    def __init__(self, colour, memory):
        super().__init__(name, company, price)
        self.colour = colour
        self.memory = memory

    def __str__(self):
        return f"{self.name} made by {self.company}, price {self.price}, colour {self.colour}, memory {self.memory}"

class Radio(Phone):
    def __init__(self, radius, answering_machine):
        super().__init__(name, company, price)
        self.radius = radius
        self.answering_machine = answering_machine

    def __str__(self):
        return f"{self.name} made by {self.company}, price {self.price}, radius {self.radius}, answering_machine {self.answering_machine}"

phones = []
with open("Mobile.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        data = line.split()
        if len(data) == 5:
            phones.append(Mobile(data[0], data[1], data[2], data[3], data[4]))

with open("Radio.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        data = line.split()
        if len(data) == 5:
            phones.append(Radio(data[0], data[1], data[2], data[3], data[4]))

for i in phones:
    print(i)

sort = sorted(phones, key=lambda x: int(x.price))

with open("sort.txt", "w+") as file:
    file.write("Sort")
    for i in sort:
        file.write(str(i))
        file.write('\n')

totalprice = 0
for i in sort:
    totalprice = totalprice + i.price
    file.write("Totalprice = " + str(totalprice))
    file.write('\n')

with open("sort.txt", "a+") as file:
    file.write("Aswering mashine\n")
    for i in sort:
        if i.answering_machine == "yes":
            file.write(str(i))
            file.write('\n')

# 2
class Table():
    def __init__(self, size, material, price):
        self.size = size
        self.material = material
        self.price = price

class Chair():
    def __init__(self, material, price):
        self.material = material
        self.price = price

class Set():
    def __init__(self, table, chairs, amount):
        self.table = table
        self.chairs = chairs
        self.amount = amount

tables = []
chairs = []
with open("furniture.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        data = line.split()
        if len(data) == 3:
            tables.append(Table(data[0], data[1], data[2]))

        if len(data) == 2:
            chairs.append(Chair(data[0], data[1]))

set = []
tablematerial = input("Enter material ")
chairsamount = input("Enter amount of the chair ")
tablesize = input("Enter size of the table ")
for i in tables:
    for j in chairs:
        if i.material == tablematerial:
            if i.size == tablesize:
                if i.material == j.material:
                    totalprice += i.price
                    for k in range(int(chairsamount)):
                        totalprice += j.price
                    set.append(Set(i, j,chairsamount))
                    print(set)

with open("order.txt", 'w') as f:
    file.write("Your order\n")
    for set in set:
        file.write(str(set))
        file.write('\n')

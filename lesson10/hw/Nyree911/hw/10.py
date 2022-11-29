# # task 1
# Визначити абстрактний тип «телефон» (назва, фірма, ціна).
# Визначити 2 похідні від нього типи: «мобільний телефон» (колір, об’єм пам’яті ),
# «радіотелефон» (радіус дії, наявність автовідповідача )
class Phone(object):
    def __init__(self, name, made, price):
        self.name = name
        self.made = made
        self.price = price


class MobilePhone (Phone):
    def __init__(self, name, made, price, color, memory):
        super().__init__(name, made, price)
        self.color = color
        self.memory = memory

    def __str__(self):
        return f"{self.name} made by {self.made}, price {self.price}, color {self.color}, memory {self.memory}"


class RadioPhone (Phone):
    def __init__(self, name, made, price, radius, selfAnswer):
        super().__init__(name, made, price)
        self.radius = radius
        self.selfAnswer = selfAnswer

    def __str__(self):
        return f"{self.name} made by {self.made}, price {self.price}, radius {self.radius}, selfAnswer {self.selfAnswer}"

# У двох текстових файлах задано дані про телефони двох різних фірм.
# Зчитати ці дані в один масив


phones = []
with open("Apple.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        data = line.split()

        phones.append(MobilePhone(data[0], data[1], int(data[2]), data[3], data[4]))

with open("panasonic.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        data = line.split()

        phones.append(RadioPhone(data[0], data[1], int(data[2]), data[3], True if data[4] == "Yes" else False))

for i in phones:
    print(i)

# і вивести у текстовий файл: - всі телефони, посортовані за ціною із зазначенням загальної суми;


sorted = sorted(phones, key=lambda x: int(x.price))

with open("sorted_price.txt", "w+") as file:
    file.write("Sorted phones with price\n")
    for i in sorted:
        file.write(str(i))
        file.write('\n')

# - радіотелефони з автовідповідачем

with open("sorted_price.txt", "a+") as file:
    file.write("Phones with self answer\n")
    for i in sorted:
        if type(i) is RadioPhone:
        # if int(i.price) < 200:
            if i.selfAnswer == "Yes":
                file.write(str(i))
                file.write('\n')


# # task 2
# Визначити два типи «Стіл» (розмір, матеріал, ціна) та «Стілець»(матеріал, ціна).

from tokenize import tabsize


class Table (object):
    def __init__(self, size, material, price):
        self.size = size
        self.material = material
        self.price = price

    def __str__(self):
        return f'{self.size} {self.material} table'


class Chair (object):
    def __init__(self, material, price):
        self.material = material
        self.price = price

    def __str__(self):
        return f'{self.material} chair'

# Визначити тип «Набір меблів», що містить назву, стіл, набір стільців, їх кількість .


class Set:
    def __init__(self, table, setChairs, amount):
        self.table = table
        self.setChairs = setChairs
        self.amount = amount

    def __str__(self):
        return f"{self.table} {self.setChairs} {self.amount}"

    def price(self):
        return self.table.price + self.setChairs.price*self.amount

# В текстовому файлі задано дані про 10 столів та крісел.  Зчитати ці дані в масиви.


tables = []
chairs = []
with open("set.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        data = line.split()
        if len(data) == 3:
            tables.append(Table(data[0], data[1], int(data[2])))

        if len(data) == 2:
            chairs.append(Chair(data[0], int(data[1])))

# for i in tables:
#     print (i)
# for i in chairs:
#     print (i)


# За введеним матеріалом, кількістю стільців та розміром стола утворити набір меблів, який зберегти у
# відповідний масив наборів. Видрукувати у файл дані про утворений набір і його вартість.
sets = []
totalprice = 0
print("1 - WOOD\n2 - STEEL")
tabMater = input("Type a number of material of table: ")
if tabMater == '1':
    tabMater = 'wood'
else:
    tabMater = 'steel'
print("1 - Small\n2 - Medium\n3 - Big")
tabSize = input("Type a number of material of table: ")
if tabSize == '1':
    tabSize = 'small'
elif tabSize == '2':
    tabSize = 'medium'
else:
    tabSize = 'big'

numbChirs = int(input("How many chairs to add? "))
for i in tables:
    for j in chairs:
        if i.material == tabMater:
            if i.size == tabSize:
                if i.material == j.material:
                    s = Set(i, j, numbChirs)
                    sets.append(s)
                    totalprice += s.price()
                    # totalprice += int(i.price)
                    # for _ in range(int(numbChirs)):
                    #     totalprice += int(j.price)
                    # sets.append(Set(i, j, numbChirs))
tables.pop(tables.index(i)-1)
with open('order.txt', 'w+') as f:
    f.write(str(sets[0]))
    f.write(str(totalprice))

# З рештою меблів утворити можливі набори меблів (за матеріалом) і додати їх до масиву наборів.
# Видрукувати у файл2 утворені набори .
with open("order2.txt", "w+")as f:
    for i in tables:
        for j in chairs:
            newprice = 0
            for _ in range(int(numbChirs)):
                newprice+=int(j.price)
            newprice+=int(i.price)
            sets.append(Set(i, j, numbChirs))
            f.write(str(Set(i, j, numbChirs)))
            f.write(str(newprice))
            f.write("\n")
            tables.pop(tables.index(i)-1)
    for i in sets:
        print(i)
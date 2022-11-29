# task 1
# Визначити абстрактний тип «телефон» (назва, фірма, ціна). 
# Визначити 2 похідні від нього типи: «мобільний телефон» (колір, об’єм пам’яті ), «радіотелефон» (радіус дії, наявність автовідповідача )
# У двох текстових файлах задано дані про телефони двох різних фірм.
# Зчитати ці дані в один масив  і вивести у текстовий файл:
# - всі телефони, посортовані за ціною із зазначенням загальної суми; 
# - радіотелефони з автовідповідачем


class Phone:
    def __init__(self, name, firm, price: int):
        self.name = name
        self.firm = firm
        self.price = price

    def __str__(self):
        return f"{self.name} {self.firm} {self.price}"


class Cellphone(Phone):
    def __init__(self, name, firm, price, colour, memory_capacity):
        super().__init__(name, firm, price)
        self.colour = colour
        self.memory_capacity = memory_capacity

    def __str__(self):
        return f"{super().__str__()} {self.colour} {self.memory_capacity}"


class Radiotelephone(Phone):
    def __init__(self, name, firm, price, radius_of_action, answering_machine):
        super().__init__(name, firm, price)
        self.radius_of_action = radius_of_action
        self.answering_machine = answering_machine

    def __str__(self):
        return f"{super().__str__()} {self.radius_of_action} {self.answering_machine}"


phones = []
with open("./data/cellphone.txt") as file:
    for line in file:
        cell = line.split()
        phones.append(Cellphone(cell[0], cell[1], cell[2], cell[3], cell[4]))

with open("./data/radiophone.txt") as file:
    for line in file:
        radio = line.split()
        phones.append(Radiotelephone(radio[0], radio[1], radio[2], radio[3], radio[4]))
for i in phones:
    print(i)

sort = sorted(phones, key=lambda x: x.price)

with open("./data/output.txt", "w") as file:
    file.write("============ Sorted by price ============\n")
    for i in sort:
        file.write(str(i))
        file.write('\n')

    total = 0.0
    for i in sort:
        total = total + float(i.price)
    file.write('Total: $ ' + str(total))
    file.write('\n')

    file.write("=== Radiophone with answering_machine ===\n")
    for i in sort:
        if type(i) == Radiotelephone and i.answering_machine == 'AM':
            file.write(str(i))
            file.write('\n')

# task 2
# Визначити два типи «Стіл» (розмір, матеріал, ціна) та «Стілець»(матеріал, ціна).
# Визначити тип «Набір меблів», що містить назву, стіл, набір стільців, їх кількість .

# В текстовому файлі задано дані про 10 столів та крісел.  Зчитати ці дані в масиви.
# За введеним матеріалом, кількістю стільців та розміром стола утворити набір меблів, який зберегти у відповідний масив наборів. 
# Видрукувати у файл дані про утворений набір і його вартість. 
# З рештою меблів утворити можливі набори меблів (за матеріалом) і додати їх до масиву наборів. Видрукувати у файл2 утворені набори .        

import random
import string


class Table:
    def __init__(self, size, material, price):
        self.size = size
        self.material = material
        self.price = price

    def __str__(self):
        return f"{self.size} {self.material} {self.price}"


class Chair:
    def __init__(self, material, price):
        self.material = material
        self.price = price

    def __str__(self):
        return f"{self.material} {self.price}"


class SetFurniture:
    def __init__(self, name, table, set_of_chairs, number_sets):
        self.name = name
        self.table = table
        self.set_of_chairs = set_of_chairs
        self.number_sets = number_sets

    def __str__(self):
        return f"{self.name} {self.table} {self.set_of_chairs} {self.number_sets}"


tables = []
chairs = []
with open("./data/furniture.txt") as f:
    for line in f:
        furniture = line.split()
        if len(furniture) == 3:
            tables.append(Table(furniture[0], furniture[1], furniture[2]))
        else:
            chairs.append(Chair(furniture[0], furniture[1]))
for i in tables:
    print(i)
for j in chairs:
    print(j)

MATERIAL = ['wood', 'glass', 'velor', 'leather']
SET_OF_CHAIRS = ['2', '3', '1']
SIZE = ['150x60', '170x70']

set_of_furnitures = []
total = 0.0
for i in range(4):
    letters = string.ascii_lowercase
    name = ''.join(random.choices(letters, k=5))
    table = random.choice(SIZE)
    set_of_chairs = random.choice(MATERIAL)
    number_sets = random.choice(SET_OF_CHAIRS)
    set_of_furniture = SetFurniture(name, table, set_of_chairs, number_sets)
    set_of_furnitures.append(set_of_furniture)

with open("./data/furniture2.txt", 'w') as f:
    f.write("========== set_of_furnitures ==========\n")
    for set_of_furniture in set_of_furnitures:
        f.write(str(set_of_furniture))
        f.write('\n')

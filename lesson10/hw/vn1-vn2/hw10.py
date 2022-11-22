# task 1
# Визначити абстрактний тип «телефон» (назва, фірма, ціна).
# Визначити 2 похідні від нього типи: «мобільний телефон» (колір, об’єм пам’яті ),
# «радіотелефон» (радіус дії, наявність автовідповідача )

# У двох текстових файлах задано дані про телефони двох різних фірм.
# Зчитати ці дані в один масив  і вивести у текстовий файл:
# - всі телефони, посортовані за ціною із зазначенням загальної суми;
# - радіотелефони з автовідповідачем

class Phone:
    def __init__(self, type, brand, price):
        self.type = type
        self.brand = brand
        self.price = price

class MobilePhone(Phone):
    def __init__(self, type, brand, price, color, memory):
        super().__init__(type, brand, price)
        self.color = color
        self.memory = memory

class RadioPhone(Phone):
    def __init__(self, type, brand, price, coverage_area, answerphone):
        super().__init__(type, brand, price)
        self.coverage_area = coverage_area
        self.answerphone = answerphone

all_phones = []
with open('samsung.txt', 'r') as file:
    for line in file:
        list = line.split()
        if list[0] == 'mobile':
            a = MobilePhone(*list)
        elif list[0] == 'radio':
            a = RadioPhone(*list)
        all_phones.append(a)
with open('nokia.txt', 'r') as file:
    for line in file:
        list = line.split()
        if list[0] == 'mobile':
            a = MobilePhone(*list)
        elif list[0] == 'radio':
            a = RadioPhone(*list)
        all_phones.append(a)

sorted_list = sorted(all_phones, key=lambda x: int(x.price))
total_price = 0
with open('all_phones.txt', 'w+') as file:
    for y in sorted_list:
        total_price += int(y.price)
        file.writelines(f"{y.type}, {y.brand}, {y.price}\n")
    file.write(f"Total price {total_price}")

with open('radio_phones.txt', 'w') as file:
    for y in sorted_list:
        if isinstance(y, RadioPhone):
            if y.answerphone == "yes":
                file.write(f"{y.type} {y.brand} {y.price} {y.coverage_area} {y.answerphone} \n")

# task 2
# Визначити два типи «Стіл» (розмір, матеріал, ціна) та «Стілець»(матеріал, ціна).
# Визначити тип «Набір меблів», що містить назву, стіл, набір стільців, їх кількість .

# В текстовому файлі задано дані про 10 столів та крісел.  Зчитати ці дані в масиви.
# За введеним матеріалом, кількістю стільців та розміром стола утворити набір меблів,
# який зберегти у відповідний масив наборів. Видрукувати у файл дані про утворений набір
# і його вартість.
# З рештою меблів утворити можливі набори меблів (за матеріалом) і додати їх до масиву наборів.
# Видрукувати у файл2 утворені набори .

class Table:
    def __init__(self, size, material, price):
        self.size = size
        self.material = material
        self.price = price

class Chair:
    def __init__(self, material, price):
        self.material = material
        self.price = price

class FurnitureSet:
    def __init__(self, name, table, chairs_set, chairs_quantity):
        self.name = name
        self.table = table
        self.chairs_set = chairs_set
        self.chairs_quantity = chairs_quantity

all_items = []
with open('file_1.txt', 'r') as file:
    for line in file:
        items_list = line.split()
        if items_list[0] == "table":
            t = Table(items_list[1], items_list[2], items_list[3])
            all_items.append(t)
        elif items_list[0] == "chair":
            c = Chair(items_list[1], items_list[2])
            all_items.append(c)

all_furniture_sets = []
set_number = 0
for i in all_items:
    ch_set = []
    if isinstance(i, Table):
        set_number += 1
        for j in all_items:
            if isinstance(j, Chair):
                if j.material == i.material:
                    for l in range(int(i.size)):
                        ch_set.append(j)
        s = FurnitureSet(f"Furniture set {set_number}", i, ch_set, f"quantity of chairs: {i.size}")
        all_furniture_sets.append(s)
with open('file_2.txt', 'w') as file:
    for line in all_furniture_sets:
        set_price = 0
        file.write(f"{line.name}:\ntable of {line.table.material} for {line.table.size} persons,\n")
        set_price += int(line.table.price)
        for chair in line.chairs_set:
            file.write(f"chair of {chair.material},\n")
            set_price += int(chair.price)
        file.write(f"{line.chairs_quantity}\nFurniture set price = {set_price}\n")

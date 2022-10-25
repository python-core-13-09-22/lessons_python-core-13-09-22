# # task 1
# Визначити тип: «`Ягода`» (назва, колір, список вітамінів) та тип  «`Компот`»(назва, кількість ягід, 
# список ягід).

from os import set_blocking
from random import randrange


class Berry ():
    def __init__(self, name, color, vitamins):
        self.name = name
        self.color = color
        self.vitamins = vitamins
    def __str__(self):
        return f"{self.name}"

class Kompot(Berry):
    def __init__ (self, num_berries, lst_berries):
        self.num_berries = num_berries
        self.lst_berries = lst_berries
    def __str__(self):
        return f"There is {self.num_berries} berries: {self.lst_berries}"


        

# Створити масив з 10 різних ягід.  

strawberry = Berry('strawberry', "red", "B")
ruspberry = Berry('ruspberry', 'red', 'A' )
blackberry = Berry('blackberry', 'black', 'P') 
blueberry = Berry("blueberry", 'blue', 'K')
goji = Berry('goji', 'red', 'A')
bilberry = Berry('bilberry', 'blue', 'C')
cranberries = Berry('cranberries', 'red', 'C')
grape = Berry('grape', 'green', 'K')
black_currant = Berry('black_currant', 'black', 'C')
red_currant = Berry('red_currant', 'red', 'C')

lst_berries = [strawberry, ruspberry, blackberry, blueberry, goji, bilberry, cranberries, grape, black_currant, red_currant]

# Утворити стільки компотів, скільки різних кольорів ягід є у списку.

colors = []
for berry in lst_berries:
    if berry.color not in colors:
        colors.append(berry.color) 

# Заповнити таким чином масив компотів і вивести його.
kompots = []
for i,x in enumerate(colors):
    print(f'{i+1} is {x} color kompot')
    kompots.append(x)
    
# Для кожного компоту видрукувати список вітамінів. 
kompot_vitamins = []
all_vitamins = {}
for col in kompots:
    for berry in lst_berries:
        if col == berry.color:
            if berry.vitamins not in kompot_vitamins:
                kompot_vitamins.append(berry.vitamins)
    all_vitamins[col]=kompot_vitamins
    kompot_vitamins = []

print(all_vitamins)


# # task 2
# Визначити тип «`Шпаргалка`»( предмет,номер ) та похідні від нього типи  «`Паперова`»
# (розмір, місце переховування) та «`Електронна`» (назва носія).
class CheatSheet():
    def __init__ (self, subject, number):
        self.subject = subject
        self.number = number


class PaperCheatSheet(CheatSheet):
    def __init__(self, subject, number, size, hide):
        super().__init__(subject, number)
        self.size = size
        self.hide = hide
    def __str__ (self):
        return f"Cheat Sheet on {self.subject}, number {self.number}, paper type, {self.size} size, hiidden {self.hide}"

class ElectronicCheatSheet(CheatSheet):
    def __init__ (self, subject, number, hub):
        super().__init__(subject, number)
        self.hub = hub

    def __str__(self):
        return f"Cheat Sheet on {self.subject}, number {self.number}, electronic type stored on {self.hub}"

# Визначити тип «`Студент`»(ПІП, група, список шпаргалок)
class Student(CheatSheet):
    def __init__(self, name, group, cheatSheet):
        self.name = name
        self.group = group
        self.lst_CheatSheet = cheatSheet

    def __str__(self):
        return f"{self.name}, from {self.group} group, with {self.lst_CheatSheet}"

    def ShowCheatStr(self):
        return f"{self.lst_CheatSheet}"

    def ShowCheat(self):
        return self.lst_CheatSheet
# Створити список студентів та додати їм шпаргалки різних типів.
lst_students = []

students = ["Mark", "Anthony", "Andrew", "Stewen", "Nicola", "Micky", "Jim", "David", "Angela", "Suzana", "Pamela", "Stefany"]
subjects = ["Math", "Biology", "English", "Ukrainian", "Geography", "Science", "Chemesry"]
places_of_hide = ["in pocket", "in socks", "in sleeves", "under the table"]
hubs = ["mobile", "tablet", "laptop", "iWatch", "Samsung Watch"]
size = ["big", 'medium', 'small']

for _ in range (randrange(0,10)):
    lst_students.append(Student(students[randrange(0,11)], randrange(1,20), PaperCheatSheet (subjects[randrange(0,6)], randrange(0,50), size[randrange(0,2)], places_of_hide[randrange(0,4)])))
for _ in range (randrange(0,10)):
    lst_students.append(Student(students[randrange(0,11)], randrange(1,20), ElectronicCheatSheet (subjects[randrange(0,6)], randrange(0,50), hubs[randrange(0,4)])))
for i in lst_students:
    print(i)

# Видрукувати список всіх шпаргалок, посортованих за предметом та номерами. 

all_cheatSheets = []
for stud in lst_students:
    all_cheatSheets.append(stud.ShowCheat())
sort = sorted(all_cheatSheets, key = lambda x: (x.subject, x.number))
for i in sort:
    print (i)

# # Вивести всі електронні шпаргалки на носіях «комп» та їх кількість.
laptop_cheat = []
all_cheatSheets = []
for stud in lst_students:
    all_cheatSheets.append(stud.ShowCheatStr())
count = 0
for sheet in all_cheatSheets: 
    if "laptop" in sheet:
        laptop_cheat.append(sheet)
        count+=1
if count > 0:
    print(laptop_cheat)
print(f"There is {count} cheat sheets on laptop")


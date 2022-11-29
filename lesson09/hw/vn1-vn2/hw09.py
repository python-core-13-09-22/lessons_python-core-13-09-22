# task 1
# Визначити тип: «`Ягода`» (назва, колір, список вітамінів) та тип  «`Компот`»(назва, кількість
# ягід, список ягід).

# Створити масив з 10 різних ягід.
# Утворити стільки компотів, скільки різних кольорів ягід є у списку.
# Заповнити таким чином масив компотів і вивести його.
# Для кожного компоту видрукувати список вітамінів.

class Berry:
    def __init__(self, name, color, vitamins_list):
        self.name = name
        self.color = color
        self.vitamins_list = vitamins_list


class Juice:
    def __init__(self, name, berries_quantity, berry_list):
        self.name = name
        self.berries_quantity = berries_quantity
        self.berry_list = berry_list


b1 = Berry("Вишня", "Червоний", ["C", "A"])
b2 = Berry("Малина", "Червоний", ["C", "A", "В"])
b3 = Berry("Полуниця", "Червоний", ["C", "A"])
b4 = Berry("Вишня", "Жовтий", ["C", "A"])
b5 = Berry("Смородина", "Червоний", ["C", "A", "D"])
b6 = Berry("Смородина", "Чьорний", ["C", "A"])
b7 = Berry("Чьорниця", "Синій", ["C", "A", "B"])
b8 = Berry("Шипшина", "Червоний", ["C", "A", "D"])
b9 = Berry("Черешня", "Червоний", ["C", "A"])
b10 = Berry("Черешня", "Жовтий", ["C", "A"])


berries_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]
colors_list = []
for b in berries_list:
    colors_list.append(b.color)
colors_set = set((colors_list))
juice_list = []
for c in colors_set:
    berries_quantity = 0
    berry_list = []
    for b in berries_list:
        if b.color == c:
            berry_list.append(b.name)
            berries_quantity += 1
    j = Juice(c, berries_quantity, berry_list)
    juice_list.append(j)
for k in juice_list:
    print(f"Назва компоту: {k.name}, він містить {k.berries_quantity} ягід:")
    vitamins = []
    for b in k.berry_list:
        print(f"ягода {b}")
        for v in berries_list:
            if v.name == b and v.color == k.name:
                vitamins.extend(v.vitamins_list)
    vitamins_set = set((vitamins))
    print(f"Список вітамінів {vitamins_set}")


# task 2
# Визначити тип «`Шпаргалка`»( предмет,номер ) та похідні від нього типи  «`Паперова`»(розмір ,
# місце переховування) та «`Електронна`» (назва носія).
# Визначити тип «`Студент`»(ПІП, група, список шпаргалок).

# Створити список студентів та додати їм шпаргалки різних типів.
# Видрукувати список всіх шпаргалок, посортованих за предметом та номерами.
# Вивести всі електронні шпаргалки на носіях «комп» та їх кількість.

class Crib:
    def __init__(self, subject, number):
        self.subject = subject
        self.number = number

class PaperCrib(Crib):
    def __init__(self, subject, number, size, hiding):
        super().__init__(subject, number)
        self.size = size
        self.hiding = hiding

class DigitalCrib(Crib):
    def __init__(self, subject, number, device):
        super().__init__(subject, number)
        self.device =device

class Student:
    def __init__(self, name, group, crib_list):
        self.name = name
        self.group = group
        self.crib_list = crib_list


N = int(input(f"Скількі студентів має бути?: "))
students_list = []
all_crib_list = []
crib_quantity = 0
for i in range(N):
    name = input(f"Напиши ім'я студента: ")
    group = int(input(f"Напиши номер групи студента на ім'я {name}: "))
    number = int(input(f"Скількі шпаргалок надати студенту {name}?: "))
    crib_list = []
    for y in range(number):
        subject = input(f"З якого предмету надати {y + 1} шпаргалку студенту на ім'я {name}?: ")
        choice = int(input(f"Паперову (введіть 1) чи цифрову (введіть 2)?: "))
        if choice == 1:
            size = input(f"Якого розміру шпаргалка (введіть число в см)?: ")
            hiding = input(f"Де її сховати?: ")
            crib = PaperCrib(subject, number, size, hiding)
        if choice == 2:
            device = input(f"На компьютері чи у телефоні?: ")
            crib = DigitalCrib(subject, number, device)
        crib_list.append(crib)
    student = Student(name, group, crib_list)
    students_list.append(student)
for s in students_list:
    print(f"Студент {s.name}")
    for c in s.crib_list:
        all_crib_list.append(c)
for sbj in all_crib_list:
    try:
        if sbj.device == "comp":
            crib_quantity += 1
            print(f"Цифрова шпаргалка по предмету {sbj.subject} на носію {sbj.device}")
    except:
        continue
print(f"Кількість цифрових шпаргалок {crib_quantity}")

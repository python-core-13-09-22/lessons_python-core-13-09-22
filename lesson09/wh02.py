#
# # task 2
# Визначити тип «`Шпаргалка`»( предмет,номер ) та похідні від нього типи
# «`Паперова`»(розмір , місце переховування) та
# «`Електронна`» (назва носія).
# Визначити тип «`Студент`»(ПІП, група, список шпаргалок).
#
# Створити список студентів та додати їм шпаргалки різних типів.
# Видрукувати список всіх шпаргалок, посортованих за предметом та номерами.
# Вивести всі електронні шпаргалки на носіях «комп» та їх кількість.
import random
import string


class Chit:
    def __init__(self, subject, number):
        self.subject = subject
        self.number = number
    def __str__(self):
        return f"{self.subject} {self.number}"
    def __repr__(self):
        return f"{self.subject} {self.number}"

class PaperChit(Chit):
    def __init__(self, subject, number, size, hiding_place):
        super().__init__(subject, number)
        self.size = size
        self.hiding_place = hiding_place
    def __str__(self):
        return f"{super().__str__()} {self.size} {self.hiding_place}"

class ElectronicChit(Chit):
    def __init__(self, subject, number, media_name):
        super().__init__(subject, number)
        self.media_name = media_name
    def __str__(self):
        return f"{super().__str__()} {self.media_name}"

class Student:
    def __init__(self, name, group, chips):
        self.name = name
        self.group = group
        self.chips = chips
    def __str__(self):
        s = f"{self.name} {self.group}\n"
        for chip in self.chips:
            s += f"\t{chip}\n"
        return s


SUBJECTS = ["matan", "fizra", "informatics"]
HIDING_PLACE = ["рука", "голова", "нога"]
MEDIAS = ["PC", "Phone"]
GROUPS = ["PMi11", "PMa12"]

if __name__ == "__main__":
    students = []
    for _ in range(random.randint(5, 10)):
        letters = string.ascii_lowercase
        name = ''.join(random.choices(letters, k=10))
        group = random.choice(GROUPS)
        chits = []
        for i in range(random.randint(5, 10)):
            subject = random.choice(SUBJECTS)
            number = random.randint(1, 99)
            if i % 2:
                hiding_place = random.choice(HIDING_PLACE)
                chit = PaperChit(subject, number, random.randint(1,10), hiding_place)
            else:
                media_name = random.choice(MEDIAS)
                chit = ElectronicChit(subject, number,media_name)
            chits.append(chit)
        student = Student(name, group, chits)
        students.append(student)
    chits = []

    with open("../lesson10/data/students.txt",mode="a+", encoding='utf-8') as file:

        for student in students:
            print(student)
            file.write(student.__str__())
            chits.extend(student.chips)
    print(chits)
    c = sorted(chits, key=lambda x: (x.subject, x.number))
    for chit in c:
        print(chit)
    for i in range(len(chits)-1):
        for j in range(i+1, len(chits)):
            if chits[i].subject > chits[j].subject:
                chits[i], chits[j] = chits[j], chits[i]
            elif chits[i].subject == chits[j].subject:
                if chits[i].number > chits[j].number:
                    chits[i], chits[j] = chits[j], chits[i]
    print(chits)
    for chit in chits:
        print(chit)
    print()
    count = 0
    for chit in chits:
        if type(chit) == ElectronicChit and chit.media_name == MEDIAS[0]:
            count +=1
            print(chit)
    print(count)
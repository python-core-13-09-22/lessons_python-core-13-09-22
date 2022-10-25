class Shparhalka:
    def __init__(self, predmet, number):
        self.predmet = predmet
        self.number = number

class Paperova(Shparhalka):
    def __init__(self, misze, rozmir, predmet, number):
        super().__init__(predmet, number)
        self.rozmir = rozmir
        self.misze = misze

class Elektronna(Shparhalka):
    def __init__(self, predmet, number, nosiy):
        super().__init__(predmet, number)
        self.nosiy = nosiy

class Student:
    def __init__(self, fullname, group, spysok_spargalok):
        self.fname = fullname
        self.group = group
        self.spysok_spargalok = spysok_spargalok


sp1 = Paperova(predmet="Matematyla", number=21, rozmir=15, misze='liva_kyshenya')

sp2 = Elektronna(predmet="Istoriya", number=35, nosiy="komp")

sp3 = Paperova(predmet="Literatura", number=45, rozmir=15, misze='rukav')

sp4 = Elektronna(predmet="Fizyka", number=14, nosiy="telefon")

sp5 = Paperova(predmet="Matematyla", number=47, rozmir=11, misze='liva_kyshenya')

sp6 = Paperova(predmet="Fizyka", number=32, rozmir=19, misze='prava_kyshenya')

sp7 = Elektronna(predmet="Istoriya", number=37, nosiy="komp")

sp8 = Elektronna(predmet="Literatura", number=28, nosiy="komp")

sp9 = Paperova(predmet="Matematyla", number=16, rozmir=23, misze='remin')

sp10 = Elektronna(predmet="Istoriya", number=63, nosiy="smart_hodynnyk")

vsi_sparhalky = [sp1, sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9, sp10]



student_1 = Student(fullname="Ivanov Ivan Ivanovych", group=1, spysok_spargalok=[sp1, sp3, sp6])

student_2 = Student(fullname="Vasyliv Vasyl Vasylyovych", group=3, spysok_spargalok=[sp2, sp4, sp9])

student_3 = Student(fullname="Ronovych Roman Romanovych", group=2, spysok_spargalok=[sp3, sp8, sp7])

student_4 = Student(fullname="Valentyniv Valentyn Valentynovych", group=2, spysok_spargalok=[sp1, sp3, sp4])

student_5 = Student(fullname="Chewchenko Taras Hryhorovych", group=3, spysok_spargalok=[sp1, sp5, sp10])

student_6 = Student(fullname="Franko Ivan Yakovych", group=1, spysok_spargalok=[sp10, sp1, sp6])

student_7 = Student(fullname="Nosatova Anastasiya Andrijivna", group=3, spysok_spargalok=[sp1, sp3, sp9])

student_8 = Student(fullname="Saluznyj Valerij Fedorovych ", group=2, spysok_spargalok=[sp1, sp4, sp7])

student_9 = Student(fullname="Volodymyriv Volodymyr Volodymyrovych", group=1, spysok_spargalok=[sp1, sp8, sp2])

student_10 = Student(fullname="Roslyi Mykola Leonidovych", group=3, spysok_spargalok=[sp10, sp3, sp4])

spysok_studentiv = [student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8, student_9, student_10]



for i in range(len(vsi_sparhalky)):
    for j in range(len(vsi_sparhalky)):
        if vsi_sparhalky[i].number < vsi_sparhalky[j].number:
            vsi_sparhalky[i], vsi_sparhalky[j] = vsi_sparhalky[j], vsi_sparhalky[i]
        else:
           pass

for i in vsi_sparhalky:
    print(f"Шпаргалка номер: {i.number}. Предмет: {i.predmet}")

for i in vsi_sparhalky:
    if i.__class__ == Elektronna:
        if i.nosiy == "komp":
            print(i.predmet, i.number, i.nosiy)
        else:
            pass
    else:
        pass

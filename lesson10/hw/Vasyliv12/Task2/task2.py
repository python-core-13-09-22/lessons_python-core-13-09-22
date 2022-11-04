# Визначити два типи «Стіл» (розмір, матеріал, ціна) та «Стілець»(матеріал, ціна).
# Визначити тип «Набір меблів», що містить назву, стіл, набір стільців, їх кількість .

# В текстовому файлі задано дані про 10 столів та крісел. Зчитати ці дані в масиви.
# За введеним матеріалом, кількістю стільців та розміром стола утворити набір меблів,
# який зберегти у відповідний масив наборів. Видрукувати у файл дані про утворений набір і його вартість.
# З рештою меблів утворити можливі набори меблів (за матеріалом)
# і додати їх до масиву наборів. Видрукувати у файл 2 утворені набори .

class Table:
    def __init__(self, size, material, price):
        self.size = size
        self.material = material
        self.price = price


class Chair:
    def __init__(self, material, price):
        self.material = material
        self.price = price

class NabirMebliv:
    def __init__(self, name, numtable, numchair):
        self.name = name
        self.numtable = numtable
        self.numchair = numchair

oll = 'oll.txt'
sakas = 'vach_sakas.txt'
table_massive = []
chair_massive = []
with open(oll, 'r') as meblya:
    for ryadok in meblya:
        ryadok = ryadok.split()
        print(ryadok)
        if ryadok[0] == 'table':
            table_massive.append(ryadok)
        elif ryadok[0] == 'chair':
            chair_massive.append(ryadok)
        else:
            pass
print(table_massive)
print(chair_massive)
choice = int(input(''' Виберіть матеріал набора:
Дуб - 1
Осика - 2
Сосна - 3
ДСП - 4
Пластик - 5 :
'''))
dovsyna = int(input("Введіть довжину стола: "))
shyryna = int(input("Введіть ширину стола: "))
n_chair = int(input("Введіть кількість стільчиків в наборі: "))

match choice:
    case 1:
        t_choice = table_massive[0]
        ch_choice = chair_massive[0]
    case 2:
        t_choice = table_massive[1]
        ch_choice = chair_massive[1]
    case 3:
        t_choice = table_massive[2]
        ch_choice = chair_massive[2]
    case 4:
        t_choice = table_massive[3]
        ch_choice = chair_massive[3]
    case 5:
        t_choice = table_massive[4]
        ch_choice = chair_massive[4]


t1 = Table(size=f'{shyryna}x{dovsyna}', material=t_choice[1], price=((shyryna * dovsyna)/10)*int(t_choice[2]))
ch1 = Chair(material=ch_choice[1], price=ch_choice[2])
nabir1 = NabirMebliv(name='Nabir 1', numtable=t1, numchair=n_chair)




print(t1.price, t1.material, t1.size)

with open(sakas, 'w') as danni:
    danni.write(f'''
Your order:
Table: material - {t1.material}, dimensions - {t1.size}, price for 10 cm. - {t_choice[2]},  the price of the table - {t1.price}
Chairs: material - {ch1.material}, price for 1 - {ch1.price}, total price - {int(ch1.price) * n_chair}   

Total cost of the order: {(int(ch1.price) * n_chair)+t1.price}
 ''')
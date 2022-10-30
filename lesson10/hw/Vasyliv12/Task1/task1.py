# Визначити абстрактний тип «телефон» (назва, фірма, ціна). Визначити 2 похідні від нього типи: «мобільний телефон» (колір, об’єм пам’яті ),
# «радіотелефон» (радіус дії, наявність автовідповідача )

# У двох текстових файлах задано дані про телефони двох різних фірм.
#  Зчитати ці дані в один масив і вивести у текстовий файл:
# всі телефони, посортовані за ціною із зазначенням загальної суми;
# радіотелефони з автовідповідачем

class Phone:
    def __init__(self, name, firm, price):
        self.name = name
        self.firm = firm
        self.price = price

class MobilPhone(Phone):
    def __init__(self, name, firm, price, color, memory):
        super().__init__(name, firm, price)
        self.color = color
        self.memory = memory

class RadioPhone(Phone):
    def __init__(self, name, firm, price, workradius, autoanswer):
        super().__init__(name, firm, price)
        self.workradius = workradius
        self.autoanswer = autoanswer

samsung = 'Samsung.txt'
nokia = 'Nokia.txt'
new_file = 'new_file.txt'
ollPhone = []
price_sum = 0
with open(samsung, 'r') as samsung_file:
    for i in samsung_file:
        i = i.split()
        print(i)
        if i[0] == 'mobil':
            i = MobilPhone(name=i[1], firm=i[2], price=i[3], color=i[4], memory=i[5])
        elif i[0] == 'radio':
            i = RadioPhone(name=i[1], firm=i[2], price=i[3], workradius=i[4], autoanswer=i[5])
        else:
            pass
        ollPhone.append(i)

with open(nokia, 'r') as nokia_file:
    for i in nokia_file:
        i = i.split()
        print(i)
        if i[0] == 'mobil':
            i = MobilPhone(name=i[1], firm=i[2], price=i[3], color=i[4], memory=i[5])
        elif i[0] == 'radio':
            i = RadioPhone(name=i[1], firm=i[2], price=i[3], workradius=i[4], autoanswer=i[5])
        else:
            pass
        ollPhone.append(i)

with open(new_file, 'w') as file:
    for i in range(len(ollPhone)):
        for j in range(len(ollPhone)):
            if int(ollPhone[i].price) < int(ollPhone[j].price):
                ollPhone[i], ollPhone[j] = ollPhone[j], ollPhone[i]
            else:
                pass

    for a in ollPhone:
        if a.__class__ == MobilPhone:
            file.write(f"{a.firm} {a.name}, {a.price}, {a.color}, {a.memory} \n")
            price_sum = price_sum + int(a.price)
        elif a.__class__ == RadioPhone:
            file.write(f"{a.firm} {a.name}, {a.price}, {a.workradius}, {a.autoanswer} \n")
            price_sum = price_sum + int(a.price)

    file.write(f"\nThe total cost of all phones is: {str(price_sum)}\n")

    file.write("\nRadio telephones with answering machine:\n")
    for a in ollPhone:
        if a.__class__ == MobilPhone:
            pass
        elif a.__class__ == RadioPhone:
            if a.autoanswer == 'yes':
                file.write(f"{a.firm} {a.name}, {a.price}, {a.workradius}, {a.autoanswer} \n")
            else:
                pass


for i in ollPhone:
    print(i.name, i.firm, i.price)





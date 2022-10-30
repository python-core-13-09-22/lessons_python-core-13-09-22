# task 1
# Визначити абстрактний тип «телефон» (назва, фірма, ціна). 
# Визначити 2 похідні від нього типи: «мобільний телефон» (колір, об’єм пам’яті ), «радіотелефон» (радіус дії, наявність автовідповідача )
# У двох текстових файлах задано дані про телефони двох різних фірм.
# Зчитати ці дані в один масив  і вивести у текстовий файл:
# - всі телефони, посортовані за ціною із зазначенням загальної суми; 
# - радіотелефони з автовідповідачем

class Phone:
    def __init__(self, name, firm, price):
        self.name = name
        self.firm = firm
        self.price = price
    def __str__(self):
        return f"{self.name} {self.name} {self.price}"
    def __repr__(self):
        return f"{self.name} {self.name} {self.price}"    
        
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
        
# with open("data/output.txt",mode="a+", encoding='utf-8') as file:
with open("..lesson10/hw/data/cellphone.txt") as file:
    for line in file:
        print(line.strip())
        

# phones = []
# with open("/data/cellphone.txt") as file:
#      while True:
#         line = file.readline()
#         if not line:
#             break
#         data = line.split( )
#         phones.append(Cellphone)  
# print(phones)     

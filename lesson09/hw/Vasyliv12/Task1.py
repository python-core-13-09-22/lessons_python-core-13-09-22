
class Yahoda:
    def __init__(self, name, color, vitaminy):
        self.name = name
        self.color = color
        self.vitaminy = vitaminy

yahody = []

cshereshnya = Yahoda(name="Cshereshnya", color="red", vitaminy=["A", "B", "C"])
yahody.append(cshereshnya)

smorodyna = Yahoda(name="Smorodyna", color="black", vitaminy=["D", "E", "D"])
yahody.append(smorodyna)

malyna = Yahoda(name="Malyna", color="pink", vitaminy=["F", "G", "zynk"])
yahody.append(malyna)

kavun = Yahoda(name="Kavun", color="green", vitaminy=["B1", "omega", "C"])
yahody.append(kavun)

lohyna = Yahoda(name="Lohyna", color="black", vitaminy=["A", "C", "E", "B"])
yahody.append(lohyna)

vyshnya = Yahoda(name="Vyshnya", color="red", vitaminy=["C2", "B2", "magnesium"])
yahody.append(vyshnya)

brusnytsya = Yahoda(name="Brusnytsya", color="violet", vitaminy=["B1", "calzium", "D"])
yahody.append(brusnytsya)

ozyna = Yahoda(name="Ozyna", color="black", vitaminy=["A", "A1", "B1"])
yahody.append(ozyna)

agrus = Yahoda(name="Agrus", color="green", vitaminy=["C", "B3", "D1"])
yahody.append(agrus)

busyna = Yahoda(name="Busyna", color="black", vitaminy=["B2", "magnesium", "C"])
yahody.append(busyna)

for i in yahody:
    print(i.name, i.color, i.vitaminy)
print("\n")
class Kompot(Yahoda):
    def __init__(self, name, berrys, spysok_yagody):
        self.name = name
        self.berrys = berrys
        self.spysok_yagody = spysok_yagody

spysoKompotiv = []

redKompot = Kompot(name="Black kompot", berrys=3, spysok_yagody=[busyna, agrus, lohyna] )
spysoKompotiv.append(redKompot)
blackKompot = Kompot(name="Black kompot", berrys=4, spysok_yagody=[cshereshnya, malyna, brusnytsya, vyshnya])
spysoKompotiv.append(blackKompot)
greenKompot = Kompot(name="Green kopot", berrys=3, spysok_yagody=[agrus, kavun, busyna])
spysoKompotiv.append(greenKompot)
pinkKompot = Kompot(name="Pink kompot", berrys=2, spysok_yagody=[malyna, cshereshnya])
spysoKompotiv.append(pinkKompot)


for i in spysoKompotiv:
    print(i.name)
    for j in i.spysok_yagody:
        print(f"Вітаміни ягоди {j.name}: {j.vitaminy}")
    print("\n")




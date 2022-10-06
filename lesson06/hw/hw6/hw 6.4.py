import random

s_posytyv = []
s_negatyv = []
ves_spysok = []

vidyemni = 0
pozytyvni = 0


for i in range(20):
    chyslo = random.randint(-5, 5)
    ves_spysok.append(chyslo)
    if chyslo < 0:
        s_negatyv.append(chyslo)
    elif chyslo > 0:
        s_posytyv.append(chyslo)
    else:
        continue


print(f"Повний сформований список: {ves_spysok}")
print(f"Список позитивних елементів: {s_posytyv}")
print(f"Список негативних елементів: {s_negatyv}")
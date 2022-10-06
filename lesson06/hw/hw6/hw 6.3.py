import random

spysok = []
vidyemni = 0
pozytyvni = 0
nulovi = 0
for i in range(20):
    chyslo = int(random.uniform(-5, 4))
    if chyslo < 0:
        vidyemni = vidyemni + 1
    elif chyslo > 0:
        pozytyvni = pozytyvni + 1
    else:
        nulovi = nulovi + 1

    spysok.append(chyslo)

print(f"Сформований список: {spysok}")
print(f" Кількість відємних чисел: {vidyemni}")
print(f"Кількість позитивних чисел: {pozytyvni}")
print(f"Кількість нульових чисел: {nulovi}")

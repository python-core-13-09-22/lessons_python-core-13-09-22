n = int(input(" Введіть висоту куба(рядків): "))
m = int(input(" Введіть ширину куба(стовбців): "))

kontur = input("Введіть символ контура: ")
zalyvka = input("Введіть символ заливки: ")

kub = []

for i in range(n):
    i = i + 1
    line = []
    for j in range(m):
        j = j + 1
        if i == 1 or i == n:
            element = kontur
        else:
            if j == 1 or j == m:
                element = kontur
            else:
                element = zalyvka

        line.append(element)
    kub.append(line)

for i in kub:
    for j in i:
        print(j, end="\t")
    print()








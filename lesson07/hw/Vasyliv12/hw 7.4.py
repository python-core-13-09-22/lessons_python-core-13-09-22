#  Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12),
#  і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь).

def season(a):
    if a.isnumeric():
        if 3 <= int(a) <= 5:
            print("Весна")
        elif 6 <= int(a) <= 8:
            print("Літо")
        elif 9 <= int(a) <= 11:
            print("Осінь")
        elif int(a) == 12 or int(a) == 1 or int(a) == 2:
            print("Зима")
        else:
            print("Ви ввели неправильне значення")
    else:
        print("Ви ввели неправильне значення")


misyats = input("Введіть номер місяця: ")

season(misyats)
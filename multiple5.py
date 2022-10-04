#Вводяться десять натуральних чисел більше 2. Порахувати, скільки серед них чисел, що кратні 5-ти.
# (не використовувати лісти)
count = 10
count_multiple_of_5 = 0
while count != 0:
    UserNumber = int(input('enter numbers larger 2 -   ' + str(count) + '  numbers left   '))
    count = count - 1

    if UserNumber % 5 == 0:
        count_multiple_of_5 = count_multiple_of_5 + 1
print(str(count_multiple_of_5) + '  numbers multiple of 5')




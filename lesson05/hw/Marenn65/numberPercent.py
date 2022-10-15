#Для чисел, що вводяться користувачем,
# визначити відсоток додатних та від’ємних чисел.
# При введенні числа 0 закінчити роботу.


positive = 0
negative = 0


while True:
    UserNumber = int(input('enter any number   '))
    if UserNumber > 0:
        positive = positive + 1
    elif UserNumber < 0:
        negative = negative + 1


    print('percentage of positive =  ' + str((positive * 100)/(positive+negative)))
    print('percentage of positive =  ' + str((negative * 100) / (positive + negative)))


    if UserNumber == 0:
        break

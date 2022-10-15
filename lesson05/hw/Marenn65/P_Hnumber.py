# Дано число P і число H.
# Користувач вводить послідовність чисел.
# Визначити: суму тих чисел, які менше P;
# добуток чисел, які більші за H;
# кількість чисел, що знаходяться в діапазоні значень від P до H.
# При введенні числа рівного P або H, припинити обчислення та вивести результат.
# (не використовувати білдін функції)

while True:
    P = 15
    H = 5
    UserInput = int(input('enter number from 5 to 15  '))

    sumlessP = int((P*(P+1)/2) - (UserInput*(UserInput+1)/2) + UserInput)
    print(sumlessP)


    def multiplyList(myList):
        result = 1
        for x in myList:
            result = result * x
        return result
    list1 = (range(H,UserInput))
    print(multiplyList(list1))


    PHrange = (P - H) - 2
    print(PHrange)

    if UserInput == P or UserInput == H:
        break
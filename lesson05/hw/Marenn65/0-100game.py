# У програмі генерується випадкове ціле число від 0 до 100.
# Користувач повинен його відгадати не більше ніж за 10 спроб.
# Після кожної невдалої спроби повинно повідомлятися чи більше чи менше введене користувачем число, ніж те, що загадане.
# Якщо за 10 спроб число не відгадане, то вивести загадане число.
from random import random, randint

num = randint(0,100)
#print(num)

count = 10
while True:
    UserNum = int(input('enter number from 0 to 100   '))
    count = count -1
    print(str(count) + '  attempts left')
    if UserNum < num:
        print('Your number is smoler')
    elif UserNum > num:
        print('Your number is BIGER')
    if count == 0 or num == UserNum:
        print('random number was   ' + str(num))
        break

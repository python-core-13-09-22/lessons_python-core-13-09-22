from curses.ascii import isdigit
import random

# 1. У програмі генерується випадкове ціле число від 0 до 100. 
# Користувач повинен його відгадати не більше ніж за 10 спроб. 
# Після кожної невдалої спроби повинно повідомлятися чи більше чи менше введене користувачем число, 
# ніж те, що загадане. Якщо за 10 спроб число не відгадане, то вивести загадане число.

x = random.randrange(0,100)
for _ in range (10):
    guess = int(input('Please insert a random number between 0 and 100: '))
    if guess > x:
        print("Your guess is bigger than a hidden number")
    elif guess < x:
        print("Your guess is lower than a hidden number")
    elif guess == x:
        print("BINGO")
        break
    else:
        print(f"Unfortunately you didn't find correct unswer,\nHidden number was {x}")


# 2. Вводяться десять натуральних чисел більше 2. 
# Порахувати, скільки серед них чисел, що кратні 5-ти. (не використовувати лісти)
div_5 = 0
print("Plese write 10 numbers, and we will check if they are multiples of 5")
for _ in range (10):
    x = int(input ("Please insert a number bigger than '2'"))
    if x.isdigit and x > 0:
        if x % 5 == 0:
            div_5+=1
    else:
        print("Please write correct input")
print (f"You have written {div_5} numbers multiples of 5")


# 3. Вивести на екран таблицю множення (від 1 до 9).

mul1 = 1
mul2 = 1
for num in range(9):
    for num in range (9):
        res = mul1 * mul2
        print(f"{mul1}*{mul2}={res}")
        mul2 +=1
    mul1+=1
    mul2 = 1


# 4. Вивести на екран «прямокутник» розміру N на M, утворений з двох видів символів. 
# Контур прямокутника повинен складатися з одного символу, а "заливка" - з іншого.

N = int(input("Write first side of rectangle: "))
M = int(input ("Write second side of rectangle: "))
side = " # "
mid = " \U0001f600"
print( N *side)
for _ in range (M-2):
    print( " #",(N-2) *mid,"#")
print( N *side)

# 5. Дано число P  і число H. Користувач вводить послідовність чисел. 
# Визначити: суму тих чисел, які менше P; добуток чисел, які більші за H; кількість чисел, 
# що знаходяться  в діапазоні значень від P до H. При введенні числа рівного P або H, 
# припинити обчислення та вивести результат. (не використовувати білдін функції)

P = random.randrange(1,20)
H = random.randrange(1,20)
print (f"insert numbers, everething lower than {P} will be added, bigger than {H} - multiplied")
sum = 0
mul = 1
beetween = 0
x = 1231313123123
while x != P or x !=H:
    x = int(input("Write a number: "))
    if P > x:
        sum+=x
    if H < x:
        mul*=x
    if P>H:
        if H<x<P:
            beetween+=1
    if H>P:
        if P<x<H:
            beetween+=1
    if x ==P or x==H:
        print(f"Your have printed {P} or {H}")
        break
print(f" Sum is {sum}, multiplied is {mul}, and beetween is {beetween} numbers")  

        
# 6. Для чисел, що вводяться користувачем, визначити відсоток додатних та від’ємних чисел. 
# При введенні числа 0 закінчити роботу.


big = 0
low = 0
all = 0
run = True

while run:
    try:
        x = int(input ("You can enter any numbers you want, or 0 to stop: "))
        if x > 0:
            big+=1
            all+=1
        elif x < 0:
            low +=1
            all+=1
        elif x == 0:
            break
    except ValueError as e :
        print("Plese write correct number")
low_per = low/all*100
big_per = big/all*100
print (f"You have printed {low} or {'%.2f' %low_per}% lower than 0 and {big} or {'%.2f' %big_per}% bigger than 0 numbers")

    

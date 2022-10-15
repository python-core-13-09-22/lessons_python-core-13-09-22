from random import randrange
import re
from subprocess import list2cmdline
# 1. Заповнити один список випадковими числами, інший - введеними з клавіатури числами, в третій записати суми відповідних елементів перших двох. 
# Вивести вміст списків на екран.
lst1_1=[]
lst1_2=[]
lst1_3=[]
for _ in range (3):
    lst1_1.append(randrange(10))
for _ in range (3):
    lst1_2.append(int(input("Insert item to a list: ")))
lst1_3.append(lst1_1[0]+lst1_2[0])
lst1_3.append(lst1_1[1]+lst1_2[1])
lst1_3.append(lst1_1[2]+lst1_2[2])
print(lst1_1, lst1_2, lst1_3)

# 2. Заповнити список дійсними числами введенням з клавіатури. Порахувати суму і добуток елементів списку. 
# Вивести на екран сам список, отримані суму і добуток його елементів.

lst_2 =[]
for _ in range (3):
    lst_2.append(int(input("Insert item to a list: ")))
sum = lst_2[0]+lst_2[1]+lst_2[2]
mul = lst_2[0]*lst_2[1]*lst_2[2]
print(f"Your list is {lst_2}, sum of each element= {sum}, multiplication product = {mul}")

# 3. Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список. 
# Порахувати кількість додатних, від’ємних і нульових елементів. Вивести на екран елементи списку і пораховані кількості.

lst_3 =[]
more= 0
less =0
null = 0

for _ in range(20):
    lst_3.append(randrange(-5, 4))
for num in lst_3:
    if num > 0:
        more+=1
    elif num < 0:
        less+=1
    else:
        null+=1
print(f"Your list is {lst_3}\nBigger than zero is {more} numbers\nLess than zero is {less} numbers\nand 0 was {null} times")

# 4. Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки додатні, у другий - тільки від’ємні.
#  Числа, рівні нулю, ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.

more =[]
less =[]
for _ in range(10):
    x = randrange(-5, 5)
    print(x)
    if x > 0:
        more.append(x)
    elif x < 0:
        less.append(x)

print(f'List of numbers bigger than zero{more}\nList of numbers less than zero{less}')

# 5. Заповнити список випадковими додатними і від’ємними цілими числами. Вивести його на екран.
#  Видалити з списку всі від’ємні елементи і знову вивести.

lst_5 = []
for _ in range(10):
    lst_5.append(randrange(-100, 100))
print(lst_5)    
res_5 = [num for num in lst_5 if num > 0]
print(res_5)
        
# 6. У другому списку зберегти індекси парних елементів першого списку. Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2,
#  то  другий треба заповнити значеннями 1, 4, 5, 6 (або 0, 3, 4, 5 - якщо індексація починається з нуля),
#  оскільки саме в цих позиціях першого масиву стоять парні числа.

lst_6 = []
res_6 = []
for _ in range (6):
    lst_6.append(randrange(20))
print(lst_6)
for x in lst_6:
    if x %2 ==0:
        res_6.append(lst_6.index(x))
print(res_6)



# 7. У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран.

lst_7 = []
res_7 =[]
for _ in range (10):
    lst_7.append(randrange(10))
print(lst_7)
for num in lst_7:
    if lst_7.count(num) ==1:
        res_7.append(num)
print(res_7)

# 8. У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.

lst_8 = []
for _ in range (5):
    lst_8.append(randrange(30))
lst_8.sort()
print(lst_8,max(lst_8), min(lst_8))
x = lst_8.pop(0)
y = lst_8.pop(3)
lst_8.insert(0,y)
lst_8.insert(4,x)
print(lst_8)

# 9. Порахувати суми кожного рядка і кожного стовпця матриці. Доповнити її стовпцем, 
# який містить суми елементів рядків та рядком, елементами якого є суми елементів стовпців.

lst_9_1 = []
lst_9_2 = []
lst_9_3 = []
r1=0
r2=0
r3=0
for i in range(3):
    lst_9_1.append(i)
for x in range(3):
    lst_9_2.append(lst_9_1)
matrix_length = len(lst_9_2)
for i in range(matrix_length):
    r1+=(lst_9_2[i][0])
for i in range(matrix_length):
    r2+=(lst_9_2[i][1])  
for i in range(matrix_length):
    r3+=(lst_9_2[i][2])
for i in range(matrix_length):
    x=sum(lst_9_2[i])
lst_9_2[2].append(x)
lst_9_3.append(r1)
lst_9_3.append(r2)
lst_9_3.append(r3)
lst_9_2.append(lst_9_3)
print(lst_9_2)

# 10. Сформувати матрицю з чисел від 0 до 999, вивести її на екран. Порахувати кількість двозначних чисел в ній.

lst_10_1 = []
lst_10_2 = []
XX_numbers = 0
for i in range (1001):
    if 9<i<100:
        XX_numbers+=1
    if len(lst_10_1) ==10:
        lst_10_2.append(lst_10_1)
        lst_10_1=[]
        lst_10_1.append(i)
    else:
        lst_10_1.append(i)
for i in lst_10_2:
    print(i)
print(XX_numbers)

    

# 11. Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків). Програма повинна обчислювати суму введених елементів
#  кожного рядка і записувати її в останній рядок. Наприкінці слід вивести отриману матрицю.


lst_11_1 = []
lst_11_2 = []
for i in range (4):
    lst_11_2.append(lst_11_1)
    for _ in range(4):
        lst_11_1.append(int(input("Write a number for a matrix: ")))
    lst_11_1.append(sum(lst_11_1))
    lst_11_1 = [] 
for i in lst_11_2:
    print(i)


# 12. Знайти максимальний елемент серед мінімальних елементів стовпців матриці.
lst_12_1 = []
lst_12_2 = []

for i in range (3):
    lst_12_2.append(lst_12_1)
    for _ in range(3):
        lst_12_1.append(int(randrange(1,20)))
    lst_12_1 = [] 

for i in lst_12_2:
    print(i)
for i in range(3):
    print(f'in {i} colomn, the lowest number is: {min([colomn[i] for colomn in lst_12_2])}')
    print(f'in {i} colomn, the highest number is: {max([colomn[i] for colomn in lst_12_2])}')        


# 13. Дві матриці заповнюються введенням з клавіатури. В елементи третьої матриці такої ж розмірності записати більші з відповідних
#  елементів перших двох. 

lst_13_1 = []
lst_13_2 = []
lst_13_3 = []
matrix_13_1 = []
matrix_13_2 = []
matrix_13_3 = []

for i in range (9):
    matrix_13_1.append(lst_13_1)
    for _ in range(3):
        lst_13_1.append(int(input("Write an element of first matrix: ")))
    lst_13_1 = []   

for i in range (9):
    matrix_13_2.append(lst_13_2)
    for _ in range(3):
        lst_13_2.append(int(input("Write an element of second matrix: ")))
    lst_13_2 = []    

for i in range (len(matrix_13_1)):
    if matrix_13_1[i][0]>matrix_13_2[i][0]:
        lst_13_3.append(matrix_13_1[i][0])
    elif matrix_13_1[i][0]<=matrix_13_2[i][0]:
        lst_13_3.append(matrix_13_2[i][0])
    if len(lst_13_3) == 3:
        matrix_13_3.append(lst_13_3)
        lst_13_3 = []

for i in range (len(matrix_13_1)):
    if matrix_13_1[i][1]>matrix_13_2[i][1]:
        lst_13_3.append(matrix_13_1[i][1])
    elif matrix_13_1[i][1]<=matrix_13_2[i][1]:
        lst_13_3.append(matrix_13_2[i][1])
    if len(lst_13_3) == 3:
        matrix_13_3.append(lst_13_3)
        lst_13_3 = []

for i in range (len(matrix_13_1)):
    if matrix_13_1[i][2]>matrix_13_2[i][2]:
        lst_13_3.append(matrix_13_1[i][2])
    elif matrix_13_1[i][2]<=matrix_13_2[i][2]:
        lst_13_3.append(matrix_13_2[i][2])
    if len(lst_13_3) == 3:
        matrix_13_3.append(lst_13_3)
        lst_13_3 = []

for i in matrix_13_1:
    print(i)
for i in matrix_13_2:
    print(i)
for i in matrix_13_3:
    print(i)

# 14. У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані відповідно на головній та бічній діагоналях.
lst_14_1 = []
matrix_14_1 = []
x = 0
for _ in range (10):
    matrix_14_1.append(lst_14_1)
    for _ in range(10):
        lst_14_1.append(randrange(1,10))
    lst_14_1 = []
print("Created matrix 10x10")
for i in matrix_14_1: 
    print(i)
for i in range(10):
    matrix_14_1[i][x],matrix_14_1[i][9-x]= matrix_14_1[i][9-x],matrix_14_1[i][x]
    x+=1
print("Changed matrix")       
for i in matrix_14_1:
    print(i)


# 15. Змінити послідовність стовпців матриці так, щоб елементи її першого рядка були відсортовані за зростанням.

lst_15_1 = []
matrix_15_1 = []
colomn = []
colomn_1 = []
x = 0
for _ in range (4):
    matrix_15_1.append(lst_15_1)
    for _ in range(4):
        lst_15_1.append(randrange(10,99))
    lst_15_1 = []
print("Created matrix 4x4")
for i in matrix_15_1:
    print(i)
print("_______________")
for i in range(4):
    colomn.append([colomn[i] for colomn in matrix_15_1])
    x=sorted(colomn)
for i in range(4):
    colomn_1.append([colomn[i] for colomn in x])
for i in colomn_1:
    print(i)
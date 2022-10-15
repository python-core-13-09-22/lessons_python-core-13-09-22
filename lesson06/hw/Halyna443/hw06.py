from random import randint
import random
import math
import numpy as np 

# Task 1
# Заповнити один список випадковими числами, інший - введеними з клавіатури числами, в третій записати суми відповідних елементів перших двох. 
# Вивести вміст списків на екран.
l1 = [randint (-5,80) for x in range (10)]
print(l1)
l2 = list(map(int, input().split(',')))
print(l2)
l3 = [sum(i) for i in zip(l1, l2)]
print(l3)


# Task 2
# Заповнити список дійсними числами введенням з клавіатури. Порахувати суму і добуток елементів списку. 
# Вивести на екран сам список, отримані суму і добуток його елементів.
a = []
n = int(input("Enter number of elements : "))
s = 0
m = 1
for i in range(0, n):
    el = float(input())
    a.append(el)     
print(a)
s =sum(a)
m =math.prod(a)
print('SUM = ', s)
print('Muilt = ', m)


# Task 3
# Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список. Порахувати кількість додатних, від’ємних і нульових елементів.
# Вивести на екран елементи списку і пораховані кількості. 
positive = 0
negative = 0
zero = 0
listss = [randint (-5,4) for d in range (20)]
print(listss)
for i in range(20):
    if listss[i] > 0:
        positive += 1
    elif listss[i] < 0:
        negative += 1     
    else:
        zero += 1
print("Positive Number: ", positive)
print("Negative Number: ", negative)
print("Zero: ", zero)


# Task 4
# Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки додатні, у другий - тільки від’ємні.
# Числа, рівні нулю, ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.
lis1 = []
lis2 = []
lis = [randint (-5,5) for f in range (10)]
print(lis)
for i in range(10):
        if lis[i] > 0:
            lis1.append(lis[i])
        if lis[i] < 0: 
            lis2.append(lis[i])   
        else:
            pass  
print(lis1)
print(lis2)


#  Task 5
# Заповнити список випадковими додатними і від’ємними цілими числами. Вивести його на екран. Видалити з списку всі від’ємні елементи і знову вивести.
w = [randint (-7,7) for k in range (22)]
print('The original list is : ', w)
result = [el for el in w if el >= 0]
print('List after filtering : ', (result))


# Task 6
# У другому списку зберегти індекси парних елементів першого списку. Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2, 
# то  другий треба заповнити значеннями 1, 4, 5, 6 (або 0, 3, 4, 5 - якщо індексація починається з нуля), оскільки саме в цих позиціях першого масиву стоять парні числа.
wel = [randint (-7,7) for x in range (18)]
print('The original list is : ', wel)
welindex = []
for ind, elem in enumerate(wel):
    if elem % 2 == 0 and elem != 0:
        welindex.append(ind)
print('Indices of even elements: ', welindex)       


# Task 7
# У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран. 
l = [9, 7, 3, 3, 'aa', 'aa', 8, -5, -7, 'bb']
print(l)
x = []
for a in l:
    if a not in x: 
        x.append(a)
    else:
        x.remove(a)
print(x)


# Task 8
#  У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.
num = [randint (-7,4) for x in range (7)]
print('The original list is : ', num)

maxn = num.index(max(num))
print('the index of the maximum element: ', maxn)

minn = num.index(min(num))
print('the index of the minimal element: ', minn)

num[maxn],num[minn] = num[minn],num[maxn]
print('List after is: ',num)
              
# Task 9 
# Порахувати суми кожного рядка і кожного стовпця матриці. Доповнити її стовпцем, який містить суми елементів рядків та рядком, елементами якого є суми елементів стовпців.
h = np.reshape(np.matrix(range(16)), (4, -1))
print(h)
y = h.sum(0)
y1 = h.sum(1)
print(y)
print(y1)

 
    
 # Task 10
#  Сформувати матрицю з чисел від 0 до 999, вивести її на екран. Порахувати кількість двозначних чисел в ній.
h33 = []
for a in range(100):
    h33.append(a)
print(h33)    
count = 0 
for a in h33:
    if 10 <= a <= 99:
        count = count + 1   
print(count)

# Task 11
# Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків). 
# Програма повинна обчислювати суму введених елементів кожного рядка і записувати її в останній рядок.
# Наприкінці слід вивести отриману матрицю.

M1 = []
M2 = []
for i in range (4):
    M2.append(M1)
    for _ in range(4):
        M1.append(int(input('Enter a number: ' )))
    M1.append(sum(M1))
    M1 = [] 
for i in M2:
    print(i)  

# Task 12 
#  Знайти максимальний елемент серед мінімальних елементів стовпців матриці.
x = np.random.randint(20, size=(5, 4))
print(x)
y = (x.min(0))
print(y)
print(max(y))




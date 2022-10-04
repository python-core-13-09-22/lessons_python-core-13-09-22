# Task1
import random
a = random.randint(0, 100)
for b in range(10):
    b = int(input('Try to guess the number: '))
    if a == b: print ('Guessed!'  )
    else:
            if a < b: print('Your number is greater' )
            else: print('Your number is less' )
print(a)        
        
# Task 2 
s = 0
for a in range(10):
    a = int(input('enter an integer greater 2: '))
    if a % 5 == 0:
        s += 1
        print(s," ",a)
print("s = ",s)
        
# Task 3
for i in range(1, 10):
    for j in range(1, 10):
        print(f' {i * j:2} ', end = ' ')
    print()        

# Task 4    
N = random.randint(4,8)
M = random.randint(4,8)
print(N)
print(M)
for x in range(N):
    if x == 0 or x == N-1:
        for y in range(M):
            print(" | ", end='')
    if x >= 1 and x <= N-2:
        for y in range(M):
            if y == 0 or y == M-1:
                print(" | ", end='')
            if y >= 1 and y <= M-2:
                print(" = ", end='')
    print("")
    
# Task 5
P = 10
H = 5
a = 0
p = 0
h = 1
c = 0
while a != P or a != H:
    a = int(input('enter a: '))
    if a < P:
        p += a        
    if a > H:
        h *= a
    if P < H:
        if P < a < H:
            c += 1
    if H < P:
        if H < a < P:
            c += 1           
    if a == P or a == H:
        print('sum of numbers= ', p, 'multiplication of numbers= ', h, 'count of numbers= ', c)
        break  


# Task 6
positive = 0
negative = 0
count = 0
i = 1
try:
    while i != 0:
        i = int(input('enter i: '))
        if i < 0:
            negative += 1
            count += 1
        if i > 0:
            positive += 1
            count += 1
        if i == 0:
            print('negative = ', negative, 'positive = ', positive, 'count = ', count)      
            break
    n = round(negative/count*100)
    p = round(positive/count*100)
    print('negative = ', n,'%' ' positive = ', p, '%')
except:
    print("You can't divide by zero!")


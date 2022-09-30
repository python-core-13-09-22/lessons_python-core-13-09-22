#Задано три довільних числа.
#Визначити, чи можна побудувати трикутник з такими довжинами сторін;
# Якщо так, то видрукувати його периметр та площу.
while True:
    try:
        def checkValidity(a, b, c):
            # check condition
            if (a + b <= c) or (a + c <= b) or (b + c <= a):
                return False
            else:
                return True

        a = int(input('enter length of first side '))
        b = int(input('enter length of second side '))
        c = int(input('enter length of third side '))
        if checkValidity(a, b, c):
            print("Valid")
        if checkValidity(a, b, c) == False:
            print("Invalid side length")
            break

        perimeter = a + b + c
        print('perimeter of triangle is ',  perimeter)
            # calculate the semi-perimeter
        s = (a + b + c) / 2

            # calculate the area
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('Area of a triangle is %f' % area)
    finally:
        if checkValidity(a,b,c) == False:
            continue


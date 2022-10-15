#Ввести значення(рік), вивести повідомлення It's a leap year! якщо рік високосний і
# This is not a leap year! якщо ні.
import calendar
y = input('insert year')
tf = calendar.isleap(int(y))
if tf == True:
    print("It's a leap year!")
else:
    print('This is not a leap year!')

#Ввести три значення (рік, місяць, день) у відповідні змінні.
# Визначити чи введені дані відповідають коректному запису дати.


while True:
    try:
        year = input('year')
        month = input('month')
        day = input('day')
        date = year + month + day

        z = calendar.weekday(int(year), int(month),int( day))
        if z>=0:
            print('ok date is valid')
            break
    except ValueError:
        print("invalid date! Please try again")







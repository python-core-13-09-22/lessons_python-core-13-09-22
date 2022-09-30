#Нехай k- ціле від 1 до 365. Присвоїти цілій змінній n значення
# (понеділок, вівторок, …, суботу чи неділю) залежно від того,
# на який день тижня припадає k-й день не високосного року, в якому
# 1 січня - понеділок.


import calendar as cal
from datetime import datetime, date, timedelta
k = int(input('enter day of the year from 1 to 365   '))
year = 2022
while True:
    year = year + 1
    a = cal.weekday(year, 1, 1)
    b = cal.isleap(year)
    if a == 0 and cal.isleap(b) == True:
        print(year, a, b)
        break

k=str(k)
# adjusting day num
k.rjust(3 + len(k), '0')
start_date = date(int(year), 1, 1)

result_date = start_date + timedelta(days=int(k) - 1)
result = result_date.strftime("%d-%m-%Y")
print("The day number: " + str(k))
print("Date in year: " + str(result))
q = str(result)
q = q.split('-')
month = q[1]
day = q[0]
z = cal.day_name[cal.weekday(year, int(month), int(day))]
print(z)


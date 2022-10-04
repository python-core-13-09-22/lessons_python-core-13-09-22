#Вивести на екран таблицю множення (від 1 до 9).
x = range(1,10)
n = range(1,10)

mult_table = [[i*j for j in x] for i in n]
for i in mult_table:
    print(i)
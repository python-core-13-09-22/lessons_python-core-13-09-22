# У матриці 10x10 поміняти значення елементів у кожному рядку, розташовані відповідно на головній та бічній діагоналях.
import random

# xoo
# oxo
# oox

# oox
# oxo
# xoo
N = 10
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randint(0, 100))
    matrix.append(row)

# pprint(matrix)
# print(matrix)
# d = {1:{1:"a", 2:"b"}, 2:"b"}
# pprint(d, width=1)
# print(d)
from colorama import Fore, Style


for i in range(N):
    for j in range(N):
        if j == i:
            print(f"{Fore.RED}{matrix[i][j]}{Style.RESET_ALL}", end="\t")
        elif j == N - 1 - i:
            print(f"{Fore.GREEN}{matrix[i][j]}{Style.RESET_ALL}", end="\t")
        else:
            print(matrix[i][j], end="\t")
    print("")
swap_index = 0
for i in range(N):
    # matrix[i][swap_index] = matrix[i][N - 1 - swap_index] # err
    # matrix[i][N - 1 - swap_index] = matrix[i][swap_index] # err
    a = matrix[i][swap_index]
    b = matrix[i][N - 1 - swap_index]
    matrix[i][N - 1 - swap_index] = a
    matrix[i][swap_index] = b
    # matrix[i][swap_index], matrix[i][N - 1 - swap_index] =  matrix[i][N - 1 - swap_index], matrix[i][swap_index]

    swap_index += 1
swap_index = 0
for i in range(N):
    for j in range(N):
        if j == swap_index:
            print(f"{Fore.GREEN}{matrix[i][j]}{Style.RESET_ALL}", end="\t")
        elif j == N - 1 - swap_index:
            print(f"{Fore.RED}{matrix[i][j]}{Style.RESET_ALL}", end="\t")
        else:
            print(matrix[i][j], end="\t")

    swap_index += 1
    print("")

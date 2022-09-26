# finds the product of numbers
n = 4562
prod = 1
while n > 0:
    digit = n % 10
    prod = prod * digit
    n = n // 10
print(prod)

# reverse of number
n = 4562
b = str(n)
print((b[::-1]))

# sort of numbers
n = 4562
x = [int(a) for a in str(n)]
x.sort()
print(x)


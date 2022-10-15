num = 1274
#print sum of num digits
num_array = [int(x) for x in str(num)]
p = sum(num_array)
print(p)
#print reverse num
print(str(num)[::-1])
#o = (sorted(num_array, reverse=True))
#print(o)

#print sorted num
sorted = (sorted(num_array))
#print(type(sorted))
q = ''.join(map(str, sorted))
print(int(q))

#Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
a = 1
b = 5
print(a, b)
a, b = b, a
print(a, b)




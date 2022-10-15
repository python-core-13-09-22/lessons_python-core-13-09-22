#To do
# task 1
text = open("C:/Users/admin/Desktop/TheZenofPython.txt", "r")
text = text.read()
print(text)
better = text.count("better")
print(better)
never = text.count("never")
print(never)
s = text.count("is")
print(s)
text = text.replace("i", "&")
print(text)
text = text.upper()
print(text)

# task 2
num = input()
if num.isdigit() > 999 and num.isdigit() < 10000:
    s = num[0] * num[1] * num[2] * num[3]
print(s)
print(sorted(num))
print(num[::-1])

# task 3
a = input()
b = input()
a, b = b, a
print(a, b)

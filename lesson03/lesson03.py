# MAX = 10
#
# a = "test"
# print(id(a))
# a += "test"
# print(id(a))
# # a[1] = "a"
# l = []
# print(id(l))
# l.append(10)
# print(id(l))
# l.append(10)
# print(id(l))
# l.append(10)
# print(id(l))

# a = 999**999
# print(a)
# print(len(str(a)))
# print(int("10"))
# i = input("value:")
# print(int(i, 2))
# print(int(i, 8))
# print(int(i, 10))
# print(int(i, 16))
# a = 55
# f = input("formula:")
# print(eval(f))
# t = tuple()
# print(type(t))

# for i in range(255):
#     print(f"{i}-{chr(i)} ")
#
# text = "hjfsvbdlkcbdjhsgdgajbdia"
# for c in text:
#     print(f"{c} - {ord(c)}")

# a = 28
# print(bin(a))
# print(oct(a))
# print(hex(a))
# for i in range(33):
#     print(f"{bin(i)[2:].zfill(4)}\t{oct(i)[2:]}\t{i}\t{hex(i)[2:]}")


#
# class A: pass
# class B(A): pass
# a = A()
# b = B()
# print(type(a), type(a) is A)
# print(type(b), type(b) is A)
# print(type(a), type(a) is B)
# print(type(b), type(b) is B)
#
# print(isinstance(a, A))
# print(isinstance(a, B))
# print(isinstance(b, A))
# print(isinstance(b, B))
#
# class A: pass
# a = A()
# text = str(a)
# print(text)
# print(id(a))
# print(int(text[-17:-1], 16))

# name = "John"
# age = 23
# template = "%s is %d years old."
# print(template % (name, age))
# template = "{} is {} years old."
# print(template.format(name, age))
# template = "{n} is {d} years old. {n}"
# print(template.format(d=age, n=name))
# print(f"{name} is {age} years old. {age}")


# text = "0123456789abcdef"
#
# print(text[0])
# print(text[15])
# print(text[0:5])
# print(text[5:12])
# print(text[:])
# print(text[5:])
# print(text[:5])
# print(text[::2])
# print(text[-1])
# print(text[-2])
# print(text[-2:-5])
# print(text[-2:-5:-1])
# print(text[::-1])
# a = "This will split all words into a list".split("a")
# print(a)
# b = "-A-".join(a)
# print(b)
#
# print((-1)**0.5)

import math

print(math.pi)
l = []
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l[2] = 5
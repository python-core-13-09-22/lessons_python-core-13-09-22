# def f():
#     pass
# a = f()
# print(a)
# def f():
#     count = 10
#     return count
# # print(count)
# print(f())
# # print(count)
#
# def f():
#     print("f")
#     return "test"
#     print("f")
# print(f())

# def f():
#     """
#     this is funcrion
#     :return:
#     """
#     for i in range(10):
#         if i == 3:
#             return "test"*i
# print(f())
# help(f)
# help(f.__doc__)

# def f(a, b):
#     print(f"{a=} {b=}")
#
# f(1,2)
# f(2,1)
# f(b=1, a=2)

# def f(a, b, c=10):
#     print(f"{a=} {b=} {c=}")
# f(1, 3)
# f(1, 3, 55)
# f(c=99, a=55, b=35)
# f(99, c=55, b=35)


# def f(a, b, c=10): # err
#     print(f"{a=} {b=} {c=}")
# def f(*args, **kwargs):
#     print(f"{args=} {kwargs}")
#
#
# f(1, 2, 3, 4, c=1, b=44, d=55)
#
# print("asdhfvbjs", "vdshbfvjk", "asvfus dk")
#
#
# def f(a, b, *args, c=10, d=25, **kwargs):
#     print(f"{a=} {b=} {c=} {d=} {args=} {kwargs}")
#
#
# f(1, 2, 3, 4, 5, 6, c=99, g=555)
# f(1, 2, 3, 4)
#
# l = [1, 2, 3, 4]
# f(l[0], l[1], l[2], l[3])
# f(*l)
# d = {
#     "a":1,
#     "b":2,
#     "c":3,
#     "d": 25,
#     "g": 555
#
# }
# f(*d)
# f(**d)
# # f(a=d["a"], ...)
# d = {
#     "a1":1,
#     "b1":2,
#     "c1":3,
#     "d1": 25,
#     "g1": 555
#
# }
# f(*l, **d)

# MAX = 999
# MIN = -999
# def f():
#     print(MAX)
#     MAX = 25
#     print(MAX)
# f()
# print(MAX)
# MAX = 999
# MIN = -999
#
# def f():
#     global MAX
#     print(MAX)
#     MAX = 25
#     print(MAX)
#
# f()
# print(MAX)
# print("glob", dir())
# def f1():
#     a1 = 1
#     print("f1")
#
#     def f2():
#         nonlocal a1
#         a2 = 2
#         a1 = 55
#         print("f2", a2, a1)
#         def f3():
#             a3 = 3
#             global a2
#             a2 = 555
#             print("f3")
#             print("f3 ", dir())
#         print("f2" , dir())
#         f3()
#     f2()
#     print("f1", a1,dir())
# f1()
# print("glob", dir())

# l = [(12,3,45,5,2),(22,3,4,56,2,3), (1,2,3), (999, 9999)]
#
# l.sort(key=lambda a: sum(a))
# print(l)
# print(dir())
# def custom_sort(elements):
#     return -sum(elements)
#
# custom_sort = lambda elements: -sum(elements)
# l.sort(key=custom_sort)
# print(l)
# print(dir())
#
# f = lambda a,b,c:a+b+c
# print(f(1,2,3))
# def calc_factorial(x):
#     if x == 1 or x == 0:
#         return 1
#     else:
#         return x * calc_factorial(x - 1)
#
#
# # 1*2*3*4*5*6*7*8
#
# print(calc_factorial(5))
# print([(i, calc_factorial(i)) for i in range(10)])
#
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# print(calc_factorial(1000))
#
# def calc_factorial(5):
#     if x == 1 or x == 0:
#         return 1
#     else:
#         return 5*(4*(3*(2*1)))
#
# # 1,2,3,5,8,13...

sum(ite)

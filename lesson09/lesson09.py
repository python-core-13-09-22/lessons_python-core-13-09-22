# class Singleton:
#     obj = None  # attribute for storing a single copy
#
#     def __new__(cls, *args, **kwargs):  # class Singleton.
#         print("__new__")
#         if cls.obj is None:
#             # If it does not yet exist, then
#             # call __new__ of the parent class
#             cls.obj = object.__new__(cls, *args, **kwargs)
#         # cls.obj.a = 1
#         return cls.obj  # will return Singleton
#     def __init__(self):
#         print(self.__dict__)
#         print("__init__")
# s1 = Singleton()
# s2 = Singleton()
# s3 = Singleton()
# s4 = Singleton()
# print(id(s1))
# print(id(s2))
# print(id(s3))
# print(id(s4))

# class A:
#     def __init__(self, a):
#         self.a = a
#     def printA(self):
#         print(f"A: a:{self.a}")
#
# class B(A):
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.b = b
#     def printB(self):
#         print(f"B: a:{self.a} b:{self.b}")
#
# a = A(1)
# print([i for i in dir(a) if not i[0] == "_"])
# a.printA()
# b = B(2, 22)
# print([i for i in dir(b) if not i[0] == "_"])
# b.printA()
# b.printB()
# print(b.__class__)
# print(b.__dict__)

#
# class A:
#     def printA(self):
#         print("A")
#
#     def print(self):
#         print("A")
#
#
# class B(A):
#     def printB(self):
#         print("B")
#
#     def print(self):
#         print("B")
#
#
# class C(B):
#     def printC(self):
#         print("C")
#
#     def print(self):
#         print("c")
#
#
# class D(B):
#     def printD(self):
#         print(A)
#
#     def print(self):
#         print("d")
#
#
# class E(C, D):
#     def printE(self):
#         print(A)
#
#
# e = E()
# e.printA()
#
# e.print()
#
#
# class E(D, C):
#     def printE(self):
#         print(A)
#
# e = E()
# e.print()
#
# print(E.__mro__)

#
# class A:pass
# class B(A):pass
# class C(A):pass
# class D(B):pass
# class E(C):pass
# class F(C):pass
# class G(D, F):pass
# class K(E,F):pass
# class J(K, G):pass
#
# print(J.__mro__)

# from imp import a, _a, __a
# print(dir())
# class A:
#     def __init__(self):
#         self.a = 1
#         self._a = 2
#         self.__a = 3
#     def __my(self):
#         print(self.__a)
#     def my(self):
#         self.__my()
# a = A()
#
# print(a.a)
# print(a._a)
# # print(a.__a)
# # print(a.__my())
# print(a._A__a)
# a._A__my()
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"x:{self.__x} y{self.__y}"
#
#     def getX(self):
#         print("getX")
#         return self.__x
#
#     def setX(self, x):
#         print("setX")
#         self.__x = x
#
#     x = property(getX, setX)
#
#     @property
#     def yy(self):
#         print("getY")
#         return self.__y
#
#     @yy.setter
#     def yy(self, y):
#         print("setY")
#         self.__y = y
#
#
# p = Point(1, 2)
#
# p.setX(15)
# print(p)
#
# print(p.__dict__)
# p.x = 55
# print(p.x)
# p.yy = 999
# print(p.yy)
#
# print(p.__dict__)


# class A:
#     def printA(self):
#         print("A")
#
#     def print(self):
#         print("A")
#
#
# class B(A):
#     def printB(self):
#         print("B")
#
#     def print(self):
#         print("B")
#
#
# class C(B):
#     def printC(self):
#         print("C")
#
#     def print(self):
#         print("c")
#
#
# class D(B):
#     def printD(self):
#         print(A)
#
#     def print(self):
#         print("d")
#
#
# class E(C, D):
#     def printE(self):
#         print(A)
#
#
# e = E()
# e.printA()
#
# e.print()
# print([i for i in dir(e) if not i[0] == "_"])
# print(type(e))
# e.__class__ = B
# print([i for i in dir(e) if not i[0] == "_"])
# print(type(e))


class A:
    def print(self):
        print("A")
    def printA(self):
        print("A")


class B(A):
    def print(self):
        print("B")

    def print_old(self):
        super().print()
    def print_old(self, a):
        print(a)
        super().print()
b = B()
b.print()
b.print_old()
b.printA()
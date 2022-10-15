# тест = 1
# print(тест)

# print(1 == 1)
# print("1" == 1)
# print((1, 2, 3) == (1, 2, 3))
# print((1, 2, 3) == (1, 3, 2))
# print((1, 2, 3) == [1, 2, 3])
# print([1, 2, 3] == [1, 2, 3])
# print([1, 2, 3] == [1, 3, 2])
# print(1 != 1)
# print(1 != "1")
# print(1 < 5)
# print(1 > 5)
# print(1 > 1)
# print(1 >= 1)
# print("a" >= "b")
# print("ca" >= "ab")
# print("a" < "b")
# for i in range(255):
#     print(f"{i}-{chr(i)} ")
#
# print((1, 23) < (1, 24))
# print((1, 25) < (1, 24))
# a = (1,2)
# b = (1,2)
# def eq(x, y):
#     for i in range(min(len(x), len(y))):
#         if x[i] >= y[i]:
#             return False
#     if len(x) > len(y):
#         return False
#     return True
# print(eq(a, b))
# print(a<b)

# False, None, 0, empty iterabl("", (), [], {})

# l = [False, None, 0, (), [], {}, set()]
# for i in l:
#     if not i:
#         print(i, "is False")
# l = [False, None, 0, "", (), [], {}, set(), True, 0.5, -2, "a", (1, 2), [1], {1: 1}, {1}]
# for i in l:
#     if i:
#         print(i, "is True")
#     else:
#         print(i, "is False")
###############
# string = input("enter str: ")
# number = int(input("enter number: "))
#
# # if number > 10:
# #     if len(string) > 3:
# #         print("all good!")
# if number > 10 and len(string) > 3:
#     print("1) all good!")
#
# if ((number > 10 and number < 20) or (number > 30 and number < 40)) and len(string) > 3:
#     print("2) all good!")
#
# if number > 10 and (number < 20 or number > 30) and number < 40 and len(string) > 3:
#     print("2) all good!")
#########

# print(10 and 25 and (12, 2))
# print(10 and 25 and "test")
# print(10 and 0 and "test")
# print(10 and 10 and [] and "test")
# print(10 or 10 or [] or "test")
# print(0 or 10 or [] or "test")
# print(0 or 0 or [] or "test")
# print(0 or 0 or [] or None)
# a = 0 or 0 or [] or None
###############
# a = int(input("a:"))
# if a > 0: print("is positive")
# if a > 0:
#     print("is positive")
#     print("is if body")
# print("main")

# if a > 0:
#     print("is positive")
#     if a > 100:
#         print("is more 100")
#     print("body first if")
# print("main")

# a = input("a:")
# if a.startswith("-") and a[1:].isnumeric() or a.isnumeric() :
#     a = int(a)
#     if a > 0:
#         print("is positive")
#     else:
#         print("is negative")
# else:
#     print("a is not Numeric")
#############################
# a = input("a:")
# if a.startswith("-") and a[1:].isnumeric() or a.isnumeric() :
#     a = int(a)
#     if a > 1:
#         print("is positive")
#     else:
#         if 0 < a  :
#             print("a is (0, 1)")
#         else
#             if a == 0:
#                 print("is zero")
#             else:
#                 if a > -1:
#                     print("a is (-1, 0)")
#                 else:
#                     print("is negative")
# else:
#     print("a is not Numeric")


# if a.startswith("-") and a[1:].replace(".", "", 1).isdigit() or a.replace(".", "", 1).isdigit():
#     a = float(a)
#     if a > 1:
#         print("is positive")
#     elif 0 < a:
#         print("a is (0, 1)")
#     elif a == 0:
#         print("is zero")
#     elif a > -1:
#         print("a is (-1, 0)")
#     else:
#         print("is negative")
# else:
#     print("a is not Numeric")

#
# if a.startswith("-") and a[1:].replace(".", "", 1).isdigit() or a.replace(".", "", 1).isdigit():
#     a = float(a)
#     if a > 1:
#         print("is positive")
#     elif a > 0:
#         print("a is (0, +\u221e)")
#     elif a > -10:
#         print("is zero")
#     elif a > -1:
#         print("a is (-1, 0)")
#     else:
#         print("is negative")
# else:
#     print("a is not Numeric")
# print("\u263A")

# a = 55
# if a >= 10 and a <= 100:
#     print("a in [10:100]")
# if 10 <= a <= 100:
#     print("a in [10:100]")
#
# a = 1
# b = 2
# c = 3
# if 0 < a < b < c < 100:
#     print("test")

#######################################
# condition ? true : false
# s = a > 0 ? "is positive" : "is negative"

# a = int(input("a:"))
# s = ""
# if a > 0:
#     s = "is positive"
# else:
# #     s = "is negative"
# a = 1
# s = "is positive" if a > 0 else "is negative"
# print(s)
# a = -1
# s = "is positive" if a > 0 else "is negative"
# print(s)

#####

status = 400
match status:
    case 400:
        print("Bad request")
    case 401:
        print("Unauthorized")
    case 403:
        print("Forbidden")
    case _:
        print("Other error")

if status == 400:
    print("Bad request")
elif status == 401:
    print("Unauthorized")
elif status == 403:
    print("Forbidden")
else:
    print("Other error")

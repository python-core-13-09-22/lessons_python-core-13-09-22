# index = 0
#
# while index < 10:
#     print(index)
#     index += 1

# print("end")

# for i in [10, 13, 55, "aa"]:
#     print(i)
# print("end")
# for i in (10, 13, 55, "aa"):
#     print(i)
# print("end")
# for i in "dagsfvhadjfkagk":
#     print(i)
# print("end")
# d = {"key1": "value1",
#      "key2": "value2",
#      "key3": "value3",
#      "key4": "value4",
#      "key5": "value5"}
# for i in d:
#     print(i, d[i])
#
# print(d.items())
# for key, value in d.items():
#     print(key, value)
# for key in d:
#     value = d[key]
#     print(key, value)
# # key, value = 'key1', 'value1'
# print(key)
#


# for i in range(10):
#      for j in range(10):
#           for k in range(10):
#                for l in range(10):
#                     count = i*j*k*l
# l =  ["a", "b", "c", "d", "e", "f"]
# for i in l:
#      print(i)
# for i in range(len(l)):# 0 -> n
#      print(f"{i} {l[i]}")
#
# for i in range(-len(l), len(l)):# -n -> n
#      print(f"{i} {l[i]}")
# for i in range(-len(l), len(l), 3):# -n -> n sten
#      print(f"{i} {l[i]}")
#
# r = range(10)
# print(r)
# r = range(-len(l), len(l))
# print(r)
# r = range(-len(l), len(l), 3)
# print(r)
# # for i in r:
# #      print(i)
# i = iter(r)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# i = 0
# while i < 10:
#     print(i)
#     i += 1
#     if i == 5:
#         break
# print("end")
#
# for i in range(10):
#     print(i)
#     i += 1
#     if i == 5:
#         break
# print("end")

# i = 0
# while i < 10:
#     print(f"before {i}", end=" -> ")
#     i += 1
#     if i == 5:
#         print()
#         continue
#     print(f"after {i}")
# for i in range(3):
#     if i == 1:
#         continue
#     for j in range(3):
#         if j > 0:
#             break
#         for k in range(3):
#             print(f"{i}-{j}-{k}")


# i = 0
# while i < 10:
#     print(f"before {i}", end=" -> ")
#     i += 1
#     if i == 5:
#         print()
#         # continue
#         break
#     print(f"after {i}")
# else:
#     print(f"else {i}")
# print("end")

# l = [random.randint(-10, 2) for i in range(10)]
# print(l)
# flag = False
# for i in l:
#     if i > 0:
#         flag = True
#
# if not flag:
#     print("text")

# flag = True
# while flag:
#     l = [random.randint(-10, 3) for i in range(10)]
#     print(l)
#     for i in l:
#         if i > 0:
#             break
#     else:
#         flag = False
#         print("text")
#
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# print(matrix)
#
# for row in matrix:
#     print(row)
# for row in matrix:
#     for element in row:
#         print(element, end="\t")
#     print()

matrix = []
row = input("enter count row:")
for i in range(int(row)):
    size = input(f"enter size {i}-row:")
    line = []
    for j in range(int(size)):
        element = input(f"matrix[{i}][{j}]=")
        line.append(element)
    matrix.append(line)

for row in matrix:
    for element in row:
        print(element, end="\t")
    print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end="\t")
    print()
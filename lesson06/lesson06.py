## list

# l = list()
# print(l)
# l = list("ats")
# print(l)
# # l = list(1)  # error
# l = []
# print(l)
# l = [1, 2, 3, 4, 5]
# print(l)
# l = [[1, 2, 3] * 3] * 3
# print(l)
# l[0][0] = 999
# print(l)
# #
# print([i for i in dir(list) if not i[0] == "_"])
#
# l = []
# l.append([1, 2, 3, 4, 5])
# l.append("test")
# l.append("test")
# l += ["a", "b"]
# print(l)
# l.extend([1, 2, 3, 4, 5])
# print(l, id(l))
# l.clear()
# print(l, id(l))
# l = []
# print(l, id(l))
# l.extend([1, 2, 3, 4, 5])
# del l[2]
# print(l, id(l))
# # del l
# # print(l, id(l))
#
# ll = l.copy()
# ll = l[:]
# l.extend([1, 2, 3, 4, 5])
# l.append((1, 2))
# l.append((1, 2))
# l.append((2, 1))
# print(l, l.count(3))
# print(l, l.count(4))
# print(l, l.count((1, 2)))
# print(l.index(3))
# print(l.index(2))
# print(l.index(2, 3))
# print(l.index(2, 3, 8))
# # print(l.index(2, 3, 4))
# # print(l.index(2222, 3, 4))
# l.insert(5, "value")
# l.insert(55, "value")
# l.insert(-55, "value")
# print(l)
# l.remove(2)
# l.remove(2)
# # l.remove(2)
# print(l)
#
# a = l.pop()
# print(a, l)
#
# a = l.pop(5)
# print(a, l)
# #
# # a = l.pop(55)
# # print(a, l)
# l = [1, 2, 3, 4, 5]
# l.reverse()
# print(l)
# ll = reversed(l)
# print(l, list(ll))
#
# l = [1, 4, 2, 3, 4, 8, 34, 23, 5]
# l.sort()
# print(l)
# l = list(map(str, l))
# l.sort()
# print(l)
# l = [1, 4, 2, "3", "4", 8, 34, 23, 5]
#
#
# # l.sort() # error
# # print(l)
# def sort_int_string(value):
#     if type(value) == int:
#         return value
#     if type(value) == str:
#         return ord(value)
#
#
# l.sort(key=sort_int_string)
# print(l)
#
# print(all([1, 2, 4, 5, 6, 7, 8]))
# print(all([1, [], 4, 5, 6, 7, 8]))
# l = ["a", "b", "c"]
# e = list(enumerate(l))
# print(e)
# s = "test"
# for i in s:
#     print(i)
# for i in range(len(s)):
#     print(i, s[i])
# for index, value in enumerate(s):
#     print(index, value)
# print(l)
# # print(sum(l))
# print(max(l))


#### tuple

# t = tuple()
# print(t)
# t = tuple("test")
# print(t)
# t = ()
# print(t)
# t = (1, )
# print(t)
#
# print([i for i in dir(tuple) if not i[0] == "_"])
#
# # t[0] = 55
# t = (1,[1, 2])
# t[1].append(55)
# print(t)
#
#
# l = ["a"*i for i in range(100)]
# t = tuple("a"*i for i in range(100))
# print(l.__sizeof__())
# print(t.__sizeof__())

## set

# s = set()
# print(s)
# s = set("dkshfvbjdhsvfjhdsvfjhvdsjhfbdsjhbjf")
# print(s)
# s = {}
# print(s, type(s))# not set
#
# s = {"a", 1, 3}
# print(s, type(s))
#
# s.add("test")
# print(s, type(s))

# s1 = {1, 2, 3, 4, 5}
# s2 = {3, 4, 5, 6, 7}
#
# print(s1.difference(s2))
# print(s2.difference(s1))
# # print(s1.difference_update(s2))
# print(s1, s2)
# t = s1.pop()
# print(t, s1)
# # t = s1.pop("2") # error
#
#
# print([i for i in dir(set) if not i[0] == "_"])
# print([i for i in dir(frozenset) if not i[0] == "_"])

### dict
#
# d = dict()
# print(d)
# d = dict(zip("abcd",[1,2,3,4]))
# print(d)
# d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
# print(d)
# d = {}
# print(d)
# d = {1:"a", 2:"b"}
# print(d)
# # list
# # d = {[1,2]:2}
# print([i for i in dir(dict) if not i[0] == "_"])
#
# d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
# print(d.fromkeys("zx", 5))
# print(d.get("a"))
# print(d["a"])
# print(d.get("aaa"))
# # print(d["aaa"])
# print(d.items())
# print(d.keys())
# print(d.values())
# v = d.pop("a")
# print(v, d)
# v = d.popitem()
# print(v, d)

# s = {1,2,3,4,2,3,4,2,3,4,2,34,4}
# for i in s:
#     print(i)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for key in d:
    print(key, d.get(key))
d["a"] = "test"
d["temp"] = d.copy()
print(d)
for key, value in d.items():
    print(key, value)

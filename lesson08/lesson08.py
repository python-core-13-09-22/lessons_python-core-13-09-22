# # class MyClass:
# #     """
# #     vnjskdbvk
# #     docstring
# #     """
# #
# # print(MyClass.__doc__)
# #
# # # print(2**5586)
#
#
# class Order(object):
#     index = 0
#     l = []
#     def __init__(self, id, name, cost, date):
#         self.id = id
#         self.name = name
#         self.cost = cost
#         self.date = date
#
#     def __str__(self):
#         return f"id:{self.id} name:{self.name} cost:{self.cost} date:{self.date}"
#
#     def __repr__(self):
#         return f"<{self.id}, {self.name}>"
#
#     def __add__(self, other):
#         order = Order(id=self.id + other.id,
#                       cost=self.cost + other.cost,
#                       name=self.name + other.name,
#                       date=date.today())
#         return order
#
#     def __hash__(self):
#         return 100
#
#     def add_cost(self, extra_cost):
#         self.cost += extra_cost
#
#
# from datetime import date
#
# a1 = Order(1, "order1", 55.66, date.today())
# a2 = Order(2, "order2", 155.66, date(2022, 10, 10))
# temp = a2.__str__()
# print(temp)
# print(a1)
# print(a1.id, a1.name, a1.cost, a1.date)
# a = [a1, a2, Order(3, "order3", 155.66, date(2022, 9, 10)), a1 + a2]
# print(a)
#
# a1.add_cost(10)
# print(a1)
#
# print(Order.__dict__)
# print(a1.__dict__)
# print(Order.index)
# print(a1.index)
# print(a2.index)
# Order.index = 10
# print(Order.index)
# print(a1.index)
# print(a2.index)
# a1.new_atr = 55
# print(a1.__dict__)
# print(a2.__dict__)
# print(Order.index, Order.l,)
# print(a1.index, a1.l, a1.__dict__)
# print(a2.index, a2.l, a2.__dict__)
#
# a1.index = 999
# a1.l.append(99)
#
# print(Order.index, Order.l)
# print(a1.index, a1.l, a1.__dict__)
# print(a2.index, a2.l, a2.__dict__)

class Order(object):
    __index = 1
    l = []
    def __init__(self, name, cost, date):
        self.id = self.__index
        Order.__index += 1
        self.name = name
        self.cost = cost
        self.date = date
        Order.l.append(self)

    def __str__(self):
        return f"id:{self.id} name:{self.name} cost:{self.cost} date:{self.date}"

    def __repr__(self):
        return f"<{self.id}, {self.name}>"

    def __add__(self, other):
        order = Order(cost=self.cost + other.cost,
                      name=self.name + other.name,
                      date="date.today()")
        return order

    def __hash__(self):
        return 100

    def add_cost(self, extra_cost):
        self.cost += extra_cost

a1 = Order( "order1", 55.66, "date.today()")
a2 = Order("order2", 155.66, "date(2022, 10, 10)")

print(a1)
print(a2)

print(Order.l)
import random
# Python Zen

pythonZen = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one -- and preferably only one -- obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never.    Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!  Live Python training"
x1 = pythonZen.count('never')
x2 = pythonZen.count('better')
x3 = pythonZen.count('is')
x4 = pythonZen.upper()
x5 = pythonZen.replace('and', '&')

print(x1,x2,x3,x4,x5)

# XXXX number

y=str(random.randrange(1000, 9999))
y1=int(y[0])+int(y[1])+int(y[2])+int(y[3])
y2=y[::-1]
y3 = "".join(sorted (y))
print(y,y1,y2,y3)

# compare 2 
a=random.randrange(0,5)
b=random.randrange(0,5)
if a == b:
    print(True)
else:
    print(False)

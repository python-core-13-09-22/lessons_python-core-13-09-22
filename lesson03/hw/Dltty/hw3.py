#Task1

text = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

word1 = text.count('better')
print(word1)
word2 = text.count('never')
print(word2)
word3 = text.count('is')
print(word3)
text.upper()
text.replace('i','&')


#task2

n =str(5713)
b1= n[::-1]
print(b1)
a = int(n[0]) * int(n[1]) * int(n[2]) * int(n[3])
print(a)
print(sorted(n))

#task3
a=1
b=1
print(a==b)

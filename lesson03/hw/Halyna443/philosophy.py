import this

the_zen_of_Python = '''
Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!
'''
# count the number of words
print(the_zen_of_Python.count('better'))
print(the_zen_of_Python.count('never'))
print(the_zen_of_Python.count('is'))

# make upper case words
print(the_zen_of_Python.upper())

# change a letter to simbol
print(the_zen_of_Python.replace('i', '&'))      


# text = "There is never the end. Is it better "
# print(f" origin text :{text}")
# count = 0
# l = []
# l = text.split()
# for i in range(len(l)):
#     l[i] = l[i].lower()
#     if l[i] == 'better' or l[i] == 'never' or l[i] == 'is':
#         count += 1
#     l[i] = l[i].replace('i', '&')
#     l[i] = l[i].upper()
# print(f"  There are {count}  better never or is words")
# print(f"  The upper words with changes of i to & :", *l)

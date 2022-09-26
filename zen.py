#Записати в стрічку філософію Пайтона
import this
import codecs
z = codecs.encode(this.s, 'rot13')
#Вивести весь текст у верхньому регістрі (всі великі літери)
z = z.upper()
print(z)
#Знайти в заданій стрічці кількість входжень слів (better, never, is)
zen = z.split()
search = 'iS BEttEr NeVeR'
search = search.upper()
search = search.split()

for x in search:
    e = zen.count(x)
    print(x,'find', e ,'times')

#Замінити всі входження символу “і” на “&”
replased_i = z.lower().replace('i', '&')
print(replased_i)












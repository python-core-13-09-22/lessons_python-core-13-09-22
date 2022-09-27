#Task 1
print("Task 1")
text=" There is never the end.  Is it better "
print(f" origin text :{text}")
count =0
l=[]
l=text.split()
for i in range(len(l)):
    l[i]=l[i].lower()
    if l[i]== 'better' or l[i]=='never' or l[i]=='is':
        count+=1
    l[i]=l[i].replace('i','&')      
    l[i]=l[i].upper() 
print(f" There are {count}  better never or is words" )
print(" The upper words with changes of i to & :",*l)

#Task 2
print("Task 2")
number1=1452
print(f" origin number :{number1}")
number=str(number1)
print(" reverse number:" ,number[::-1])
mult=1
for i in number:
    mult*=int(i)
print(f" multiply all the numbers: {mult}")
sort_number = sorted(number)
new_sort_number = ''.join(sort_number)
print(f" sorted order number: {new_sort_number}")

#Task 3
print("Task 3")
var1=0
var2=1
print(f" Befor: Val1 = {var1}, Val2 = {var2}" )
var1,var2=var2, var1
print(f" After: Val1 = {var1}, Val2 = {var2}" )

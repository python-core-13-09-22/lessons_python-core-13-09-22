import datetime

file = open('data/welcom.txt')
for line in file:
    print(line)
file.close()
file = open('data/welcom.txt')
while True:
    line = file.readline()
    if not line:
        break
    print(line)
file.close()
#
# try:
#     file.write(‘hello world’)
# finally:
#     file.close()
with open('data/welcom.txt' ) as file:
    for line in file:
        print(line)
with open('data/out.txt', "a") as file:
    # file.write(str(datetime.datetime.now()))
    file.write(str(datetime.datetime.now()) +"\n")
zen = open('ZenPython.txt')
data = zen.read()
v = 0
while v != 5:
    v = int(input('''
    
Виберіть завдання яке хочете перевірити, та введіть відповідну цифру:

          1 - Показати філософію Пайтона
          2 - Знайти в заданій стрічці кількість входжень слів (better, never, is)
          3 - Вивести весь текст у верхньому регістрі.
          4 - Замінити всі входження символу "i" на "&".
          5 - Вийти та закінчити перевірку          
          
          Ваш вибір:  '''))
    if v == 1:
        print('\nПоказати філософію Пайтона\n')
        for line in zen:
          print(line)

    elif v == 2:
        w_bet = data.count('better')
        w_new = data.count('never')
        w_is = data.count('is')
        print(f'''\nЗнайти в заданій стрічці кількість входжень слів (better, never, is)
        
                 Кількість вибраних слів в тексті така:                  
                  - better: {w_bet};
                  - newer: {w_new};
                  - is: {w_is}''')
    elif v == 3:
        registr = data.upper()
        print(registr)
    elif v == 4:
        print(data.replace('i', '&'))
    elif v == 5:
        print('\nГарного Вам настрою. До побачення !\n')
    else:
        print('Будь ласка виберіть варіант зі списку')


    if v != 5:
        input('\nДля продовження введіть будь-який символ\n')
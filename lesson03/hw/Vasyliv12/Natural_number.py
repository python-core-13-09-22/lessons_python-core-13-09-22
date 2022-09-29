x = input('\nВведіть необхідне число:  ')

y = 0

for i in x:
    y = y + int(i)
print(f'\nДобуток цифр цього числа: {y}')

n = x[::-1]
print(f'\nчисло в реверсному порядку: {n}')

l = list(x)
ls = ''.join(sorted(l))
print(f'\nВідсортоване число: {ls}')


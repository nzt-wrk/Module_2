first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

# Вариант 1
if first==second==third:
    print('все числа равны')
elif first==second or first==third  or second==third:
    print('два числа равны из трех')
else:
    print('равных числе нет')

# вариант 2
if first==second==third:
    print('все числа равны')
elif first!=second!=third and first!=third:
    print('равных числе нет')
else:
    print('два числа равны')

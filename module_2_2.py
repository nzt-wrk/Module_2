first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first==second==third:
    print('все числоа равны')
elif first==second or first==third  or second==third:
    print('два числа равны из трех')
else:
    print('равных числе нет')
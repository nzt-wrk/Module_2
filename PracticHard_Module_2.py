# import random
# # set_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# # n = random.choice(set_1)

def Password_num(n):
    result = ""
    cnt = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            cnt += 1  # Счетчик переборов по циклам (не обязателен для работы программы)
            if n % (i + j) == 0:
                result = result + str(i) + str(j)
    return result, cnt

def input_int():
    while True:
        s = input('Введите число от 3 до 20: ')
        try:
            return int(s)
                # if s < 3 or s > 20:
                #     print('Ошибка. Ведено не допустимое значение!')
                # else:
                #     return s
        except ValueError:
            print('Ошибка. Ведено не допустимое значение!')

n = input_int()
while n < 3 or n > 20:
    print('Ошибка. Число должно быть в диапазоне от 3 до 20!')
    n = input_int()
else:
    password, cnt = Password_num(n)
    print('----------------------------------')
    print(f'Пароль для числа {n}: {password}')
    print()
    print(f'Кол-во переборов по циклам: {cnt}')
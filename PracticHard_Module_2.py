# import random
# # set_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# # n = random.choice(set_1)

def Password_num(n):  # функция получения пароля из исходного(введеного) числа
    result = ""
    cnt = 0

    for i in range(1, n):
        if n > 20:
            break
        else:
            for j in range(i + 1, n):
                cnt += 1  # Счетчик переборов по циклам (не обязателен для работы программы)
                if n % (i + j) == 0:
                    result = result + str(i) + str(j)
    return result, cnt


def input_int():  # функция проверки на вводимое значение и перевод вводимого значения в целочисленое
    while True:
        s = input('Введите число от 3 до 20 или введите "\u001b[31mStop\u001b[0m" для остановки программы: ')
        s = s.capitalize()
        if s == "Stop":
            return s
            break
        else:
            try:
                return int(s)
            except ValueError:
                print('------------------------------------------')
                print('- \u001b[31mОшибка. Ведено не допустимое значение! \u001b[0m-')
                print('- \u001b[31mне допускается ввод букв и пробелов    \u001b[0m-')
                print('\u001b[0m------------------------------------------')
                print()


while True:
    n = input_int()
    if n == "Stop":
        break
    result, cnt = Password_num(n)
    if n > 20:  # ограничиваем допустимое исходное значение диапазоном от 3 до 20 согласно задаче
        print(f'---------------------------------------------------------------')
        print(f'- Пароль для числа {n}: \u001b[31mОшибка. Число не должно быть больше 20!')
        print(f'\u001b[0m- Кол-во переборов по циклам: {cnt}')
        print(f'---------------------------------------------------------------')
        print()
    else:
        #result, cnt = Password_num(n)
        if n < 3:
            print(f'---------------------------------------------------------------')
            print(f'Пароль для числа {n}: \u001b[31mОшибка. Число не должно быть меньше 3!')
            print(f'\u001b[0mКол-во переборов по циклам: {cnt}')
            print(f'---------------------------------------------------------------')
            print()
        else:
            print(f'---------------------------------------------------------------')
            print(f'Пароль для числа {n}: \u001b[36m{result}')
            print(f'\u001b[0mКол-во переборов по циклам: {cnt}')
            print(f'---------------------------------------------------------------')
            print()

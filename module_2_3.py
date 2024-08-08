my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Вариант 1 без continue и break
i = 0
while i < len(my_list) and my_list[i] >= 0:
    if my_list[i] == 0:
        i += 1
    else:
        print(my_list[i])
        i += 1

print()

# Вариант 2 с использованием continue
i = 0
while i < len(my_list) and my_list[i] >= 0:
    i += 1
    if my_list[i-1] == 0:
        continue
    else:
        print(my_list[i-1])

print()

# Вариант 3 с использованием break
i = 0
while i < len(my_list):
    if my_list[i] == 0:
        i += 1
    elif my_list[i] < 0:
        break
    else:
        print(my_list[i])
        i += 1

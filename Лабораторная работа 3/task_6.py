list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0

for i, current_num in enumerate(list_numbers):  # перебераем пары индекс - значение
    max_num = list_numbers[max_index]
    if current_num > max_num:  # если текущее число больше того, что встречали ранее
        max_index = i  # то перезаписываем индекс максимального числа
        max_num = list_numbers[max_index]  # и перезаписываем число

last_ = list_numbers[-1]
list_numbers[max_index] = last_
list_numbers[-1] = max_num

print(list_numbers)

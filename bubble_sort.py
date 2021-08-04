'''
Бежим по списку и, если текущее число меньше предыдущего, меняем их местами.
Самое большое число всплывает к правой крайней ячейке (right_point) как пызырек.
Добежав до конца, начинаем с начала.
В этот раз можно не добежать до правого края на один шаг
(там уже самое большое число)
'''


from random import randint

# генерируем случайный список
list_size = 20
lst = [randint(-10, 10) for i in range(list_size)]
print(*lst)

for right_point in range(len(lst) - 1, 0, -1):
    for left_point in range(1, right_point + 1):
        if lst[left_point] < lst[left_point - 1]:
            lst[left_point], lst[left_point - 1] \
                = lst[left_point - 1], lst[left_point]

print(*lst)

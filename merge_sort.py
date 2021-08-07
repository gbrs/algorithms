'''
Сортировка слиянием.
Делим список пополам. И каждый кусочек тоже делим.
Вплоть до образования списков из одного элемента.
А потом идем по дереву в "обратную" сторону:
сливаем попарно списки, но уже в нужном порядке.
'''

from random import randint


def merger(arr):
    '''сортировка слиянием, реализованная через методы списков: pop, append'''

    # print('/', arr)  # для контроля процесса разделения

    # тривиальные случаи пустого и единичного списка
    if len(arr) < 2:
        return arr

    # разделяем: располовиниваем списки
    left_arr = merger(arr[0:len(arr) // 2])
    right_arr = merger(arr[len(arr)//2:len(arr)])

    # сливаем
    sorted_arr = []
    while len(left_arr) > 0 and len(right_arr) > 0:
        sorted_arr.append(left_arr.pop(0) if left_arr[0] < right_arr[0]
                          else right_arr.pop(0))
        # print('*', sorted_arr)  # для контроля процесса слияния
    else:
        if len(left_arr) != 0:
            sorted_arr.extend(left_arr)
        else:
            sorted_arr.extend(right_arr)
    # print('*', sorted_arr)  # для контроля процесса слияния
    return sorted_arr


# генерация случайного списка
lst_size = 20
lst = [randint(-5, 5) for i in range(lst_size)]
print(*lst)

lst = merger(lst)
print(*lst)

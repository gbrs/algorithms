'''
Бежим по списку и, если текущее число меньше предыдущего, меняем их местами.
Самое большое число всплывает к правой крайней ячейке (right_point) как пызырек.
Добежав до конца, начинаем с начала.
В этот раз можно не добежать до правого края на один шаг
(там уже самое большое число)
'''

'''
Модернизация. Запоминаем место (last_swap_place), 
где мы в последний раз сделали перестановку:
после этого места все уже отсортировано. 
Все более крупные числа уже были подняты ранее.
Теперь сортируем не добегая до этого места.
Не на много-то и меньше сравнений делает в результате код:
очень редко < 490 000 для 1 000 элементов (без оптимизации - 499 500)
'''


from random import randint

# генерируем случайный список
list_size = 1000
lst = [randint(-500, 500) for i in range(list_size)]
print(lst)

right_point = len(lst) - 1
while right_point >= 1:
    last_swap_place = 0
    for left_point in range(1, right_point + 1):
        if lst[left_point] < lst[left_point - 1]:
            lst[left_point], lst[left_point - 1] \
                = lst[left_point - 1], lst[left_point]
            last_swap_place = left_point
    right_point = last_swap_place - 1

print(lst)

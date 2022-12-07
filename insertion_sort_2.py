'''
Сортировка вставками (англ. Insertion sort) — алгоритм сортировки,
в котором элементы просматриваются последовательно
и размещается в нужное место среди ранее упорядоченных элементов
циклическим сдвигом вправо.
'''

from random import randint

# генерируем случайный список
LIST_SIZE = 1000
lst = [randint(-100, 100) for i in range(LIST_SIZE)]
print(*lst)

# первый элемент - уже отсортированная часть массива, перебираем все остальные.
for i in range(1, LIST_SIZE):
    current_elem = lst[i]
    place = i
    # пробегаемся влево, смещая элементы вправо пока они больше текущего элемента
    # или пока не упремся в левый край списка
    while (place - 1) >= 0 and lst[place - 1] >= current_elem:
        lst[place] = lst[place - 1]
        place -= 1
    # вставляем текущий элемент
    lst[place] = current_elem

print(*lst)

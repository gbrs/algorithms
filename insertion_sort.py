# TODO недоделан

'''
Сортировка вставками (англ. Insertion sort) — алгоритм сортировки,
в котором элементы просматриваются последовательно
и размещается в нужное место среди ранее упорядоченных элементов
циклическим сдвигом вправо.
'''

from random import randint

# генерируем случайный список
list_size = 5
# lst = [randint(-10, 10) for i in range(list_size)]
lst = [7, 6, 9, 8, 1]
spam = None
print(0, 0, 0, *lst)

for i in range(1, list_size):
    for j in range(i - 1, -1, -1):  # обратное движение обеспечит устойчивость сортировки
        if lst[j] <= lst[i]:
            spam = lst[i]
            # сдвиг вправо
            for k in range(i, j + 1, -1):
                lst[k] = lst[k - 1]
            lst[j + 1] = spam
            break
        else:
            spam = lst[i]
            # сдвиг вправо
            for k in range(i, 0, -1):
                lst[k] = lst[k - 1]
            lst[0] = spam

    print(i, j, spam, *lst)




'''
Сортировка вставками (англ. Insertion sort) — алгоритм сортировки,
в котором элементы просматриваются последовательно
и размещается в нужное место среди ранее упорядоченных элементов
циклическим сдвигом вправо.
'''

# переусложнил. Смотри вариант 2


from random import randint

# генерируем случайный список
list_size = 1000
lst = [randint(-100, 100) for i in range(list_size)]
spam = None
print(*lst)

# первый элемент - уже отсортированная часть массива,
# перебираем все остальные.
for i in range(1, list_size):
    # пробегаем отсортированную часть массива (до i),
    # подыскивая подходящее место для вставки.
    # Обратное движение обеспечит устойчивость сортировки
    for j in range(i - 1, -1, -1):
        if lst[j] <= lst[i]:
            spam = lst[i]
            # сдвиг вправо
            for k in range(i, j, -1):
                lst[k] = lst[k - 1]
            # вставка текущего элемента в нужное место
            lst[j + 1] = spam
            break
    # если не нашли подходящего места - значит текущий элемент надо вставить в начало
    else:
        spam = lst[i]
        for k in range(i, 0, -1):
            lst[k] = lst[k - 1]
        lst[0] = spam
    # print(*lst)

print(*lst)

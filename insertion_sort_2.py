'''
Сортировка вставками (англ. Insertion sort) — алгоритм сортировки,
в котором элементы просматриваются последовательно
и размещаются в нужное место среди ранее упорядоченных элементов
циклическим сдвигом вправо. Отсортированная часть каждый раз увеличивается, соответственно
'''

def generate_random_list(list_size):
    '''
    генерация случайного списка из целых чисел
    :param list_size: размер генерируемого списка
    :return: list int, список из целых чисел
    '''
    from random import randint
    range_of_values = list_size // 2
    return [randint(-range_of_values, range_of_values) for i in range(list_size)]


def find_insertion_place(i):
    '''
    пробегаем отсортированную часть массива (до i), подыскивая подходящее место для вставки.
    Обратное направление поиска места обеспечит устойчивость сортировки
    :param i: int, номер текущего элемента
    :return: int, номер места для вставки
    '''
    for j in range(i - 1, -1, -1):
        if lst[j] <= lst[i]:
            return j + 1
    return 0


def find_insertion_place_binary(i):
    left = 0
    right = i - 1
    if lst[i] < lst[left]:
        return 0
    if lst[i] > lst[right]:
        return i
    while lst[left] < lst[right]:
        middle = (right + left) // 2
        if lst[i] < lst[middle]:
            right = middle
        else:
            left = middle
    return left + 1


def shift_cyclically_right(i, insertion_place):
    '''
    циклический сдвиг элементов вправо
    :param i: int, номер текущего числа
    :param insertion_place: int, номер места, куда надо вставить текущее число
    :return: None
    '''
    spam = lst[i]
    for k in range(i, insertion_place, -1):
        lst[k] = lst[k - 1]
    lst[insertion_place] = spam


list_size = 50
lst = generate_random_list(list_size)
print(*lst)

# первый элемент - уже отсортированная часть массива,
# перебираем все остальные, добавляя их в нужные места отсортированной части.
for i in range(1, list_size):
    insertion_place = find_insertion_place(i)
    shift_cyclically_right(i, insertion_place)

print(*lst)

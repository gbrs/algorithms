'''
Сортировка вставками (англ. Insertion sort) — алгоритм сортировки,
в котором элементы просматриваются последовательно
и размещаются в нужное место среди ранее упорядоченных элементов
циклическим сдвигом вправо. Отсортированная часть каждый раз увеличивается
на единицу
'''

def generate_random_list(list_size):
    """
    генерация случайного списка из целых чисел
    :param list_size: размер генерируемого списка
    :return: list int, список из целых чисел
    """
    from random import randint
    range_of_values = list_size // 2
    return [randint(-range_of_values, range_of_values) for i in range(list_size)]


def find_insertion_place(current):
    """
    пробегаем отсортированную часть массива (до current), 
    подыскивая подходящее место для вставки линейным поиском.
    Обратное направление поиска места обеспечит устойчивость сортировки
    :param current: int, номер текущего элемента
    :return: int, номер места для вставки
    """
    for j in range(current - 1, -1, -1):
        if lst[j] <= lst[current]:
            return j + 1
    return 0


def find_insertion_place_binary(current):
    """
    в отсортированной части массива (до current)
    подыскиваем подходящее место для вставки бинарным поиском,
    используя пару указателей: left и right.
    Работает с глобальным списком lst, но не изменяет его.
    :param current: int, номер текущего элемента
    :return: int, номер места для вставки
    """
    left = 0
    right = current - 1
    if lst[current] < lst[left]:
        return 0
    if lst[current] > lst[right]:
        return current
    # не забывам обработать случай, когда левый и правый указатель впритык друг к другу подошли
    while lst[left] < lst[right] and right - left > 1:
        middle = (right + left) // 2
        if lst[current] < lst[middle]:
            right = middle
        else:
            left = middle
    return right


def find_insertion_place_bisect(current):
    """
    в отсортированной части массива (до current) модуль bisect
    подыскивает подходящее место для вставки.
    Работает с глобальным списком lst, но не изменяет его.
    :param current: int, номер текущего элемента
    :return: int, номер места для вставки
    """
    from bisect import bisect
    return bisect(lst[0:current], lst[current])


def shift_cyclically_right(current, insertion_place):
    """
    циклический сдвиг элементов вправо.
    side effect: Изменяет глобальный список lst.
    :param current: int, номер текущего числа
    :param insertion_place: int, номер места, куда надо вставить текущее число
    :return: None
    """
    spam = lst[current]
    for k in range(current, insertion_place, -1):
        lst[k] = lst[k - 1]
    lst[insertion_place] = spam


LIST_SIZE = 40
lst = generate_random_list(LIST_SIZE)
# lst = [-5, -11, 12, 7, 15]
print(*lst)

# первый элемент - уже отсортированная часть массива,
# перебираем все остальные элементы, добавляя их в нужные места отсортированной части.
for i in range(1, LIST_SIZE):
    insertion_place = find_insertion_place_bisect(i)
    shift_cyclically_right(i, insertion_place)
    # print(*lst)

print(*lst)


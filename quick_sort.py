"""
Выбираем некий опорный элемент. Есть более эффективные способы,
но для простоты я выбираю первый элемент.
Все числа меньше и равные опорному должны оказаться слева от него,
а бОльшие - справа. Данная схема использует два флага
(один в начале массива (сразу за опорным), другой на последней позиции),
которые приближаются друг к другу, пока не найдётся пара элементов,
где один больше опорного и расположен перед ним, а второй меньше и расположен после.
Эти элементы меняются местами. Обмен происходит до тех пор, пока флаги не встретятся.
Ставим опорный элемент между бОльшими и меньшими элементами.
Потом рекурсивно сортируем  списки слева и справа.
"""


def generate_random_list(list_size):
    """
    генерация случайного списка из целых чисел
    :param list_size: размер генерируемого списка
    :return: list int, список из целых чисел
    """
    from random import randint
    range_of_values = list_size // 2
    return [randint(-range_of_values, range_of_values) for i in range(list_size)]


def sort_quickly(lst, start, end):
    """
    рекурсивно вызываем сортировку для элементов слева и отдельно справа от опорного.
    Если элементов меньше трех, то ничего не надо делать: мы их уже отсортировали.
    :param lst: list, сортируемый список
    :param start: int, первый элемент сортируемого участка
    :param end: int, последний элемент сортируемого участка (точнее на 1 больше)
    :return: None
    """
    if end - start > 1:
        pivot = share_elements(lst, start, end)
        sort_quickly(lst, start, pivot)
        sort_quickly(lst, pivot + 1, end)


def share_elements(lst, start, end):
    """
    распределение элементов сортируемого участка матрицы: маленькие налево,
    большие направо. Опорным элементом берем первый. Создаем два флага -
    левый и правый - на границах сортируемой части массива. Смещаем левый флаг
    пока не найдем элемент больше опорного, а правый - пока не найдем меньше опорного.
    Обмениваем эти элементы местами.
    В конце между большими и маленькими элементами ставим опорный элемент
    и возвращаем его место в списке.
    :param lst: list, сортируемый список
    :param start: int, первый элемент сортируемого участка
    :param end: int, последний элемент сортируемого участка (точнее на 1 больше)
    :return: right - место положения правого флага
    """

    pivot = lst[start]
    left = start + 1
    right = end - 1

    while True:
        # смещение флагов
        while (left <= right and lst[left] <= pivot):
            left += 1
        while (left <= right and lst[right] >= pivot):
            right -= 1
        # обмен элементов
        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]
        # помещение опорного элемента между маленькими и большими элементами
        else:
            lst[start], lst[right] = lst[right], lst[start]
            return right


LIST_SIZE = 30
lst = generate_random_list(LIST_SIZE)
print(*lst)
sort_quickly(lst, 0, LIST_SIZE)
print(*lst)

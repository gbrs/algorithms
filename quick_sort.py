"""
Выбираем некий опорный элемент. Есть более эффективные способы,
но для простоты я выбираю последний элемент.
Все числа меньше и равные опорному должны оказаться слева от него,
а бОльшие - справа. Данная схема использует два индекса
(один в начале массива, другой на предпоследней позиции - перед опорным),
которые приближаются друг к другу, пока не найдётся пара элементов,
где один больше опорного и расположен перед ним, а второй меньше и расположен после.
Эти элементы меняются местами. Обмен происходит до тех пор, пока индексы не пересекутся.
Алгоритм возвращает последний индекс и на это место меняется опорный элемент.
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


def find_left_larger(left, right, base):
    while left < right:
        if lst[left] <= base:
            left += 1
        else:
            return left
    return left


def find_right_larger(left, right, base):
    while left < right:
        if lst[right] > base:
            right -= 1
        else:
            return right
    return right


def sort_quickly(start, stop):
    print(start, stop)
    if start < stop:
        base = lst[stop + 1]
        left = find_left_larger(start, stop, base)
        right = find_right_larger(start, stop, base)
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            print('swap ', *lst)
            left = find_left_larger(left, right, base)
            right = find_right_larger(left, right, base)
        lst[stop + 1], lst[left] = lst[left], lst[stop + 1]
        print('base ', *lst)
        sort_quickly(start, left - 2)
        sort_quickly(left + 1, stop - 1)



LIST_SIZE = 9
# lst = generate_random_list(LIST_SIZE)
lst = [4, 3, 2, 1, -1, -2, -3, -4, 0]
print('start', *lst)

sort_quickly(0, LIST_SIZE - 2)
print('stop ', *lst)

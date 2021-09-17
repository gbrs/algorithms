"""
Разновидность сортировки пузырьком.
Бежим по списку и, если текущее число больше следующего, меняем их местами.
Самое большое число всплывает к правой границе (right_border) словно пызырек.

Запоминаем место (last_swap_place), где мы в последний раз сделали перестановку:
после этого места все уже отсортировано. Все более крупные числа уже были подняты ранее.
В следующий раз будем сортировать только до этого места: перемещаем сюда right_border.

Добежав до конца не начинаем с начала, а идем влево: гоним пузырьки малых чисел влево.
Здесь работаем уже с left_border.
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


def move_bubble_right(left_border, right_border):
    """
    гонит пузырьки больших чисел вправо, запоминая место последнего обмена last_swap_place
    :param left_border: int, левая граница неотсортированного участка
    :param right_border: int, правая граница неотсортированного участка
    :return: int, место последнего обмена, именно до сюда теперь надо гнать пузырьки в следующий раз
    side effects: сортирует глобальный массив lst
    """
    last_swap_place = left_border
    for current_number in range(left_border, right_border):
        if lst[current_number] > lst[current_number + 1]:
            lst[current_number], lst[current_number + 1] \
                = lst[current_number + 1], lst[current_number]
            last_swap_place = current_number
    return last_swap_place


def move_bubble_left(left_border, right_border):
    """
    гонит пузырьки малых чисел влево, запоминая место последнего обмена last_swap_place
    :param left_border: int, левая граница неотсортированного участка
    :param right_border: int, правая граница неотсортированного участка
    :return: int, место последнего обмена, именно до сюда теперь надо гнать пузырьки в следующий раз
    side effects: сортирует глобальный массив lst
    """
    last_swap_place = right_border
    for current_number in range(right_border, left_border, -1):
        if lst[current_number] < lst[current_number - 1]:
            lst[current_number], lst[current_number - 1] \
                = lst[current_number - 1], lst[current_number]
            last_swap_place = current_number
    return last_swap_place


LIST_SIZE = 30
lst = generate_random_list(LIST_SIZE)

# левая и правая границы неотсортированного участка
left_border = 0
right_border = len(lst) - 1
print(f'{left_border: < 4}, {right_border: < 4}, {lst}')

while right_border > left_border:
    right_border = move_bubble_right(left_border, right_border)
    left_border = move_bubble_left(left_border, right_border)

print(f'{left_border: < 4}, {right_border: < 4}, {lst}')

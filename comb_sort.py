"""
Сортировка расчёской (англ. comb sort) улучшает сортировку пузырьком.
Основная идея — устранить черепах - маленькие значения в конце списка, которые крайне замедляют сортировку пузырьком
(кролики, большие значения в начале списка, не представляют проблемы для сортировки пузырьком).
В сортировке пузырьком расстояние между сравниваемыми элементами равно 1.
Первоначально берем расстояние n - 1 между сравниваемыми элементами (сравнивая крайние элементы),
а по мере упорядочивания массива сужаем это расстояние пока разность индексов не достигнет единицы.
Надо только один раз пройти с шагом единица.
Оптимальное значение фактора уменьшения шага - 1,247.

Впечатляюще ускоряет.
Для 1 000 элементов сравнений при неоптимизированном "пузырьке" д.б. 499 500 сравнений.
Здесь же, как правило не более 23000. И почему-то очень часто сравнений чуть-чуть больше 22000
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


def generate_step(step):
    """
    генерирует следующее значение шага: в 1.247 раза меньше предыдущего
    :param step: int, предыдущее значение шага
    :return: int, следующее значение шага (округленное вниз)
    """
    next_step = step / 1.247
    return int(next_step)


def move_bubble_right_by_jump(step):
    """
    гонит пузырьки больших чисел вправо, но не обязательно соседних элементов,
    а отстоящих друг от друга на step, изменяющийся при каждом вызове функции
    :param step: int, шаг, на который отстоят друг от друга обмениваемые элементы
    :return: None
    side effects: сортирует глобальный массив lst
    """
    current_number = 0
    while current_number + step < LIST_SIZE:
        if lst[current_number] > lst[current_number + step]:
            lst[current_number], lst[current_number + step] \
                = lst[current_number + step], lst[current_number]
        current_number += 1


LIST_SIZE = 1000
lst = generate_random_list(LIST_SIZE)
step = LIST_SIZE - 1
print(f'{step: < 4}, {lst}')

# сортируем сперва с большим шагом, но каждый раз шаг уменьшаем
while step > 0:
    move_bubble_right_by_jump(step)
    # print(f'{step: < 4}, {lst}')
    step = generate_step(step)

print(f'{step: < 4}, {lst}')

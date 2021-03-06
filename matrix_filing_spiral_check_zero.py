"""
заполнение спиралью матрицы n на m
"""

"""
Я обычно ставлю метки на границы и их аккуратно пытаюсь двигать.
Много проще заполнить все нулями или Noneами и разворачиваться,
когда дошли до границы или уже заполненных ячеек.
"""


# n, m = map(int, input().split())
N, M = 5, 7
lst = [[None] * M for _ in range(N)]
cnt = 0
row = 0
col = -1
while cnt < N * M:

    """
    Бежим по верхней строке вправо и заполняем каунтами пока либо не упремся в стенку
    (это будет только в первый раз), либо не наткнемся на уже заполненную часть матрицы
    (там не Noneы).
    Вообще можно короче написать: while lst[row][(col + 1) % m] is None.
    В ячейке [0][0] уже не None.
    """
    while col < M - 1 and lst[row][col + 1] is None:
        col += 1
        cnt += 1
        lst[row][col] = cnt

    while row < N - 1 and lst[row + 1][col] is None:  # справа бежим вниз
        row += 1
        cnt += 1
        lst[row][col] = cnt

    """
    Можно отказаться от проверки на границу, все итак сработает: в ячейке [row][-1] уже не None.
    Достаточно: while lst[row][col - 1] is None
    """
    while col > 0 and lst[row][col - 1] is None:  # снизу бежим влево
        col -= 1
        cnt += 1
        lst[row][col] = cnt

    while row > 0 and lst[row - 1][col] is None:  # слева бежим вверх
        row -= 1
        cnt += 1
        lst[row][col] = cnt

[print(*r) for r in lst]


"""
ИДЕИ РЕШЕНИЯ
Заполнять прямоугольниками, начиная с ячейки [0][0], потом [1][1] и т.д.
Сделать один цикл от 1 до n * m и внутри него по условию менять "угол" с которого идем и шаги:
    (1, 0) -> (0, 1) -> (-1, 0) -> (0, -1) -> ...

ЧАСТНОСТИ
Заполнить матрицу нулями и заполнять ее ориентируясь на нули.
"""

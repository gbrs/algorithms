"""
заполнение спиралью матрицы n на m
"""


# генерация исходного списка
n, m = [int(i) for i in input().split()]
lst = [[None] * m for _ in range(n)]

# счетчик, который будет давать нам числа, которыми мы заполняем спираль
cnt = 1 - 2

# маркеры, показывающие на границу незаполненного участка
top = 0
bottom = n
left = -1
right = m


while True:
    # заполняем матрицу по спирали, начиная с верхней строки

    # сперва подтягиваем дальнюю границу к себе
    right -= 1
    # если границы не совпадают, то заполняем строчку/столбик
    if left < right:
        for i in range(left, right):
            cnt += 1
            lst[top][i] = cnt
    # если же граница совпала, то заполняем последний элемент
    # и брекаем всё
    else:
        cnt += 1
        lst[top][right] = cnt
        break

    bottom -= 1
    if top < bottom:
        for i in range(top, bottom):
            cnt += 1
            lst[i][right] = cnt
    else:
        cnt += 1
        lst[bottom][right] = cnt
        break

    left += 1
    if left < right:
        for i in range(right, left, -1):
            cnt += 1
            lst[bottom][i] = cnt
    else:
        cnt += 1
        lst[bottom][left] = cnt
        break

    top += 1
    if top < bottom:
        for i in range(bottom, top, -1):
            cnt += 1
            lst[i][left] = cnt
    else:
        cnt += 1
        lst[top][left] = cnt
        break

[print(*row) for row in lst]

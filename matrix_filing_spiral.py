"""
заполнение спиралью матрицы n на m
"""


# генерация исходного списка
n, m = [int(i) for i in input().split()]
lst = [[None] * m for _ in range(n)]

# счетчик, который будет давать нам числа, которыми мы заполняем спираль
cnt = 1 - 2

'''
маркеры, показывающие на границу незаполненного участка.
Имеют такие значения, поскольку потом мы их подтягиваем к себе
'''
top = 0
bottom = n
left = -1
right = m


while True:
    # заполняем матрицу по спирали, начиная с верхней строки

    # сперва подтягиваем дальнюю границу к себе
    right -= 1
    # если границы не совпадают, то заполняем строчку/столбик
    '''на первом заходе возникает артефакт и мы заполняем сначала нулем
    правый верхний угол. Потом мы его перезапишем'''
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

'''
n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]
dr, dc, r, c = 0, 1, 0, 0

for cnt in range(1, n * m + 1):
    a[r][c] = cnt
    
    if a[(r + dr) % n][(c + dc) % m]:
        dr, dc = dc, -dr

    r += dr
    c += dc    
    
for row in a:
    print(*(f'{e:<3}' for e in row), sep='')
'''

'''
ИДЕИ РЕШЕНИЯ
Заполнять прямоугольниками, начиная с ячейки [0][0], потом [1][1] и т.д.
Сделать один цикл от 1 до n * m и внутри него по условию менять "угол" 
с которого идем и шаги:
    (1, 0) -> (0, 1) -> (-1, 0) -> (0, -1) -> ...

ЧАСТНОСТИ
Заполнить матрицу нулями и заполнять ее ориентируясь на нули.
'''

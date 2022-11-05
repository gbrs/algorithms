"""
Бинарный поиск. Ведется в отсортированном массиве.
Смотрим средний элемент center, если не совпадает, то если искомый элемент меньше среднего,
то ищем в середине подмассива, оставшегося слева и наоборот?.
Для этого смещаем границы left и right, обозначающие подмассив, в котором ищем.
"""

from random import randint

# генерируем список и число, которое будем искать
N = 20
lst = [randint(0, N - 1) for _ in range(N)]
lst.sort()
print(*lst)

request = randint(0, N - 1)
print(request, end=' ')

# левая и правая границы списка, в котором ищем число
left = 0
right = N - 1

# если искомое число больше/меньше искомого, смещаем соответствующую границу
while left <= right:
    center = (left + right) // 2
    if lst[center] == request:
        print(f'in position {center + 1}')
        break
    elif lst[center] < request:
        left = center + 1
    else:
        right = center - 1
else:
    print('is not in list')

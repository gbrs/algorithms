'''
Сортировка выбором
Бежим по списку до конца и находим минимальное значение. Обмениваем это значение
с первым элементом. Затем начиная со второго элемента ищем минимальное значение и
обмениваем это значение со вторым элементом. И т.д., всего (n - 1) раз
'''


from random import randint

# генерируем случайный список
list_size = 20
lst = [randint(-10, 10) for i in range(list_size)]
print(*lst)

for place_for_min in range(len(lst) - 1):
    mn = float('inf')
    for current_place in range(place_for_min, len(lst)):
        if lst[current_place] < mn:
            mn = lst[current_place]
            current_min_place = current_place
    lst[place_for_min], lst[current_min_place] \
        = lst[current_min_place], lst[place_for_min]

print(*lst)

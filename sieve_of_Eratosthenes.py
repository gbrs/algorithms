'''2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
'''


from math import ceil  # округление вверх

def erat(start, stop):
    '''строит решето Эратосфена для элементов от start до stop
    '''

    # достраиваю к решету Sieve_size элементов True.
    # Наверняка можно было и без цикла решить, но "нешмогла"
    for k in range(Sieve_size):
        sieve.append(True)

    # заполнение Falseами первой части решета.
    # Не смог придумать как не выделять этот случай
    if start == 0:
        sieve[0] = sieve[1] = False
        for k in range(2, stop // 2):
            if sieve[k]:
                for j in range(2 * k, stop, k):
                    sieve[j] = False

    # заполнение Falseами всех остальных частей решета
    else:
        for k in range(2, stop // 2):
            if sieve[k]:
                for j in range(ceil(start / k) * k, stop, k):
                    sieve[j] = False


# Решето; размер блоков, которыми последовательно достраиваем решето;
# начало очередного блока; счетчик найденных простых чисел.
''' Как переменные делать глобальными? Пайтон ругается на неопреленность переменных внутри функции
даже после global ... Поэтому всё передал "ручками" в функцию main. А erat не ругался ни на что...
'''
sieve = []
Sieve_size = 1000
start = 0
cnt_prime = 0
number_prime = int(input("Какое по счету простое число вы хотите найти? "))

# последовательно достраиваем решето Эратосфена
# пока не найдем достаточно простых чисел
while cnt_prime < number_prime:
    stop = start + Sieve_size
    erat(start, stop)
    cnt_prime += sieve[start:stop].count(True)
    start += Sieve_size

# поиск нужного по счёту простого числа (от конца к началу).
# Не нашёл нужный встроенный метод для списков
i = stop
while cnt_prime >= number_prime:
    i -= 1
    if sieve[i]:
        cnt_prime -= 1
else:
    print(i)

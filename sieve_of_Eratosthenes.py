'''Написать алгоритм нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
'''


from math import ceil  # округление вверх


def make_sieve(start, stop):
    '''строит решето Эратосфена для элементов от start до stop
    '''

    # достраиваю к решету Sieve_size элементов True.
    sieve.extend([True] * sieve_size)

    # заполнение Falseами первой части решета.
    # Не смог придумать как не выделять этот случай
    if start == 0:
        sieve[0] = sieve[1] = False
        for k in range(2, stop // 2):
            if sieve[k]:
                for j in range(2 * k, stop, k):
                    sieve[j] = False
    # заполнение Falseами всех остальных, последовательно добавляемых, частей решета
    else:
        for k in range(2, stop // 2):
            if sieve[k]:
                for j in range(ceil(start / k) * k, stop, k):
                    sieve[j] = False


# решето; размер блоков, которыми последовательно достраиваем решето;
# начало очередного блока; счетчик найденных простых чисел, номер искомого простого
sieve = []
sieve_size = 137
start = 0
cnt_prime = 0
# number_prime = 10000
number_prime = int(input("Какое по счету простое число вы хотите найти? "))

# последовательно достраиваем решето Эратосфена
# пока не найдем достаточно простых чисел
while cnt_prime < number_prime:
    stop = start + sieve_size
    make_sieve(start, stop)
    cnt_prime += sieve[start:stop].count(True)
    start += sieve_size

# поиск нужного по счёту простого числа (от конца к началу).
# Не нашёл нужный встроенный метод для списков
i = stop
while cnt_prime >= number_prime:
    i -= 1
    if sieve[i]:
        cnt_prime -= 1
else:
    print(i)

# 10 000-чное число - 104 729
# 495-е простое - 3539

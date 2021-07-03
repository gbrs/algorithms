'''
найти наибольший общий делитель (greatest common divisor) для 1, 2, 3 и более чисел
'''


'''
Если разложить каждое число на простые множители, 
то НОД - произведение тех же простых делителей 
с наименьшими степенями, встречающимися у данных нам чисел.
Отсюда очевидно, что можно найти НОД_1 пары чисел,
а потом найти НОД(НОД_1, третье число). И т.д.
'''


'''
Подаю список на вход функции, она рекурсивно вызывает себя для:
- первого элемента;
- НОД всех последующих элементов.
И т.д.
Тривиальные случаи:
- для одного числа НОД - само число; 
- для двух - классический алгоритм Евклида (см. Euclidian_algorithm) 
'''


def gcd(numbers_list):
    if len(numbers_list) == 1:
        return numbers_list[0]
    if len(numbers_list) == 2:
        if not numbers_list[1]:
            return numbers_list[0]
        return gcd([numbers_list[1], numbers_list[0] % numbers_list[1]])
    return gcd([numbers_list[0], gcd(numbers_list[1:])])


input()
input_list = list(map(int, input().split()))

print(f'Greatest common divisor: {gcd(input_list)}')


'''
4
4211844399 366003099 3083730215643 1045044099
Answer: 3249
'''

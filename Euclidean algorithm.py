'''
найти наибольший общий делитель (greatest common divisor) пары чисел
'''


'''
Пусть number_1 >= number_2. 
Если number_1 делится на некоторый делитель и number_2 на него делится,
то и (number_1 - number_2) тоже делится. Заменяем number_1 на (number_1 - number_2).
И так продолжаем пока number_1 не станет нулем.
Оставшееся число и будет НОДом.
'''


'''
Не важно какое из двух чисел больше: мы все время, вызывая функцию,
переставляем их местами. Просто, лишний шажок в начале может быть.
'''


def gcd(number_1, number_2):
    if not number_2:
        return number_1
    return gcd(number_2, number_1 % number_2)


print(f'Greatest common divisor: {gcd(12, 18)}')

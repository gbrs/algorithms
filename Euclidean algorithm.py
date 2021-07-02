'''
greatest common divisor
не важно какое из двух чисел больше: мы все время, вызывая функцию,
переставляем их местами; просто, лишний шажок будет
'''

def gcd(number_1, number_2):
    if not number_2:
        return number_1
    return gcd(number_2, number_1 % number_2)


print(f'Greatest common divisor: {gcd(12, 18)}')

'''
Проходим по списку/строке и подсчитаем количество вхождений каждого элемента.
А затем выводим элементы в "алфавитном" порядке столько раз, сколько мы насчитали.
Целесообразна лишь тогда, когда сортируемые сортируемых значений мало
по сравнению с сортируемым множеством.
'''

from random import choice
from collections import Counter

# случайная генерация текста из заданного набора символов
text = ''
text_length = 80
used_symbols = 'jhjkYhxKl kGxh3470->?/<Q'
alphabet = tuple(set(used_symbols))
for _ in range(text_length):
    text = ''.join((text, choice(alphabet)))

count_dictionary = dict(Counter(text))

for symbol in sorted(count_dictionary):
    for _ in range(count_dictionary[symbol]):
        print(symbol, end='')
print()

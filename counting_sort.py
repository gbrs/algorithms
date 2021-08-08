'''
Проходим по списку/строке и подсчитаем количество вхождений каждого элемента.
А затем выводим элементы в "алфавитном" порядке столько раз, сколько мы насчитали.
Целесообразна лишь тогда, когда сортируемые сортируемых значений мало
по сравнению с сортируемым множеством.
'''


from random import choice
# from collections import Counter

# случайная генерация текста из заданного набора символов
TEXT_LENGTH = 80
text = ''
used_symbols = 'jhjkYhxKl kGxh3470->?/<Q'
alphabet = tuple(set(used_symbols))
for _ in range(TEXT_LENGTH):
    text = ''.join((text, choice(alphabet)))

# подсчитываем количество вхождений для каждого символа, используя словарик
# count_dictionary = dict(Counter(text))  # решение с помощью collections.Counter
count_dictionary = dict()
for symbol in text:
    count_dictionary[symbol] = count_dictionary.setdefault(symbol, 0) + 1

# создание сортированного списка
sorted_list = []
for symbol in sorted(count_dictionary):
    for _ in range(count_dictionary[symbol]):
        sorted_list.append(symbol)
print(*sorted_list, sep='')

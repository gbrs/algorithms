# Рекурсивная генерация

https://algorithmica.org/tg/object-generation

Конечно же в яп есть готовые решения: 
C++ - std::next_permutation, 
python - модуль itertools (product, combinations, permutations).

Общая идея генерации через рекурсивную функцию:  
```python
def gen(prefix=[] уже нагенерированный лучше по ссылке, еще какие-то числа описывающие генерацию):
  if (условие успешного окончания генерации):
    print(ответ)
    return
  if (условие окончания генерации из-за дальнейшей нецелесообразности; только в некоторых задачах):
    return (так сказать break)
  for перебор возможных вариантов:
    prefix.append(вариант)
    gen(prefix, ...)
    prefix.pop()  # правило скаута. Обязательно чистим после себя
```

## Генерация всех двоичных чисел
Число длиной n. Цифры: 0 или 1. Вывести все в лексикографическом порядке.  
```python
def gen(n, prefix=[]):
  if len(prefix) == n:
    print(''.join(prefix))
    return
  
  prefix.append('0')
  gen(n, prefix)
  prefix.pop()

  prefix.append('1')
  gen(n, prefix)
  prefix.pop()

gen(3)
```

## Генерация всех k-ичных чисел
Число длиной n. Цифры: от 0 до k-1. Вывести все в лексикографическом порядке.  
```python
def gen(n, k, prefix=[]):
  if len(prefix) == n:
    print(''.join(prefix))
    return
  
  for i in range(k):
    prefix.append(str(i))
    gen(n, k, prefix)
    prefix.pop()

gen(n, k)
```

## Перебор перестановок
Перестановки n чисел (подряд идущих от 0 до n-1). Вывести все в лексикографическом порядке.
```python
def gen(n, used, prefix=[]):
  if len(prefix) == n:
    print(' '.join(prefix))
    return
  
  for i in range(n):
    if not used[i]:
      used[i] = True
      prefix.append(str(i))
      
      gen(n, used, prefix)
      
      used[i] = False
      prefix.pop()

n = 4
used = [False] * n  # использовано ли уже число в этой генерации
gen(n, used)
```





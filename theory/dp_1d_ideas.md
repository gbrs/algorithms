# Динамическое программирование

https://www.youtube.com/watch?v=hE0k1aLmzHk
https://youtu.be/hE0k1aLmzHk?feature=shared&t=2950

В любой задаче дп 4 шага:
1. Как описать подзадачу, которую мы будем решать на каждом шаге. dp[i] = ...
2. База. Например, dp[0] = ...
3. Переход. Как выразить dp[i] через другие - уже посчитанные dpшки?
4. Где именно в dp лежит ответ, как его получить?

Часто очень удобно в начале массива исходных данных добавить "лишние элементы", 
чтобы не надо было на краю массива рассматривать особые случаи, обкладываясь ifами. 
Значения этих элементов - в зависимости от задачи.

Динамика бывает 2 типов:
- Сверху вниз — это использование рекурсивной функции с мемоизацией.
- Снизу вверх. Последовательно решаются все промежуточные подзадачи и запоминаются ответы. Нет ограничения 
на глубину рекурсии и допзатрат на вызовы функций. Но будут вычислены все промежуточные значения, даже если они 
не были нужны. Есть два варианта заполнения. Прямой порядок — решение подзадачи вычисляется на основе уже известных 
и сразу заносится в «таблицу». Обратный порядок — к тому моменту, как мы «пришли» к подзадаче, ответ на неё 
уже вычислен. И мы подправляем ответ на подзадачи, которые от текущей зависят.

## Количество путей
С n-ой ступени мячик может спрыгивать на 1, 2 или 3 ступеньки. 
Сколько путей добраться до пола?

dp[i] - количество путей для попадания на i-ую ступеньку  
dp[n] = 1; dp[n - 1] = 2; dp[n - 2] = 3  
dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]  
Ответ в dp[0]  
Заполняем массив с правого конца


## Платная лестница
За ступание на ступеньку надо заплатить сколько на ней написано ai. 
Человечек умеет на следующую или через одну.

dp[i] - минимальная цена для попадания на i-ую ступеньку  
dp[0] = 0  
dp[1] = a1  
dp[i] = ai + min(dp[i - 2], dp[i - 1])  
Ответ в dp[n]


## Черепашка
Поле m*n, в ячейках разное количество монеток a[i][j]. Черепашка ползет из ячейки (1, 1) в (m, n). 
Может влево или вниз. Сколько максимально может собрать монеток черепашка? 

dp[i][j] - максимальное количество монеток, которое мы можем собрать дойдя до ячейки (i, j)
dp[0][*] = 0; dp[1][1] = a[1][1]
dp[i][j] = a[i][j] + max(dp[i - 1][j], dp[i][j - 1])


## Без двух единиц
Количество бинарных строк таких, что нет подряд двух единиц

Массив 2 * n
dp[i][0] - количество подходящих строк длины i c 0 на конце
dp[i][1] - количество подходящих строк длины i c 1 на конце

dp[1][0] = dp[1][1] = 1

dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
dp[i][1] = dp[i - 1][0]

Ответ: dp[n - 1][0] + dp[n - 1][1]



## Система непересекающихся множеств (СНМ)
https://ru.algorithmica.org/cs/set-structures/dsu/  
Умеет отвечать на вопросы типа «находятся ли элементы a и b в одном множестве» и «чему равен размер данного множества». 
Часто используется в графовых алгоритмах для хранения информации о связности компонент.  
Структура должна поддерживать 2 операции:
- Объединить два каких-либо множества;
- Запросить, в каком множестве сейчас находится указанный элемент.  

Изначально у нас n элементов, каждый в своём множестве. 
В каждом множестве должен быть один "лидер". 
По его номеру мы и "называем" множество. 
Создаем массив лидеров: кто является лидером данного элемента. Заполняем его напротив индексов от 1 до n - 1 числами 
от 1 до n - 1 поскольку сейчас каждый элемент сам себе лидер.  
Множества элементов мы будем хранить в виде деревьев, пристегивая при объединении лидера одного множества к лидеру 
другого. 
Но тут надо будет оптимизировать, чтобы деревья не становились слишком глубокими, бамбукообразными.  
Для запроса в каком множестве находится какой-то элемент нужно только подняться по ссылкам до корня.  
Теперь оптимизации.  
Эвристика сжатия пути. При каждом запросе второго типа все вершины попавшиеся на пути запоминаем и потом подсоединяем 
напрямую к лидеру. Простой код, если написать рекурсивно, но можно и список пройденных вершин копить и потом 
вершины из него переподсоединить к лидеру. 
Чем больше запросов второго типа обработано, тем быстрее будут обрабатываться последующие.  
Ранговая эвристика. Менее глубокое дерево подвешиваем к более глубокому - максимальная глубина не вырастет. 
Надо вести массив рангов лидеров.  
Весовая эвристика. Меньшее по количеству элементов дерево подвешиваем к большему. Надо вести массив весов для лидеров. 
Часто в задачах про графы надо отвечать на вопросы про размер компонент связности - удобно.  


## Дерево отрезков
http://e-maxx.ru/algo/segment_tree   
Например, дан массив чисел и надо для них находить минимум: стопицот запросов типа - минимум с 12 по 37-й элемент.
Строим дерево "от этого массива": сперва минимумы для пар соседних элементов, потом слой с минимумами пар пар 
(т.е. для четверок элементов). И так до общего минимума.  
Надо создать несколько функций. Для создания дерева (build), для добавления в массив новых элементов (update; 
если такое поведение в задаче есть), для извлечения ответа (get; например, ответ на отрезке l-r).
Дерево храним в массиве. Если длина исходного массива - 2^k, то длина массива дерева - 2^(k+1). Но если такая длина 
не гарантируется, то с запасом можно выделить 4*n ячеек. Корень дерева - ячейка 1 (нулевая ячейка не задействуется). 
Адреса детей ячейки m - 2*m и 2*m+1, родителя - m // 2.  
Функция build. Строим дерево рекурсивно. Начинаем с вершинки, потом идем в ее детей (2*m и 2*m+1, при этом диапазон, 
за который отвечает узел, располовинивается) и т.д. Когда доходим до листа (диапазон становится в 1 элемент), 
ставим значение из исходных данных. На обратном ходе рекурсии вычисляем значения в узлах.  
Функция get. Ответ ищем рекурсивно. Узел отвечает за элементы исходного массива [L, R]. Если [l, r] и [L, R] 
не пересекаются, то возвращаем плюс бесконечность (для задачи поиска минимума). [L, R] внутри [l, r] - значение из узла. 
Во всех остальных случаях делим отрезок пополам и вызываем рекурсивно функцию для этих подотрезков. 
Из возвращенных чисел делается ответ на обратном ходу рекурсии.  
Функция update. Движемся рекурсивно по узлам в сторону листа изменения значения. На обратном ходе пересчитываем 
значения в родительских узлах. 



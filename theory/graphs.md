# Графы

Обычно, задачи на графы формально вообще не про графы: надо еще догадаться, что здесь узлы, а что ребра
(состояния и переходы между этими состояниями). 
Например, двумерные карты с водой и островами, комнаты со стенами (лабиринты). 
Головоломка о переливании воды с двумя сосудами (массив состояний - сколько литров в каждом ведре, 
надо аккуратно описать все возможные ходы: дополнить/опустошить/перелить; перебираем состояния пока не дойдем до 
подходящего - сколько-то литров в одном из ведер).  
Вершины могут представлять состояния в задаче (например, позиции в игре), а рёбра — переходы между ними.  
Вершины могут обозначать события, а рёбра — зависимости между ними (например, в задачах на планирование).  
Вершины могут представлять объекты, а рёбра — связи или взаимодействия между ними.  
Рёбра могут обозначать, что одно событие должно произойти перед другим.  
Массив предков для хранения на i-й позиции родителя i-й вершины.  

| Задача                                | BFS | DFS |
|:--------------------------------------|:---:|:---:|
| Поиск кратчайшего пути от a до b      |  v  |  x  |
| Проверка существования пути от a до b |  v  |  v  |
| Поиск компонент связности             |  v  |  v  |
| Поиск циклов                          |  x  |  v  |
| Проверка на двудольность              |  v  |  v  |
| Топологическая сортировка             |  x  |  v  |
| Поиск компонент сильной связности     |  x  |  v  |

Поиск циклов бфсом возможен только специфичный: для данной вершины. 
Запускаемся от нее и смотрим не появится ли в потомках эта вершина. 
Для произвольной вершины придется бфс запустить от каждой. 
Зато найдет именно минимальный цикл.  
У BFSа нет риска переполнения стека рекурсии. 

## DFS
рекурсивный DFS. Прямой обход: NLR. Бежим до левого нижнего листа, потом шаг назад и пытаемся сделать шаг правее. 
И т.д. Для шагов каждый раз вызываем рекурсивно алгоритм. Используем список смежности, ведем список уже посещенных 
вершин (это просто массив: обычно в задачах вершины задаются порядковыми номерами, и значит мы можем хранить информацию 
по соответствующему индексу массива).  
Рекурсивный вариант - классика. Простой вариант со стеком (как bfs, но вместо очереди - стек) обходит вершины 
несколько в ином порядке, что не позволяет решать некоторые задачи. 
Но можно сделать более сложный вариант, обходящий так же как и рекурсивный.  
Работает и с ориентированными, и с не ориентированными графами. Сложность O(V + E).

### Достижима ли вершина f из вершины s? 
Делаем dfs из s и смотрим отмечена ли вершина f в списке посещенных вершин.  

### Cколько вершин можно достичь из заданной вершины? 
В массиве посещенных вершин будут отмечены только достижимые вершины.  

### Поиск/раскраска/подсчет компонент связности
https://www.youtube.com/watch?v=rZkauRhHKGo   
Бежим циклом по вершинам в списке посещенных вершин и запускаем дфс от каждой еще не посещенной вершинки. 
В еще одном массиве отмечаем к какой из компонент связности относится данная вершина (для подсчета кс достаточно 
счетчика, конечно). 
Впрочем, эту информацию можно хранить и в списке посещенных вершин: 0, если не посетили, и номер кс в ином случае.  

### Поиск циклов в ориентированном графе
https://www.youtube.com/watch?v=pB83tSvoBuc  
Сначала все вершины белые (нолики в списке посещенных вершин). 
При первом посещении вершины (в начале функции дфс) красим вершину в серый - 1, 
при последнем (в конце функции дфс) - в черный (2). 
Цикл - это когда мы встречаем серую вершину (мы вошли в нее, но еще не вышли).  
Для _восстановления цикла_ создаем массив для хранения на i-й позиции родителя i-й вершины. 
Как только находим цикл брэкаем всю рекурсию (а то там же происходят перезаписывания родителей). 
Остается пробежаться по массиву родителей от вершины, замкнувшей цикл до нее же. Получившийся массив реверснуть.  

### Поиск циклов в неориентированном графе
https://www.youtube.com/watch?v=8QFS6AC0WeI  
Все так же как с ориентированным графом, только надо объяснить программе, что цикл 1-2-1 нас не устраивает.
(Разве? А не надо выкинуть окраску в черный цвет? Хотя это и не помешает, но оно не нужно). 
Поэтому передаем в функцию дфс номер родителя и не учитываем этот узел при решении вопроса о наличии цикла. 
Но считать циклы простым способом не можем.

### Двудольность графа
https://www.youtube.com/watch?v=8QFS6AC0WeI  
Решается "жадно". 
Идем дфсом и красим вершины попеременно в 1 и 2. 
Если встречаем посещенную вершину, то проверяем, окрашена ли она в противоположный цвет = 3 - цвет текущей вершины. 

### Топологическая сортировка
https://www.youtube.com/watch?v=o0P8oNXoA_w  
DAG - ориентированный ацикличный(!) граф.  
DFS делаем и на выходе из узла (лист или обошли всех детей уже) добавляем узел в массив. 
Потом, перевернув этот массив, получаем "отсортированный" список узлов ts: для любой вершины из него знаем, 
что путь в нее шел только через вершины, расположенные левее нее. 
Все ребра в этом списке идут строго слева направо. 
Вершинки левее данной точно недостижимы. 
Топологическая сортировка не единственна, но это не помешает.  
Бывают задачи, в которых надо считать не с начала списка топсорта, а с конца.  

#### Нахождения кратчайшего пути 
Во взвешенном графе решается всего за O(V + E). 
Но не забываем ограничение - только в ацикличном графе.  
Создаем "обратный" список смежности (осс): откуда в эту вершину можем прийти. 
Внешний цикл - по вершинам топологически отсортированного, внутренний - по предкам выбранной во внешнем цикле вершины 
(используем осс). 
Пробуем прорелаксировать ребро dist[i] = min(dist[i], dist[j] + длина i-j), как в Форде-Беллмане.  
В Форде-Беллмане мы наугад тыкали все пути, а здесь, благодаря осс и топсорту, мы только то, что надо перебираем.  
Какое кратчайшее расстояние до вершины a? dist[ts.index(a)]. 
Если надо все расстояния от стартовой вывести, то надо будет переложить dist по массиву ts.  

#### Нахождение количества путей до какой-то вершинки
Тот же алгоритм. cnt[i] = сумма всех cnt[j] (количеств путей до родителей).  

#### Нахождение компонент сильной связности (ксс) в ориентированном графе с циклами 
https://www.youtube.com/watch?v=-UgiBh1IMQU  
Внутри ксс можно в конце концов попасть из каждого узла в каждый. 
Узлов в ксс может быть 1, 3 и более.
В DAGе каждая вершина - свой ксс - нет же циклов.  
Создаем граф, в котором все ребра направлены в противоположном направлении. 
Делаем топсорт по этому графу (конечно, неправильно так говорить, когда граф с циклами; 
правильно: сортировка по убыванию времени выхода при dfs).
Запускаем dfs на исходном графе, но в порядке топсорта, полученного на вспомогательном графе.
Находим всю ксс для первого узла, отмечаем эти вершины, как принадлежащие первой ксс, отмечаем уже посещенные вершины. 
Ни в какую из вершин, не принадлежащих нашей ксс, мы попасть уже не сможем: ребра в нее только входят, но не выходят.  
Теперь строим ксс для следующей в топсорте вершины, которую мы еще не посетили.  

#### Конденсация графа
Каждый ксс - как бы одна вершинка в новом графе. 
В этом графе нет циклов, т.е. он является DAGом.  
Красим кссы. Рассматриваем каждое ребро графа и записываем в новый граф, если оно идет из одного цвета в другой.  

### "Карта"
https://www.youtube.com/watch?v=waXBVBKdV1s  
Двумерная карта, где 0 - вода, 1 - суша. Или комната со стенками (лабиринт).   
Можно, конечно, создать явный граф на этой основе. Но так не делают.  
Массив посещенных вершин будет матрицей такого же размера. 
Можно вместо него использовать исходную карту. 
Надо будет обходить 4/8 соседей клетки (i, j) и лучше заранее создать список кортежей[(0, 1), (0, -1), (-1, 0), (1, 0)]. 
В C++ это будут 2 массива смещений: [0, 0, -1, 1] и [1, -1, 0, 0]. 
Внутри функции дфс отмечаем клетку посещенной и бежим по созданным кортежам и прибавляем значения из них 
к координатам текущей клетки. 
Если получившаяся соседняя клетка не выходит за границы, не посещена и является сушей, то запускаем от нее рекурсивно 
дфс.  
Если надо все _острова "раскрасить"_, то снаружи цикл по списку посещенных клеток. Если клетка не посещалась 
и является сушей, то запускаем от нее дфс. Первый остров в матрице посещенных клеток "красим" единичками, 
второй - двойками и т.д.   
Если надо только _посчитать количество островов_, то можно обойтись счетчиком.

### Мосты
https://ru.algorithmica.org/cs/graph-traversals/bridges/   
Мостом называется ребро, при удалении которого связный неориентированный граф становится несвязным.  
Пусть граф ненаправленный.  
Если построим дерево dfsа, то прямые рёбра — те, по которым были переходы в dfs. Обратные рёбра — не было. 
Граф из прямых ребер - дерево. 
Обратные рёбра могут вести только «вверх» — к какому-то предку в дереве обхода графа, 
но не в другие «ветки» — иначе бы dfs увидел это ребро раньше, и оно было бы прямым, а не обратным. 
Никакое обратное ребро не может являться мостом. А некоторые прямые - могут.  
d[u] - ранг вершины в дереве dfsа (чем выше вершина, тем ниже ранг).
h_up[u] = насколько высоко можно прыгнуть из поддерева u одним прыжком.  
Ребро между точками v (выше по дереву находится) и u является мостом тогда и только тогда, 
когда из вершины u и её потомков нельзя вернуться в вершину v или подняться выше нее (hup[u] <= d[u]).  
Как считать hup для вершины u:  
hup[u] = min(
1) d[u];  
Перебираем ее соседей: 
2) если это вершина-предок v - игнорируем (continue);
3) по обратным ребрам (мы их уже посещали - используем used[w]) d[w]; 
4) соседи si по прямым ребрам - делаем в них очередной шаг dfs и получаем на выходе hup(si).  
)  
У некоторых вариантов реализации могут быть проблемы при наличии кратных ребер и петель? 

#### Реберная двусвязность
Две вершины считаются рёберно двусвязными, если между ними существуют два пути без общих ребер.  
Если из графа выбросить все мосты, 
то оставшиеся компоненты (кроме одиночных?) будут компонентами реберной двусвязности.  

### Точки сочленения
https://ru.algorithmica.org/cs/graph-traversals/bridges/   
Точкой сочленения называется вершина, при удалении которой связный неориентированный граф становится несвязным.   
Пусть граф ненаправленный.  
Алгоритм будет похож на предыдущий.  
Рассмотрим ребро v -> u. 
v является точкой сочленения, если из вершины u и из любого её потомка 
в дереве обхода в глубину нет обратного ребра 
в вершину v или какого-либо её предка. 
Т.е., если hup[u] >= d[v], то v - точка сочленения. Это единственное отличие от предыдущего алгоритма. Кроме...  
Corner case: корень (v == root). Но тут достаточно посмотреть, было ли у него более одной ветви в дереве dfsа 
(мы же могли случайно начать с конца "бамбучка"; 
а если больше одной ветви (два запуска dfs из него), то корень является точкой сочленения).  

### Эйлеров цикл
https://ru.algorithmica.org/cs/graph-traversals/euler-cycle/  
Эйлеров путь — это путь в графе, проходящий через все его рёбра по разу. 
Эйлеров цикл — это эйлеров путь, являющийся циклом.  
(Гамильтонов путь и цикл — посещение всех вершины по разу. Это задача коммивояжера).  
Пусть граф неориентированный.  
Эйлеров цикл существует тогда и только тогда, когда граф связный и степени всех вершин чётны. Проверяем это.  
Алгоритм напоминает поиск в глубину. 
Главное отличие состоит в том, что пройденными помечаются не вершины, а ребра графа.  
Делаем обход графа а-ля dfs пока не придем в вершину, из которой мы все пути обошли. 
Тогда отшагиваем назад, а последнее ребро выводим как часть ответа. 
Пробуем из этой вершины еще пошагать... И т.д. 
Таким образом мы решаем проблему с "лепестками"?  
Более технологично: начиная со стартовой вершины строим путь, 
добавляя на каждом шаге не пройденное еще ребро, смежное с текущей вершиной. 
Вершины пути накапливаем в стеке S (при рекурсивном алгоритме он сам собой образуется). 
Когда наступает такой момент, что для текущей вершины w все инцидентные ей ребра уже пройдены, 
записываем (выводим) вершины из S в ответ, пока не встретим вершину, которой инцидентны не пройденные еще ребра. 
Далее продолжаем обход по непосещенным ребрам.  
Если реализовать поиск ребер инцидентных вершине и удаление ребер за O(1), то алгоритм будет работать за O(E):  
1) можно в списке смежности хранить соседей в unordered_set и удалять их по мере обработки
   (не забывать выбрасывать и "встречное" ребро, если граф не направленный);
2) создать отдельный массив edge с информацией о ребрах (соседка, обработано ли). 
Никакой модификации структур: просто ставим отметку. 
В списке смежности тогда храним не соседей, а номера ребер из edge. 
Заметим, что при добавлении ребер неориентированного графа подряд, одно будет иметь четный номер i в edge, 
а второе - нечетный i+1. 
При отмечании одного ребра как использованного надо отметить и встречное, 
легко получить номер собрата через исключающее или: i ^ 1. 
Так мы будем, приходя в вершину i, раз за разом перебирать всех ее соседей сызнова - O(M^2). 
Введем вектор first и будем в нем хранить позицию, с которой нам надо продолжить перебирать список смежности.  

Во всех вариантах реализации нужно быть чуть аккуратнее в случае, когда в графе есть кратные ребра
(мультимножество помогает) и петли.  
Эйлеров путь существует, если нечетных вершин ровно две. 
Можно использовать решение выше. 
Соединить "нечетные" вершины ребром, построить эйлеров цикл (ведь теперь степени всех вершин четные), 
а затем удалить это ребро из цикла. Если правильно сдвинуть этот цикл, мы получили эйлеров путь. 
Альтернативно, можно просто запустить обход из одной из нечетных вершин и получить такой же результат.  

### tin, tout
Часто используемые вспомогательные массивы.  
Сначала счетчик равен 1. 
При первом входе в вершину в tin записываем значение счетчика, а потом увеличиваем счетчик на единицу. 
При последнем выходе из вершины в tout записываем значение счетчика, а потом увеличиваем счетчик на единицу. 
Корень будет иметь числа 1 и 2n.  
Тогда, например, все члены u поддерева вершины v будут иметь tin[u] >= tin[v] && tout[u] <= tout[v].  

---

## BFS

![Методы определения расстояний между всеми вершинами](../images/all_distances_table.png)

https://ru.algorithmica.org/cs/shortest-paths/bfs/
https://www.youtube.com/watch?v=4iDv8Zu8L3I  
Использование очереди - классика. 
Но, как я понял, это потому, что в других задачах на основе BFS очередь нужна. 
Сам обход можно было бы совершать просто итерируясь whileом по списку, в конец которого мы добавляем "новые" вершины.  
Создадим массив расстояний. Напротив индекса стартовой вершины - 0. В остальных сначала - плюс бесконечности. 
Кладем в очередь стартовую вершину.  
Пока очередь не пуста, извлекаем из очереди левую вершину. 
Определяем ее непосещенных соседей (у них дистанция - бесконечность; но для некоторых задач лучше условие записать: 
текущее расстояние > расстояние до родителя + 1). 
Отмечаем соседку посещенной и записываем кратчайший путь до нее: +1 к расстоянию у родительницы.  
У вершин других компонент связности расстояние останется - бесконечность.  
Работает и с ориентированными и неориентированными графами. Сложность O(V + E).

### Восстановление кратчайшего пути
Как всегда: массив предков. При каждом обновлении массива расстояний обновляем и массив предков.

### Множественный BFS
Добавив в очередь изначально не одну, а несколько вершин, 
мы найдем для каждой вершины кратчайшее расстояние до одной из них. 
Это полезно для задач, в которых нужно моделировать пожар, наводнение и т.п., в которых источник «волны» не один.  
Также так можно чуть быстрее находить кратчайший путь для конкретной пары вершин, 
запустив параллельно два обхода от каждой и остановив в тот момент, когда они встретятся.

### Все вершины, лежащие на кратчайших путях из A в B
Запускаем бфс из A. Пусть расстояние 4. Запускаем бфс из B. Получаем два массива расстояний.
(Такой трюк с двойным запуском можно провернуть с любым алгоритмом, находящим кратчайший путь.) 
На кратчайших путях лежат все вершины, для которых сумма расстояний в этих массивах равна 4. 
Ребро лежит на кратчайшем пути, если сумма расстояний от одной вершины до A и от другой до B равна 3.

### Кратчайшие циклы
Найти кратчайший цикл в ориентированном невзвешенном графе.  
Произвести поиск в ширину из каждой вершины. 
Как только в процессе обхода мы натыкаемся на уже посещённую вершину - 
нашли кратчайший цикл для данной вершины, и останавливаем обход. 
Среди всех таких найденных циклов выбираем кратчайший.

### 1-k BFS
Задача нахождения кратчайших путей от вершины s для случая, когда расстояния от 1 до некоего небольшого k
(и небольшого числа вершин?). Или есть заметное ограничение на максимальную длину кратчайшего пути.  
Решение за O(kV + E)!  
В массиве dist храним расстояния от стартовой вершины. 
Заполняем его бесконечностями, для стартовой вершины - 0.  
Создаем массив mq размера k * (n - 1) + 1 (под максимально возможное расстояние + нулевое(?)) и заполняем его очередями.
(Не понял зачем очередь нужна, а не просто массив). 
Будем в i-ой очереди хранить вершины, которые имеют какой-нибудь путь длиной i от стартовой.  
Кладем в очередь на i = 0 стартовую вершину.  
Бежим по массиву очередей:  
__Если очередь не пуста, попаем по порядку вершинки v:  
____Теперь, пользуясь списком смежности, обрабатываем всех соседей u вершинки v:  
______1) пробуем прорелаксировать расстояние до соседа в dist[u] и если получается, то  
______2) добавляем соседа в соответствующую очередь: mq[ dist[v] + расстояние до соседа ].  
Заметим, что в тот момент, когда мы в первый раз в очередях mq встречаем вершину, 
в dist уже лежит кратчайшее расстояние до нее (не может быть пути короче, 
который проходил бы через вершины расположенные правее, а вершины левее мы уже все обработали).  
Чтобы не перелопачивать соседей уже обработанных вершинок заново, попнув вершину, сверяемся с used.  
Улучшение по памяти. Обработанные очереди нас уже не интересуют, 
а заполненные очереди, которые надо будет обработать в дальнейшем, находятся не далее чем на k, от текущей очереди. 
Значит нам достаточно массива очередей размером k+1. 
Куда именно класть соседей, каждый раз будем определять делением по модулю на k + 1.  
Один рассказывал так, что пути не обязательно целые. По ячейкам распределяем в соответствии с округлением вниз. 
Расстояние минимум 1 гарантирует, что соседи окажутся в другой ячейке.  

Есть еще странный вариант 1-k BFS. Разобьем каждое ребро на единичные участки, введя кучу новых вершинок. 
Запускаем обычный BFS. O(V + kE).  

### Алгоритм Дейкстры
https://www.youtube.com/watch?v=fA_xvuqzuGs https://www.youtube.com/watch?v=J-7MzbEtTR0  
Граф без отрицательных ребер. Найти минимальные расстояния до всех вершин из исходной.  
Инициализируем массив расстояний бесконечностями. Расстояние от самой вершины до неё же - 0. 
Все вершины графа помечаются как необработанные.  
Шаг алгоритма:  
- Если все вершины обработаны, алгоритм завершается.
- В противном случае из ещё необработанных вершин выбирается вершина u, имеющая минимальное расстояние 
(на первом шаге это стартовая вершина). Для этого в C++ удобно использовать вместо очереди set из пар 
(расстояние, номер вершины). Не забывать обновлять расстояния и в этом множестве, а не только в массиве расстояний.
- Мы рассматриваем всех соседей вершины u. Для каждого соседа вершины u, кроме отмеченных как обработанные, 
рассмотрим новую длину пути, равную сумме значений текущей метки u и длины ребра, соединяющего u с этим соседом. 
Если полученное значение длины меньше значения метки соседа, заменим значение метки полученным значением длины. 
Рассмотрев всех соседей, пометим вершину u как обработанную и повторим шаг алгоритма.  

Используем очередь. Сложность обычного Дейкстры - O(V^2 + E), на множестве - O((V + E) * logV). Лучше? Да. 
Но если граф плотный E ~ V^2, алгоритм на множестве становится хуже: V^2 vs V^2 * logV.  

Восстановление путей. Можно создать массив p, в ячейках которого будет храниться родитель - 
вершина, из которой произошла последняя релаксация. 
Обновлять его можно параллельно с массивом dp. 

#### Мотоциклист
Пример задачи на BFS. Мотоциклист путешествует между городами с канистрой, равной по объему баку мотоцикла. 
На проезд между городами тратится один бак. В каждом городе своя цена бензина. Найти самый дешевый путь из A в B.  
Каждый город превращаем в три: U0, U1, U2 - по количеству имеющегося у мотоциклиста бензина. 
Из V1 мотоциклист попадает в U0, из V2 - в U1; делает это "бесплатно". 
А вот из U0 в U1 или из U1 в U2 - за соответствующую плату. 
Запускаем BFS на таком графе.

### Алгоритм Форда-Беллмана
https://www.youtube.com/watch?v=cE5n2IKf7W4  
Граф с возможностью отрицательных ребер (без отрицательных циклов?). Найти минимальные расстояния до всех вершин 
от стартовой.  
Инициализируем массив расстояний бесконечностями. Расстояние от самой вершины до неё же - 0.  
Пробегаемся по всем ребрам. Если расстояние до начальной вершины бесконечность, ничего не делаем. Если нет, 
то обновляем расстояние, если путь по данному ребру оказывается короче того, который уже записан для конечной вершины. 
dist[b] = min(dist[b], dist[a] + weight).  
Так делаем V - 1 раз: крайний случай, когда все вершинки расположены в одну линейную цепочку. 
На каждом шаге i гарантировано находим кратчайшее расстояние до вершин ранга i.  
Очень простой алгоритм: цикл в цикле - до V - 1 и обход по всем ребрам.  
Сложность большая - O(V*E).  
В большинстве случаев V - 1 прогонов - слишком много, большАя/бОльшая часть - в пустую.  
Можно завести флаг, чтобы брекнуться, если на предыдущей итерации цикла не было произведено ни одного изменения.  
А можно на первом шаге обновить расстояние только для соседей стартовой вершины. А на последующих шагах пытаться 
обновлять только соседей вершин, которые были обновлены на предыдущем шаге. Очередь нам в помощь. Это называют SPFA /
 алгоритм Мура / алгоритм Ф-Б с очередью.

### Алгоритм Флойда-Уоршелла
https://www.youtube.com/watch?v=kaA3_qNfpCA https://www.youtube.com/watch?v=8JQ565Rz7d8  
Граф с возможностью отрицательных ребер (без отрицательных циклов?). Построить матрицу минимальных расстояний между 
всеми вершинами.  
Динамическое программирование.  
Строим матрицу смежности d-1[i, j]. Если путей между двумя вершинами несколько, записываем кратчайшее расстояние. 
На главной диагонали - нули. Если есть отрицательные петли, то на главную диагональ записываем их 
(или минус бесконечность?). 
Если пути нет, записываем бесконечность.  
Теперь будем сравнивать имеющиеся пути с путем из i в 0, а потом из 0 в j. Где нашли путь короче, там заменяем, 
получая матрицу d0[i, j]. Далее повторяем с промежуточной вершиной 1 - получаем кратчайший путь из тех, которые идут 
прямо из i в j или через вершины 0 и 1. И т.д.  
Получается простейший алгоритм с тремя вложенными циклами: во внешнем перебираем промежуточные вершины, 
во внутренних - i и j.  

### Алгоритм Джонсона
https://www.youtube.com/watch?v=8JQ565Rz7d8  
Граф с возможностью отрицательных ребер (без отрицательных циклов?). Построить матрицу минимальных расстояний между 
всеми вершинами.  
Какой-то кентаврик. Без подробностей здесь записал.  
Запускается алгоритм Форда-Беллмана из всех вершин графа одновременно. Изменяем вес ребер по результатам ФБ, 
они становятся неотрицательными, кратчайшие пути (но не их значения) не изменяются. Теперь можно запускать Дейкстру из 
всех вершин. Корректируем расстояния, используя результаты ФБ.

### Задачи с отрицательными циклами
https://www.youtube.com/watch?v=LVnPNWwd-yo https://www.youtube.com/watch?v=LnOOuNcRLIo  

- Определить, есть ли в графе отрицательный цикл + 
- Вывести какой-то из отрицательных циклов +
- Вывести все отрицательные циклы (в общем случае) -
- Пометить вершины, до которых нет кратчайшего пути +
- Найти кратчайшие/длиннейшие простые пути (не содержащие циклов; в общем случае) - (np-полная?)

До некоторых вершин перестают существовать кратчайшие пути (они бесконечно большие).  
Алгоритмы Форда-Беллмана и Флойда-Уоршелла надо модифицировать, борясь с отрицательными переполнениями.


---

## Минимальное остовное дерево
Дан взвешенный связный неориентированный граф. 
Найти дерево минимального веса (минимальной суммы весов ребер), которое является подграфом данного графа. 
Такие деревья называют остовами (каркасами, скелетами).  
Свойства:
- Если веса всех рёбер различны, то остов будет уникален.  
- Минимальный остов является также и остовом с минимальным произведением весов рёбер 
(замените веса всех рёбер на их логарифмы);
- Минимальный остов является также и остовом с минимальным весом самого тяжелого ребра;

Если вы решаете задачу, где ребра не добавляются, а удаляются, и нужно поддерживать минимальный остов, 
то можно попробовать решать задачу «с конца» и применить алгоритм Крускала. 
То есть запомнить все запросы и потом выполнять их с конца, 
тогда команды на удаление ребер заменять на построение ребер.  

### Алгоритм Прима 
Похож на дейкстру. Но выбираем следующую вершину по весу соединяющего ребра вместо суммарного расстояния до неё.  
Вектор dist длиной V с расстояниями +бесконечность до остова. 
Вектор used длиной V с нулями. Добавляя вершину в остов отмечаем ее единичкой. 
Список смежности длиной E с парами {соседка, расстояние до нее}. 
Приоритетная очередь (С++шный set с парами {расстояние до остова, вершина}). Приоритетность по расстоянию до остова.  
Добавим в очередь любую вершину. Например, (0, 0). dist[0] = 0. 
Пока очередь не пуста выбираем вершину с минимальным расстоянием до остова. 
Если ребро не ведет в вершину, уже находящуюся в остове, добавляем ее в остов и добавляем в очередь ее соседок. 
Одновременно пытаемся релаксировать минимальное расстояние этих вершин до остова. Если расстояние уменьшилось, 
то нужно обновить dist, удалить из очереди предыдущую пару и пушнуть пару с обновленным расстоянием.  
По пути в зависимости от задания: выводим входящие в остов ребра, суммируем длину остова...  
Сложность в зависимости от реализации: 
- O(VE). Каждый раз перебираем все ребра;
- O(E^2). Очередь с линейным поиском оптимальной вершины;
- O(ElogV). Приоритетная очередь (set в c++).  

Как и в случае с дейкстрой при плотном графе (E ~ V^2) третье хуже второго.   

### Алгоритм Крускала
Жадник. 
Отсортируем рёбра и будем пытаться добавлять их в остов в порядке возрастания весов.
Если ребро соединяет какие-то две вершины внутри одной компоненты связности, то проигнорируем его. 
При этом образуется много компонент связности, иногда мы их соединяем.  
Наивная реализация - O(ElogE + V^2). 
Но если для двух упомянутых задач использовать систему непересекающихся множеств, 
то сложность -  O(ElogE). Она определяется сложностью сортировки ребер.

### Алгоритм Борувки
O(ElogV). Очень полезен на практике, потому что в «реальных» (планарных?) графах он работает за линейное время. 
Он легко параллелится.  
Алгоритм неприятно реализовывать.  
Шаги:
1) для каждой вершины найдем минимальное инцидентное (в/из него) ей ребро;
2) добавим все такие рёбра в остов и сожмем получившиеся компоненты, то есть объединим списки смежности вершин, 
которые эти рёбра соединяют;
3) повторяем шаги 1-2, пока в графе не останется только одна вершина-компонента.

Алгоритм может работать неправильно, если в графе есть ребра, равные по весу. 
Пример: «треугольник» с одинаковыми весами рёбер. 
Избежать это можно введя какой-то дополнительный порядок на рёбрах — например, сравнивая пары из веса и номера ребра.  

---

## Наименьший общий предок
https://ru.algorithmica.org/cs/trees/binary-lifting/  
http://www.e-maxx-ru.1gb.ru/algo/lca_simpler  
https://neerc.ifmo.ru/wiki/index.php?title=Метод_двоичного_подъёма  
LCA - least/lowest common ancestor.  
Для вершин u и v - это наиболее удалённая от корня дерева вершина, лежащая на обоих путях (от u и v) до корня
1. Самый простой, наивный алгоритм для нахождения наименьшего общего предка — 
вычислить глубину вершин u и v и постепенно подниматься из каждой вершины вверх по дереву, 
пока не будет найдена общая вершина. O(h);
2. Алгоритм двоичного подъема, требующий O(n log n) времени на препроцессинг и O(log n) времени на запрос.
На препроцессинге вычисляем для каждой вершины предка, удалённого от неё на расстояние 2^k для всех возможных k, 
и использовать эту информацию для ускорения наивного алгоритма;
3. Алгоритм Тарьяна за время O(n * α(n) + m), где m — число запросов, а α - функция Аккермана 
(только в одном месте нашел упоминание этого компонента в O). 
Это offline-алгоритм: все запросы должны быть доступны заранее. 
Во время обхода dfs строим систему непересекающихся множеств и, 
пользуясь последним, отвечаем на запросы для текущей вершины;
4. Алгоритм Бендера — Фараха-Колтона, требующий O(n) времени на препроцессинг и O(1) времени на запрос. 
Как-то используется то, что задача RMQ (поиск минимума на отрезке), к которой мы сводим задачу LCA, 
является специфичной: любые два соседних элемента в массиве отличаются ровно на единицу 
(поскольку элементы массива - это не что иное, как высоты вершин, посещаемых в порядке обхода). 
Сочетает в себе разбиение массива на блоки, использование разреженной таблицы (Sparse Table) 
и предобработку для небольших блоков. 
Абсолютно бесполезен на практике  
(из-за большой константы: слишком много чего нужно считать, чтобы избавиться от логарифма в асимптотике), 
однако очень интересен с теоретической точки зрения.  

### Алгоритм двоичного подъема
Предподсчитаем для каждой вершины предков, находящихся от нее на 2^i уровней. 
Максимальное значение i: l = округление_вверх(log_2 n). O(n*logn).  
Составим массив предков up размером n * l. 
up[v][i] - вершина-предок вершины v на расстоянии 2^i от нее (если такой нет, то корень). 
Массив заполнять можно динамически, пользуясь тем, что i-ый предок - это (i-1)-ый предок (i-1)-го предка: 
up[v][i] = up [ up[v][i-1] ] [i-1]. 
Предок корня - сам корень. 
Идем dfsом и заполняем массивы up, tin и tout.  
Для определения является ли какая-то вершина предком другой используем массивы tin и tout.  
Ищем предка вершин v и u. Перебираем предков вершины u, начиная с самого дальнего 
(это корень и это максимальный шаг) и, 
если этот предок общий для u и v, смотрим предка на шаг ближе в up (т.е. вдвое ближе, это половинный шаг). 
Если же он оказывается предком только для u, но не для v, то вместо u берем этого предка и 
продолжаем процесс с четвертного шага вверх.  
Сложность - O(logn), т.к. это фактически бинпоиск - ищем ответ на середине одной из половинок.  
Интересное замечание. 
Кеш на порядок быстрее озу. При запросе к ячейке в кеш подгружаются и соседние данные. 
Правильно сделать не массив up[v][l], но массив up[l][v]. Это в разы увеличит скорость заполнения up. 
В первом случае нам для вычисления up[v][i] нужен up [up[v][i-1]] [i-1], а он окажется где-то далеко - в озу. 
А во втором: up[i][v] <- up [i-1] [up[v][i-1]], а он где-то рядом и, значит, есть вероятность, 
что его система в кеш подгрузила вместе с нашими данными.  

### Запросы на путях
Пусть нас вместо LCA спрашивают, например, о минимуме на произвольном пути (на всех рёбрах записаны какие-то числа). 
Аналогичным образом можно считать сумму, gcd, полиномиальный хеш и много других странных функций на пути, 
но только в статическом случае — когда у нас нет обновлений.  
Во время предподсчета, как в методе двоичных подъемов, сохраняем вместе с номером 2^i-ого предка 
минимум на соответствующем пути. 
Минимум на пути от u до v — это минимум от (минимума на пути от u до lca(u, v) ; и минимума на пути от v до lca(u, v). 
В свою очередь, оба этих минимума — это минимум на всех двоичных подъемах до LCA.  

---

### Гамильтонов путь
Гамильтонов путь проходит через каждую вершину графа ровно один раз. 
Гамильтонов цикл - замкнутый гамильтонов путь. 
Задача о коммивояжере. Гамильтонов цикл с наименьшей общей длиной пути. 
Это NP-полные задачи.  
Часто решают через динамическое программирование по подмножествам (по маскам). 
https://ru.wikipedia.org/wiki/Задача_о_гамильтоновом_пути  
https://neerc.ifmo.ru/wiki/index.php?title=Гамильтоновы_графы  
https://foxford.ru/wiki/informatika/postroenie-gamiltonova-tsikla?utm_referrer=https%3A%2F%2Fyandex.ru%2F  

### Паросочетания
не очень разобрался
https://algorithmica.org/ru/matching  
https://neerc.ifmo.ru/wiki/index.php?title=Паросочетания:_основные_определения,_теорема_о_максимальном_паросочетании_и_дополняющих_цепях  
http://www.e-maxx-ru.1gb.ru/algo/kuhn_matching  
Паросочетание — произвольное множество рёбер двудольного графа такое, что никакие два ребра не имеют общей вершин.  
Вообще, паросочетания можно искать в любых графах, однако этот алгоритм неприятно кодить, и он работает за O(n^3).  
Чередующаяся цепь - цепь, в которой рёбра поочередно принадлежат/не принадлежат паросочетанию. 
Увеличивающая цепь - чередующаяся цепь, у которой начальная и конечная вершины не принадлежат паросочетанию. 
Можно с помощью увеличивающей цепи увеличивать паросочетание на единицу. 
Можно взять такой путь и провести чередование: рёбра, которые не входили в паросочетание 
(первое, третье и т.д. до последнего) включим в паросочетание, а рёбра, которые раньше входили в паросочетание 
(второе, четвёртое и т.д. до предпоследнего) — удалим из него. 
Мощность паросочетания при этом увеличилась на единицу (потому что было добавлено на одно ребро больше, чем удалено) - 
удалим из него.  
Задача нахождения максимального паросочетания. Алгоритм Куна. 
Будем искать увеличивающую цепь dfsом или bfsом, пока ищется, и проводить чередование в ней. 
Как только увеличивающую цепь найти не удалось — процесс останавливаем, — текущее паросочетание и есть максимальное. 
Сложность: O(nm), что в худшем случае есть O (n^3).  

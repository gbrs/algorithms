/*
Дан массив чиел длиной до 150 000.
Массовые операции (до 150 000 штук): добавить ко всем числам на отрезке или найти сумму на отрезке.
Числа до 10^8 по модулю.
*/

/*
Реализуем ленивый вариант: не спускаем изменения до листьев каждый раз - можем остановиться в узлах вышестоящих
(см. в теории).
В этом коде относительно редкий вариант?
Перед каждым шагом вниз проталкиваем несогласованности вниз,
пересчитываем истинное значение в детях, "обнуляем" несогласованность в родителе.
В других решениях чаще, кажется, пересчет значений делается только при запросе значения
*/

#include <iostream>
#include <vector>

using namespace std;

const long long N = 150000 + 7;
const long long NO_OPERATION = 0;
vector <long long> input(    N, NO_OPERATION);  // вектор исходных данных
vector <long long>  tree(4 * N, NO_OPERATION);  // дерево отрезков
vector <long long> shift(4 * N, NO_OPERATION);  // вектор несогласованных модификаций
// в данном коде несогласованность - это несогласованность с детьми,
// сами значения для детей в tree мы пересчитываем сразу после проталкивания и они "согласованны"


void build_tree(long long vertex, long long tl, long long tr) {
    /* строим изначальное дерево */

    if (tl == tr) {
        // листья
        tree[vertex] = input[tl];
    } else {
        // рекурсивно строим дерево
        long long tm = (tl + tr) / 2;
        build_tree(vertex * 2,         tl, tm);
        build_tree(vertex * 2 + 1, tm + 1, tr);
        tree[vertex] = tree[vertex * 2]
                     + tree[vertex * 2 + 1];
    }
}


void push(long long vertex, long long tl, long long tr) {
    /* проталкиваем несогласованные модификации вниз */

    if (shift[vertex] == NO_OPERATION) return;

    // если мы не в листе
    if (tr - tl != 0) {
        // вниз проталкиваем несогласованность - в детей.
        // Если там уже была несогласованность, то надо добавить к ней.
        shift[vertex * 2]     += shift[vertex];
        shift[vertex * 2 + 1] += shift[vertex];

        // пересчитываем в детях значения tree
        long long tm = (tl + tr) / 2;
        tree[vertex * 2]     += (tm - tl + 1) * shift[vertex];
        tree[vertex * 2 + 1] += (tr - tm)     * shift[vertex];

        // несогласованности с детьми в родителе теперь нет
        shift[vertex] = NO_OPERATION;
        return;
    }
}


void add(long long l, long long r, long long val, long long vertex, long long tl, long long tr) {
    /* update на отрезке */

    // поддерево вне интервала. Ничего не делаем
    if (tr < l || r < tl) {
        return;
    }

    // поддерево внутри интервала модификации. Изменяем сумму в tree и запоминаем несогласованность
    if (l <= tl && tr <= r) {
        tree[vertex]  += val * (tr - tl + 1);
        shift[vertex] += val;
        return;
    }

    // поддерево пересекается с интервалом частично.
    push(vertex, tl, tr);  // перед каждым шагом вниз проталкиваем несогласованности вниз
    // шагаем в левого сына, потом в правого
    long long tm = (tl + tr) / 2;
    add(l, r, val, vertex * 2,         tl, tm);
    add(l, r, val, vertex * 2 + 1, tm + 1, tr);
    // считаем значение в вершине после того, как сыновей отработали
    tree[vertex] = tree[vertex * 2]
                 + tree[vertex * 2 + 1];
}


long long get_sum(long long l, long long r, long long vertex, long long tl, long long tr) {
    /* получаем сумму на отрезке */

    // поддерево вне интервала
    if (tr < l || r < tl) {
        return NO_OPERATION;
    }

    // поддерево внутри интервала модификации
    if (l <= tl && tr <= r) {
        return tree[vertex];
    }

    // поддерево пересекается с интервалом частично
    push(vertex, tl, tr);    // перед каждым шагом вниз проталкиваем несогласованности вниз
    long long tm = (tl + tr) / 2;
    return get_sum(l, r, vertex * 2,         tl, tm)
         + get_sum(l, r, vertex * 2 + 1, tm + 1, tr);
}


void print(vector <long long> & vec) {
    /* печать массивов для дебага */

    for (auto i: vec) {
        cout << i << ' ';
    }
    cout << '\n';
}


int main() {
    long long n, a, b, c, m;
    string str;

    // строим дерево
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> input[i];
    }
    build_tree(1, 0, n - 1);
    // print(tree);
    // print(shift);
    // cout << '\n';

    // исполняем запросы
    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> str >> a >> b;
        if (str == "add") {
            cin >> c;
            add(a - 1, b - 1, c, 1, 0, n - 1);
            // print(tree);
            // print(shift);
            // cout << '\n';
        } else {
            cout << get_sum(a - 1, b - 1, 1, 0, n - 1) << '\n';
            // print(tree);
            // print(shift);
            // cout << '\n';
        }
    }
}

/*
10
1 4 -6 5 2 -6 5 7 -1 1
11
add 1 4 -2
add 2 4 -4
sum 4 10
sum 7 9
add 6 10 -2
sum 1 6
add 1 9 -6
add 7 8 0
add 4 4 6
add 1 3 5
sum 1 10

10
1 4 -6 5 2 -6 5 7 -1 1
15
add 1 4 -2
add 2 4 -4
sum 4 10
sum 7 9
add 6 10 -2
sum 1 6
sum 1 10
add 1 9 -6
sum 1 10
add 7 8 0
sum 1 10
add 4 4 6
sum 1 10
add 1 3 5
sum 1 10

*/

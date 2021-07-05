'''
классическая ханойская башня с 3 стержнями.
Стержни: 1, 2, 3. Диски: 1, 2 ... n; в порядке возрастания размера.
'''


'''
Как переместить 10 дисков с первого стержня на второй? Очень просто: перемести (10 - 1) дисков на третий 
стержень, переложи нижний диск с первого стержня на второй, и потом перенеси 9 дисков с третьего стержня 
на второй.
А как 9 дисков переместить? Точно так же. Поменяются только стартовый и целевой стержни.
Задача свелась к рекурсии. Тривиальный случай - башня из одного диска. 
'''

'''
Стержней у нас три: 1, 2, 3. Их сумма - инвариант. А значит, зная стартовый и финишный стержни, мы всегда 
можем найти номер третьего стержня: 6 - start_pin - destination_pin. 
'''


def move_tower(tower_height, start_pin, destination_pin):
    if tower_height == 1:
        print(f'Move disk1 from pin{start_pin} to pin{destination_pin}')
    else:
        third_pin = 6 - start_pin - destination_pin
        move_tower(tower_height - 1, start_pin, third_pin)
        print(f'Move disk{tower_height} from pin{start_pin} to pin{destination_pin}')
        move_tower(tower_height - 1, third_pin, destination_pin)


move_tower(3, 3, 1)


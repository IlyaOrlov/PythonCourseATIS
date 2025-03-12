class Tank:
    x = 0
    y = 0
    color = 0
    speed = 1

    def Move (self, direction):
        if direction == "up" and y < 20:
            y = y - speed
        if direction == "right" and x < 20:
            x = x - speed
        if direction == "down" and y > 0:
            y = y + speed
        if direction == "left" and x > 0:
            x = x + speed
        print(f"Moving to (x).(y)")

    def Shoot(self):
        print("shooting")


class Map:
    # Массив ячеек
    width = 20
    length = 20


class Cell:
    wall = 0
'''
Поле состоит из клеток
Клетка либо пуста, либо содержит препятствие
'''


class Shot:
    direction # выстрел имеет направление
    distance # дистанция, которую он преодолевает
    color
    speed
    coordinate

    def Move(self):

    def Hit(self): # Выстрел поразил цель или нет
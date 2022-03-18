# 1.
# Написать функцию-фабрику танков.
# Принимает {тип: количество танков}: {T34: 5, Tiger: 10}
# Возвращает отсортированный по мощи (power) список танков.

# 2.
# + принимает значения скорости (speed), мощи (power) и начальной координаты (x).
# + Устанавливает переданные значения для всех танков.
import tanks


def fabric(d):
    t_common = []
    for k, v in d.items():
        t_common += [k() for _ in range(v)]
    return sorted(t_common)


def setup(lst_tanks, params):
    for j in lst_tanks:
        j._speed = params[0]
        j._power = params[1]
        j._x = params[2]
    return True


lst = fabric({tanks.Tiger: 2, tanks.T34: 4})
for i in lst:
    print(i._speed, i._power, i._x)

setup(lst, [35, 45, 5])
for i in lst:
    print(i._speed, i._power, i._x)

# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).


def my_func():
    x = int(input('Введите первое положительное число: '))
    y = int(input('Введите второе отрицательное число: '))
    if y == 0:
        return 1
    else:
        return 1 / x ** abs(y)


print(my_func())

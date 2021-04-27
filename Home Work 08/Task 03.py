# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.


class OwnErrorNotNumeric(Exception):
    def __init__(self, txt):
        self.txt = txt


numbers = []
s = ""
while s != 'stop':
    s = input("Введите ряд чисел и букв, по окончании ввода слово stop: ")
    for x in s.split():
        if x == 'stop':
            s = 'stop'
            break
        try:
            x_test = x
            if x_test[0] == "-":
                x_test = x_test[1:]
            pos = x_test.find(".")
            if pos != -1 and pos != len(x_test)-1:
                x_test = x_test[:pos] + x_test[pos+1:]
            if not x_test.isnumeric():
                raise OwnErrorNotNumeric(f"{x} - не число!")
        except OwnErrorNotNumeric as err:
            print(err)
        else:
            numbers.append(x)

print("Введенный список: ", numbers)

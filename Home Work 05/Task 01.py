# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


with open('test.txt', 'w+') as file_object:
    while True:
        string = input('Введите текст, для перехода на новую строчку используйте ENTER: ')
        if string:
            print(string, file=file_object)
        else:
            print('Ввод закончен')
            break

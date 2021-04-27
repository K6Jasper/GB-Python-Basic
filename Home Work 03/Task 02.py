# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

city = input('Введите город: ')
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождение: ')
telephone = input('Введите телефон: ')
email = input('Введите e-mail: ')


def student(_name, _surname, _year, _telephone, _email, _city):
    return ' '.join([name, surname, year, telephone, email, city])


print(student(name, surname, year, telephone, email, city))

# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


firm = {'Иванов': 29500, 'Медведев': 19500, 'Сечин': 11000, 'Громыко': 20500}
try:
    file_obj = open('task3.txt', 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print('Произошла ошибка ввода-вывода!')
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open('task3.txt', 'r') as file_obj:
    for line in file_obj:
        print(line, end='')
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f'Сотрудник получающий меньше 20000р.: {persons}')
print(f'Средняя з.п.: {result}')

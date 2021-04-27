# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


# my_list = open("task2.txt")
# cnt = 1
# for line in my_list:
#     print(f"Строка {cnt} содержит {len(line.split())} слово")
#     cnt += 1
# my_list.close()

my_file = open('task2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('task2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('task2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('task2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

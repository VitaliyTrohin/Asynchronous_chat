"""
6. Создать текстовый файл test_file.txt,
заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

from chardet import detect

with open('test_file.txt', encoding='utf-8') as file:
    for el in file.read():
        print(el)

file = open('test_file.txt', 'rb')
for el in file:
    print(el.decode(encoding='utf-8'))

"""2. Каждое из слов «class», «function», «method» записать в байтовом типе
без преобразования в последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных."""

word_1 = b'class'
word_2 = b'function'
word_3 = b'method'

words = [word_1, word_2, word_3]

for el in words:
    print(f'класс: {type(el)}\nсодержимое: {el}\nдлина: {len(el)}\n')

"""3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе."""

word_1 = 'attribute'
word_2 = 'класс'
word_3 = 'функция'
word_4 = 'type'

words = [word_1, word_2, word_3, word_4]

for el in words:
    try:
        print(bytes(el, 'ascii'))
    except UnicodeEncodeError:
        print(f'"{el}" - невозможно записать в байтовом типе')

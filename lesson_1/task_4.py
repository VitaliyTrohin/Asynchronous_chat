"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'

words = [word_1, word_2, word_3, word_4]

words_b = []
for el in words:
    el_b = el.encode('utf-8')
    words_b.append(el_b)
    print(el_b)

print()

for el in words_b:
    el_str = el.decode('utf-8')
    print(el_str)

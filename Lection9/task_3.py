# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
from pathlib import Path
text_new = ''
path = Path('C:\\development\\pythonProject\\Lection9\\test_file\\task_3.txt')

file = open(path, mode='r', encoding='utf-8')
# print(file.readlines())
for line in file.readlines():
    for symbol in line:
        if symbol.isdigit() == True:
            text_new += symbol
    text_new += '\n'
print(text_new)

# assert three_most_expensive_purchases == 202346

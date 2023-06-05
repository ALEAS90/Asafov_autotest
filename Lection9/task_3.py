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
# print(text_new)

list = []
for file.readlines():
    list.append(file.readlines())
print(list)

for _ in range(3):
    key_max = None
    int_value = int(value)
    value_max = 0
    summ = 0
    for int_value in text_new:
        if int_value > value_max:
            key_max = key
            value_max = value
    summ += value_max


assert three_most_expensive_purchases == 202346

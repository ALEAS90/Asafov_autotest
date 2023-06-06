# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
from pathlib import Path
text_new = ''
path = Path('C:\\development\\pythonProject\\Lection9\\test_file\\task_3.txt')
sum_purches = 0
counter = 0
temp = None
list_purch = []
file = open(path, mode='r', encoding='utf-8')
three_most_expensive_purchases = []


for line in file.readlines():
    temp = line.strip()
    if not temp:
        list_purch.append(sum_purches)
        sum_purches = 0
    else:
        temp = int(temp)
        sum_purches += temp

list_purch.sort(reverse=True)
list_max = list_purch[0:3]
three_most_expensive_purchases = sum(list_max)
print(three_most_expensive_purchases)



assert three_most_expensive_purchases == 202346

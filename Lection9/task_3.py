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
# path_summ = Path('C://development//pythonProject//Lection9//summ.txt')
# file_summ = open(path_summ, mode='w', encoding='utf-8')
# file_summ.write(text_new)
# # file_summ.close()
# print(file_summ.readlines())
# # print(path_summ.readlines())
#
# for i in range(3):
#     for value in file_summ.readlines():
#         if value.isdigit() == True:
#             print(value)
#
#
# #
# # list = [text_new.split('\n')]
# # print(list)
#
# # for val in text_new:
#


# for _ in range(3):
#     key_max = None
#     value_max = 0
#     summ = 0
#     for value in list:
#         if value.isdigit() == True:
#             print(value)
#     #     if int(value) > value_max and value != '':
#     #         value_max = int(value)
#     # summ += value_max
#     # print(summ)


# assert three_most_expensive_purchases == 202346

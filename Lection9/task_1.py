# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

from pathlib import Path

path = Path('C:/development/pythonProject/Lection9/test_file/task1_data.txt')
print((path.is_file()))
file = open(path, mode='r', encoding='utf-8')
for i in file.readlines():
    print(i)




# print(path)
# print(Path.readlines(path))


#
#
# def delete_nums(path):
#     print(path.readlines())
#     return delete_nums()
# delete_nums(path)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


# with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
#     with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
#         answer = file1.readlines()
#         ethalon = file2.readlines()
#         assert answer == ethalon, "Файл ответа не совпадает с эталонном"
# print('Всё ок')

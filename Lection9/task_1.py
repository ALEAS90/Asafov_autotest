# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

from pathlib import Path

path = Path('C:/development/pythonProject/Lection9/test_file/task1_data.txt')
# print((path.is_file()))
file = open(path, mode='r', encoding='utf-8')
# print(file.read())
line = ''
text_new = ''

for line in file.readlines():
    for symbol in line:
        if symbol.isdigit() == False:
            text_new += symbol
print(text_new)

path_answer = Path('C:/development/pythonProject/Lection9/test_file/task1_answer.txt')
file_answer = open(path_answer, mode='w', encoding='utf-8')
file_answer.write(text_new)
print(file_answer)
file_answer.close()


# # Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')

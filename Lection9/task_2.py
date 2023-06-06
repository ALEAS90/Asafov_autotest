# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
from pathlib import Path

file_log = 'log.txt'


def func_log(test):  # декоратор
    def wrapper():
        path = Path('C:\development\pythonProject\Lection9\log.txt')
        file_log = open(path, mode='w', encoding='utf-8')
        dt = datetime.datetime.now()
        format = '%d.%m %H:%M:%S'
        datetime.datetime.strptime(dt, format)
        file_log.write(function.__name__ + 'вызвана' + )




        print(date1)
        # """Вызвали исходную функцию"""
        function()
        """Доработали функцию новым функционалом записи в файл"""

        print(file_log.readlines())
        file_log.write(str(func_log.__name__()) + "вызвана" + str(date1))
        print(file_log)
        file_log.close()
    return wrapper




def function():  # функция, которую декорируем




# f = func_log(function)
# f()





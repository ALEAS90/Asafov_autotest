# Игра "Эрудит"
# Нужно написать программу scrabble, которая помогает считать кол-во очков (points), полученное за слово (word)
# По одному очку вы получите за буквы а, в, е=ё, и, н, о, р, с, т.
# Два очка стоит д, к, л, м, п, у.
# Три балла получают за б, г, ь, а также я.
# Четыре балла стоят буквы й, ы.
# 5 очков засчитывается за ж, з, х, ц, ч.
# 6 и 7 очков не предусмотрено.
# Восемь можно получить за букву ф, ш, э, ю.
# 10 баллов стоит буква щ,
# а 15 - ъ
# Например (Ввод --> Вывод):
# курс --> 6 (к=2, у=2, р=1, с=1)


def scrabble(word): #курс   к
    values_dct = []
    keyss = []
    values = 0
    points = []
    dct = {
         1: 'авеёинорст', 2: 'дклмпу', 3: 'бгьая', 4: 'йы', 5: 'жзхцч', 8: 'фшэю', 10: 'щ', 15: 'ъ'}
    print(dct.items())
    for i in word:
        if i in dct.values():
            print(i)

    # for i in word:
    #     if i in dct.values():
    #     values_dct += dct.items()
    #        values += dct.keys()
    #     print(values)
        # print(values_dct)
    #     print(values_dct)
    #      if i in dct.values()
    #     in dct.values():
    #     if words in key.split():
    #         points.append(dct.values())
    # print(points)


    # point = ()
    # for key in word:
    #     if word in dct.keys[]:
    #         points += dct.values()
    #     print(points)
    #         # return dct.get(key)

        # points = (sum(map(scrabble, input())))
    return points

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = ["курс", 'авеинорстё', 'дклмпеу', 'бгья', 'йы', 'жзхцч', 'фшэю', 'щъ', "карабасбарабас", "околоводопроводного",
        "еженедельное", 'эхоэнцефалограф', 'человеконенавистничество', 'делопроизводительница']

test_data = [6, 10, 13, 12, 8, 25, 32, 25, 21, 26, 20, 54, 34, 36]

for i, d in enumerate(data):
    assert scrabble(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')

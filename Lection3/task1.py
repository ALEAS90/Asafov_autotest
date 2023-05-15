# Напишите функцию modification(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

def modification(lst):
    """старый вариант решения"""
    # print(lst)
    # new_lst = []
    # new_lst.append(lst[-1])
    # for i in lst[1:-1]:
    #     new_lst.append(i)
    # new_lst.append(lst[0])
    # print(new_lst)

    """новый вариант решения после доработки"""
    lst.insert(0,lst[-1])
    lst.append(lst[1])
    lst.pop(1)
    lst.pop(-2)
    # lst.pop(1)
    print(lst)
    new_lst = lst

    return new_lst

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    ['н', 'л', 'о', 'с']
]

test_data = [
    [3, 2, 1], [5, 2, 3, 4, 1], ['с', 'л', 'о', 'н']
]


for i, d in enumerate(data):
    assert modification(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')

# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    a = list(str(num))
    print(a)
    sum = 0
    for i in a:
        sum += int(i)  #sum = sum + int(i)
        print(sum)
    t = 0
    if sum % 3 != 0:
        t = 3 - sum % 3
        print(t)


    for count, i in enumerate(a):
        if (t > 0) and (int(i) < 9) and (int(i) > 6):
            a[count] = int(a[count]) + t
            break
        elif int(i) < 1:
            a[count] = int(a[count]) + t + 9
            break
        elif int(i) < 3:
            a[count] = int(a[count]) + t + 6
            break
        elif int(i) < 7:
            a[count] = int(a[count]) + t + 3
            break
    new_num = ''
    for i in a:
        new_num = new_num + str(i)
    print(new_num)
    return int(new_num)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')

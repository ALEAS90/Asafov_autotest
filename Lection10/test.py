# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random

alpha = ('a','b','c','d','e','f','g')
# random.randrange(start, stop, step)
#возвращает случайно выбранное число из последовательности.
random.choice # лучайны элемент непустой последовательности

first_word = random.choice(alpha)
second_word = random.choice(alpha)



def generate_random_name(alpha):
    f_w = ''
    s_w = ''
    for i in range(random.randrange(1, 15, 1)):
        f_w += random.choice(alpha)
    for i in range(random.randrange(1, 15, 1)):
        s_w += random.choice(alpha)
    # print(f_w, s_w)
    yield str(f_w) + " " + str(s_w)

# f_w = ''
# s_w = ''

    # yield s_w


gen = generate_random_name(alpha)
gen
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы класса:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (-4, -5)).y_axis_intersection() --> False

class Segment:

    def __init__(self, dot1, dot2):
        self.dot1_x = dot1[0]  # Координата x первой точки
        self.dot1_y = dot1[1]  # Координата y первой точки
        self.dot2_x = dot2[0]  # Координата x второй точки
        self.dot2_y = dot2[1]  # Координата y второй точки

    def length(self):
        length_seg = (((self.dot2_x - self.dot1_x) ** 2) + ((self.dot2_y - self.dot1_y) ** 2)) ** 0.5
        return round(length_seg, 2)

    def x_axis_intersection(self):

        if self.dot1_x <= 0 <= self.dot2_x or self.dot1_x >= 0 >= self.dot2_x:
            return True
        else:
            return False

    def y_axis_intersection(self):

        if self.dot1_y <= 0 <= self.dot2_y or self.dot1_y >= 0 >= self.dot2_y:
            return True
        else:
            return False

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')

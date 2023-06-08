import pytest
import datetime

@pytest.fixture() # Таким образом функция будет восприниматься как фикстура
def time_start():
    time_start_1 = datetime.datetime.now()  # текущее время
    # date_correct = time_start_1.strftime('%d.%m %H:%M:%S')  # текущее время по маске
    # print(date_correct)
    yield time_start_1
    print('Время выполнения: ', datetime.datetime.now() - time_start_1)


@pytest.fixture(scope='class')
def for_class_fixt():
    time_start_1 = datetime.datetime.now()  # текущее время
    # date_correct = time_start_1.strftime('%d.%m %H:%M:%S')  # текущее время по маске
    # print(date_correct)
    yield time_start_1

    print('\n', 'Время выполнения класса: ', datetime.datetime.now() - time_start_1)



# Функция создает красивый разделитель из 10-и звездочек
def simple_separator():
    '''
    :return: строка разделитель
    '''
    return '**********'


# Функция создает разделитель из звездочек число которых можно регулировать параметром count
def long_separator(count):
    '''
    :param count: количество звездочек в строке
    :return: строка разделитель
    '''
    return '*' * count


# Функция создает разделитель из любых символов любого количества
def separator(symbol, count):
    """
    :param symbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель
    """
    return symbol * count


# Функция печатает Hello World в формате:
#     **********
#     Hello World!
#     ##########
def hello_world():
    """
    :return: None
    """
    print('**********\nHello World!\n##########')


# Функция печатает приветствие в красивом формате
# **********
# Hello {who}!
# ##########
def hello_who(who='World'):
    """
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    print(f'Hello {who}')


# Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
def how_many(power, *args):
    """
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления
    """
    args_sum = 0

    for i in args:
        args_sum += i

    args_power = args_sum ** power

    return args_power


# Функция выводит переданные параметры в фиде key --> value
# key - имя параметра
# value - значение параметра
def print_key_val(**kwargs):
    """
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for key, value in kwargs.items():
        print(f"{key}--> {value}")


# Функция фильтрует последовательность iterable и возвращает новую
# Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность
def my_filter(iterable, function):
    '''
    :param iterable: последовательность
    :param function: функция, фильтрующая последовательность
    :return: новая, отфильтрованная последовательность
    '''
    list_01 = []

    for i in iterable:
        if function(i) is True:
            list_01.append(i)
    return list_01

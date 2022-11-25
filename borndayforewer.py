correct_year = 1799
correct_day = '10.06'


def year():
    '''
    Спрашивает у пользователя год рождения Пушкина
    :return: ответ пользователя
    '''
    attempt_year = input('В каком году родился Пушкин?\n')
    return attempt_year


if int(year()) == correct_year:
    attempt_day = input('день и месяц рождения Пушкина в формате 01.01\n')
    if attempt_day == correct_day:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')

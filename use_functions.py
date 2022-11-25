def donate(balance):
    '''
    Позволяет увеличить сумму на счету
    :param balance: баланс до пополнения
    :return: баланс после пополнения
    '''
    deposit = int(input('введите сумму пополнения\n'))
    balance = balance + deposit
    return balance


def buy(balance, purchase_dict):
    '''
    Позволяет сделать покупку и сохранить ее название и цену
    :param balance: баланс до покупки
    :return: баланс после покупки и список покупок
    '''
    price = int(input('введите сумму покупки\n'))
    if balance >= price:
        balance = balance - price
        purchase = input('введите название покупки\n')
        purchase_dict[purchase] = price
    else:
        print('у вас не хватает денег\n')
    return balance, purchase_dict


def buy_dict(purchase_dict):
    '''
    Выводит в терминал список покупок
    :param dict_pur: список покупок
    '''
    print(purchase_dict)
    pass


# Сумма на счету
balance = 0
# Список покупок
purchase_dict = {}

while True:
    print('')
    print(f'у вас на счету сейчас {balance} рублей')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню\n')
    if choice == '1':
        balance = donate(balance)
    elif choice == '2':
        balance, purchase_dict = buy(balance, purchase_dict)
    elif choice == '3':
        buy_dict(purchase_dict)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')

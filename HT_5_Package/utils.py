"""Напишите программу считающую сдачу при покупке товара.
Номинал существующих купюр и монет соответствует принятым в России и хранится в коде программы в виде set: 5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01
На вход ваша программа принимает стоимость товара и купюры/монеты которыми платит покупатель через пробел.
Например:
Введите стоимость товара: 9800
Введите купюры внесенные в кассу: 5000 5000 (или 5000 1000 1000 1000 1000 и т.д.)
Результатом действия программы должен стать ответ содержащий количество и номинал сдачи: 100 100
Ответ должен вернуться максимально крупными купюрами, то есть минимальным количеством купюр, так как если бы это делал человек.
Ответ типа 50 50 50 50 или 5 5 5 5 5 5 5 5 5 5 5... и т.д. будет считаться неверным.
Требования к программе:
1. Все функции используемые в коде должны находиться в файле utils.py являющимся Package
2. Файл utils должен содержать в коде блок name == "__main__"
3. Исполнение и запуск самой программы должны происходить из файла main.py с соответствующими импортами функций из utils.
4. Напишите минимум 5 unit тестов. Используйте хотя бы в 2 из них конструкцию raise и pytest.
"""
def cash_register(banknotes,price):
    set = {5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01}
    price=round(price,2)
    banknotes_for_short_change = []
    paid = sum(banknotes)
    paid=round(paid,2)
    short_change = paid - price
    if paid < price:
        raise ValueError("Сумма купюр меньше стоимости")
    elif price == 0:
        raise ValueError("Цена не может быть равна 0")
    while short_change != 0:
        for i in range(len(set)):
            if short_change - max(set) >= 0:
                short_change = short_change-max(set)
                short_change = round(short_change, 2)
                banknotes_for_short_change.append(max(set))
            elif short_change - max(set) < 0:
                set.discard(max(set))
    return banknotes_for_short_change


if __name__ == "__main__":
    price1 = float(input("Введите стоимость товара:"))
    banknotes1 = input("Введите купюры внесенные в кассу:")
    banknotes1 = banknotes1.split()
    banknotes1 = [float(i) for i in banknotes1]
    print(cash_register(banknotes1, price1))
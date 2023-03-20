from utils import cash_register



price1 = float(input("Введите стоимость товара:"))
banknotes1 = input("Введите купюры внесенные в кассу:")
banknotes1 = banknotes1.split()
banknotes1 = [float(i) for i in banknotes1]
print(cash_register(banknotes1, price1))

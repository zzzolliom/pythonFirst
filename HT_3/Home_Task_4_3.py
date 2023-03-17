income_elem=input("Введите через пробел любые элементы")
income_elem=income_elem.split()
income_elem.sort()
print(income_elem)
def uniq_elem(lst):
    lst=set(lst)
    count_uniq=len(lst)
    print("Количество уникальных элементов=", count_uniq)

uniq_elem(income_elem)


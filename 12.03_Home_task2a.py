name_months = {1: 'jan', 2: 'feb', 3: 'march', 4: 'april', 5: 'may', 6: 'jun', 7: 'jul', 8: 'aug', 9: 'sep', 10: 'okt', 11: 'nov', 12: 'dec'}
year=int(input("Введите год для проверки:"))
n=int(input("Введите номер месяца"))
if(year%4==0 and year%100!= 0 or year%400==0):
    quantity_days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31,6: 30, 7: 31, 8: 31, 9: 30, 10: 31,11: 30, 12: 31}
    print(name_months[n], quantity_days_in_month[n])

else:
    quantity_days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,6: 30, 7: 31, 8: 31, 9: 30, 10: 31,11: 30, 12: 31}
    print(name_months[n], quantity_days_in_month[n],'days')



#1. Напишите программу, считывающую одно число N - номер месяца, и выводящую, сколько в  этом месяце дней и его название. (используйте словари)


#если не вводить год, то февраль всегда будет 28

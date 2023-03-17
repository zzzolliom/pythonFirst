"""
размер вклада=n
срок вклада=m
процент =10%
"""

"""def big_money(n,m,lst[])
    n=n*0.01+n
    return 1 if m==0 else big_money(n,m-1)
    lst.append(n)
    return lst
print(big_money())"""

deposit = int(input("Введите сумму"))
percent = float(input("Введите процент в формате 0.1"))
yeahrs=int(input("Введите срок вклада в годах"))


def big_money (n,p,m):
    internal_deposit=n
    for month in range(m):
        income = n * p
        internal_deposit += income
    return deposit
print(big_money(deposit, percent, yeahrs))


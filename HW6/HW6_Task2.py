"""Напишите программу принимающую на вход список [1,2,3] и выводящую все возможные комбинации его членов.:
Ответ: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)"""

"""def permutation(lst):
    l=[]
    for i in range(len(lst)):
        m = lst[i]
        print(m)
        rem_lst=lst[i:]+lst[i+1:]
        #[i:]- создает срез списка начиная с элемента с индексом i и до конца
        #[i+1:] - создает срез списка с элемента с индексом i+1 и до конца
        print(rem_lst)
        for p in permutation(rem_lst):
            l.append([m]+p)
    return(l)
data = list('123')

for p in permutation(data):

    print (p)"""


# Python function to print permutations of a given list

def permutation(lst):

    if len(lst) == 0:
        return []

    if len(lst) == 1:
       return [lst]

    l = []
    for i in range(len(lst)):
        m = lst[i]
        print("m=", m)
        remLst = lst[:i] + lst[i + 1:]
        print("remlst=",remLst)

        for p in permutation(remLst):
            l.append([m] + p)
            print("[m]=",[m])
            print("p=",p)
            print(l)
    return l

data = list('345')

for p in permutation(data):
    print(p)
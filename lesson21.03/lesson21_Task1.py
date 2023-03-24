"""
для
"""

"""a="3"
b=int(a)
c= a*b
print(c)"""

"""n = int(input('Введите число: '))
list = []
for i in range(n):
    print(i)
    for x in range(i):
        list.append(i)
        print(list)
list_result = []
for y in range(n):
    list_result.append(list[y])

print(list)
print(list_result)"""
n = int(input('Введите число: '))
v=[]
for i in range(1, n+1):
    v += [str(i)] * i

print(" ".join(v[:n]))
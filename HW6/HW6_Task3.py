#Изучите функцию permutations из itertools. Напишите программу выводящую все возможные варианты для списка [1,2,3]

from itertools import permutations

lst = [1, 2, 3, 4, 5]
permutations = permutations(lst)
for i in permutations:
    print(i)

# дан список чисел, определите сколько в этом списке элементов , которые больше двух соседей и выведите кол-во таких элементов.Крайние элементы никогда не учитываются
input_string = input("введите через пробел не менее 2 любых значений")
input_values = input_string.split()
input_values=[int(i)for i in input_values]

def count_elem(lst):
    has_small_neighbors = []
    for i in range(len(lst)):
        if i == 0 or i == len(lst) - 1:
            continue
        elif lst[i - 1] < lst[i] and lst[i] > lst[i + 1]:
            has_small_neighbors.append(lst[i])
    print(len(has_small_neighbors))


count_elem(input_values)

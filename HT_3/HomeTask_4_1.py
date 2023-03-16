#напишите функцию, которая принимает список и меняет местами егот первый и последний элемент
input_string = input("введите через пробел не менее 2 любых значений")
input_values = input_string.split()

def change(n):
    n[0], n[-1] = n[-1], n[0]
    print(n)

change(input_values)
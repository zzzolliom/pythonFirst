#Используя random.sample сгенерируйте список случайных элементов. Используйте List comprehension.



def random_digit(n,l):
    from random import sample
    if n>=l or n==l:
        my_random_lst=sample([i for i in range(n)],l)
        print(my_random_lst)
    elif n is not int or l is not int:
        raise ValueError("Все введенные значения должны быть целыми числами")
    else:
        raise ValueError("n не может быть меньше l")



if __name__=="__main__":
    a = int(input("введите число, которое определит границу выбора рандомных значений"))
    b = int(input("введите число, которое определит длину списка my_random_lst"))
    random_digit(a,b)
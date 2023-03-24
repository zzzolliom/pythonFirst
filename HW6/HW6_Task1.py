#Напишите программу, принимающую на вход слова через запятую и выводящую слова в алфавитном порядке. Используйте List comprehension.

def words_sorting(words):
    words_lst2=[]
    words_lst2=[i for i in words if isinstance(i, str)]
    words_lst2=[i.lower() for i in words_lst2]
    words_lst2.sort()
    return(words_lst2)


if __name__ == "__main__":
    words_lst = [1, 3, "LION", "APPLE", "HOUSE", None, [], "apple"]
    print(words_sorting(words_lst))


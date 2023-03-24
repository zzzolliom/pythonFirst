
""" напишите ф-ю """
dict_d={1:2,2:3,3:4}
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key not in d:
        d[key].append(value)

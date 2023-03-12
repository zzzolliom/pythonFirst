people = str(input())
cars= input()
people=people.split(' ')
cars=cars.split(' ')
people.sort()
cars.sort()
#result_list=(zip_longest(people,cars,fillvalue='Для вас нет машин'))
result_list=list(zip(people,cars))
if len(people)==len(cars):
    print(result_list)
else:
       print('Для кого-то нет машин')
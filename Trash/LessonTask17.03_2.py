import random

throw= (random.randint(1,6))
throw2= (random.randint(1,6))
print(throw, throw2)
answer= input("Еще раз?")
while answer=="Yes":
    throw = (random.randint(1, 6))
    throw2 = (random.randint(1, 6))
    print(throw, throw2)
    answer = input("Еще раз?")



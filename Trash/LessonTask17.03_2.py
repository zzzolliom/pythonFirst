import random
from collections import Counter
throw_count =[]
for i in range (10000000):
    throw = (random.randint(1, 6))
    throw_count.append(throw)
print(Counter(throw_count))


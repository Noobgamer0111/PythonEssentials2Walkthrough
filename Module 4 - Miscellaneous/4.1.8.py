# Use filter() to filter out only positive and even numbers from a list of random numbers 
# using lambda function.
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)
    
# Output:
# [10, -3, 5, 7, -10]
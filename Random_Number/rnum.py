# random number generator integer in the range 1 to 10

# import random
# random.randint(1, 10)

# for _ in range(10):
#     print(random.randint(1, 10))



# seed() method
# The seed() method is used to initialize the random number generator. The random number generator needs a number to start with (a seed value), to be able to generate a random number.

# random.seed(10)
# print(random.randint(1, 10))



# Random Number Generator
import random as rnd
_list =[]
i = 0
counter = 0
while i < 10:
    new= rnd.randint(1, 10)
    if new not in _list:
        _list.append(new)
        i += 1
        counter += 1
print(_list) # list of random numbers
print(counter) # number of iterations
'''
Randomization in Python: First you must import the random module
See documentation for how to use random module in python
'''
import random
random_integer = random.randint(1, 10)
#print(random_integer)
# The above will print a number between 1 and 10 each time you run it
random_float = random.random() # this only gives 0 => <1
#print(random_float)

# To find a floats between 0 and any other number, use random.uniform(0, 5)
random_float_1 = random.uniform(0,5)
print(random_float_1)

#or
randomFloat = random.random() * 5
print(randomFloat)

#from the previous code challenge

love_score = random.randint(0, 100)
print(f" Your love score is {love_score}")
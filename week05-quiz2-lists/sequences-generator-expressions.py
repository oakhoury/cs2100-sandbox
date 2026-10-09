'''
Code to demonstrate working with sequences
Includes code on list comprehension, generator expressions,
  and using the any() and all() functions
'''
import random

# Pick 50 unique random numbers from a range of 1 to 500
# range() is a sequence type
# random.sample() returns a list... which is a sequence type
unique_numbers = random.sample(range(1, 501), 50)
un = unique_numbers

# 10 unique numbers... but in a tuple, default is a list (see above)
# A tuple is also a sequence type
t = tuple(random.sample(range(1, 501), 10))

# A string is also a sequence type
phrase = 'AI is not ML'

list_of_words = phrase.split()

# The reverse of split is join
phrase_with_dots = '.'.join(phrase.split())


# A 2D list... (e.g. a matrix or grid):
grid : list[list[int]] = [
    [10, 20, 30],
    [50, 60, 70],
    [80, 90, 100, 200, 300, 400]
]

# list generator... eagerly creates list
l = [c for c in 'Iterable' if c.lower() in 'aeiou']


# generator expression... lazily generates each
# item only when requested via next()
g = (c for c in 'Iterable' if c.lower() in 'aeiou')
next(g)

# Additional calls to next(g) generate the next item
# That generation is lazy... the item is generated
# only when requested.


# The statistics module has function for common statistics
# See: https://docs.python.org/3/library/statistics.html
from statistics import mean, stdev

mean_value = mean(unique_numbers)
stdev_value = stdev(unique_numbers)
print(f'mean = {mean_value} and stdev = {stdev_value}')

# Now, let's find out if any of the 50 randomly generated numbers is 
# 1 standard deviation greater than the mean
is_any_above_1stdev = any(v > mean_value + 1.5 * stdev_value for v in unique_numbers)

# The following will create the list with values that are 1 stdev above mean
# It's repetitive of some of the work done already, this is just a demo!
above_1stdev = [v for v in unique_numbers if v > mean_value + 1.5 * stdev_value]
print(f'Values 1 standard deviation above mean: {above_1stdev}')

# Exercise: Edit the code to do this for 1.5 of 2 standard deviations above the mean.
# Run the code several times... you should see that sometimes there are no values
# that are 1.5 standard deviations above the mean and most of the time there are no
# values that are 2 standard deviations above.

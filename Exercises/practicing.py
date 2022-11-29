import math
from statistics import mean, median, mode

data_science = 9, 11, 22, 34, 17, 22, 40
mean(9, )


# mean(data_science(9, 11, 22, 34, 17, 22, 40))


def square(x):
    square = (x * x)
    return square


def squaring(number):
    return number ** 2


print("the value of 6 is: ", squaring(6))
print("the value of 7 is:", square(7))

import random

for roll in range(10):
    print(random.randrange(1, 9), end=' z')

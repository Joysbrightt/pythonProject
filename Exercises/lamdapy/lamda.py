
# using lambda to add to variable

# add = lambda x, y: x+y
# sub= lambda x, y: x + y
#
# print(add.__name__)
# print(sub.__name__)
#
#
# # calling a function that can take another function as parameter
#
# def add(a,b):
#     return a+b
#
# def sub(c,d):
#     return d-c
# def mult(e,f):
#     return e * f
#
# def div(g,h):
#     return h / g
#
#
# def operate(x, y, funct):
#     return funct(x, y)
#
















# writing a function called multiple let it have a parameter and function
from functools import reduce


def multiple(x, f):
    return f(x)


def double(x):
    return x * x

# val_double = multiple((5,)

# val_double = multiple(5, lambda x: x * x)
# print(val_double)

# val_triple = multiple(5, lambda x: x * x * x)
# print(val_triple)




#
#
# val_sub = operate(5, 24, sub)
# val_add = operate(5, 24, add)
# function_of_mult = operate(5, 24, mult)
# function_of_div = operate(4, 16, div)
#
# div = operate(5,24, lambda x, y: y/x)
#
#
#
# print(val_sub)
# print(val_add)
# print(function_of_mult)
# print((int)(function_of_div))
#
# print(div)

# absolute (abs)


# test using a function all
# print(all([1,2,23,3,4,5,5,0]))
# print(all([1,2,23,3,4,5,5]))
#
# print(all([True, False, True]))
# print(all([True, True, True]))
# print(any([True, True, True]))


names = ["Amaka", "Segun", "comb", "Samson", "foil"]
print([name.istitle() for name in names])

print(all([names.istitle() for name in names]))

# using keyword ANY in accessing a dictionary
# peoples =[
#     {"name": "Omosetan" "Omorele", "age": 30, "Year_of_exp": 4, "language": ["python", "java"]},
#     {"name": "John" "Doe", "age": 25, "Year_of_exp": 2, "language": ["JavaScript", "C#"]},
#     {"name": "Amaka" "Stephen", "age": 19, "Year_of_exp": 5, "language": ["python"]},
#     {"name": "Florence" "Segun", "age": 28, "Year_of_exp": 4, "language": ["JavaScript", "Python", "java", "HTML"]},
#     {"name": "Ernest" "Adeola", "age": 30, "Year_of_exp": 4, "language": ["JavaScript", "java", "Kotlin"]},
#
#
# ]
# print([people["age"] <= 20 and "Python" in people["language"] for people in peoples])
# print(any([people["age"] <= 20 and people["language"] == 'Python' for people in peoples]))
# print([people["name"] for people in peoples if people["age"] <= 28 and "Python" in peoples])
#
#
#
# # map is a higher other function
# map will take two things
# map is a list one can get iterable from using keyword list on it..
# map work is to transform and return whatever it's given
# it essential for functional programming
# map object will only evauluate once

# lst = list(map(lambda x: x**2, range(1, 10)))
# print(lst)

map_object = map(lambda a: a**2, range(1, 10))
lst1 = list(map_object)

map_object = map(lambda a: a**2, range(1, 15))
lst2 = list(map_object)

print("1", lst1)
print("2", lst2)

map_object = map(lambda a: a**2 if a % 2 == 0 else a, range(1, 10))
lst3 = list(map_object)
print("3", lst3)

# filter will only give the condition of a parameter met
# filter give it something that will give it either true or false

def isEven(a):
    return a % 2 == 0

filter_obj = list(filter(isEven, range(1,10)))
print((filter_obj))


# using keyword REDUCE
#
number = reduce(lambda a, b: a + b, range(1,11))
print(number)



# find the longest string
#  from functools import reduce
fruits = ["Apple", "Pear", "Pineapple", "Orange", "Watermelon", "Banana", "Cucumber"]
longest = reduce(lambda a, b: a if len(a) > len(b) else b, fruits)
shortest = reduce(lambda c, d: c if len(c) < len(d) else d, fruits )
equals = reduce(lambda e, r: e if len(e) >= len(r) else r, fruits)
print(shortest)
print(fruits)
print(longest)

# using MAX to find the maximum string in a list
fruits = ["Pear", "Apple", "Pineapples", "Orange", "Watermelon", "Banana", "Cucumber"]
print(max(fruits))
# gives the maximum item in the list
print(max(fruits, key= len))
# sorting list of items from the short to the longest
print(sorted(fruits, key=len, reverse=True))

# sorting items in a list alphabetically
print(sorted(fruits, key= lambda x: x[-1]))
# todo list, set, dict, strings

# S = "Hello"
#
# it = iter(S)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
# for lst in [1, 2, 3, 4, 5]:
#     print(lst)


def custom_for(iterable, func):
    it = iter(iterable)
    while True:
        try:
            func(next(it))
        except StopIteration:
            break


def cube(num):
    print(num ** 3)


custom_for([1, 2, 3, 4, 5], cube)


def gen():
    count = 0
    while True:
        yield count
        count += 1
        # for i in gen()



def counter(low, high):
    while low < high:
        yield  low
        low +1

print(list(counter(2,6)))

tiger = gen()
print(next(tiger))
print(next(tiger))
print(next(tiger))
print(next(tiger))
print(next(tiger))
print(next(tiger))


# number = 1
#
# def func():
#     print(number)
#     def func_two():
#         print(number)
from typing import Tuple


def function(param):
    print("Before reassignment -> ", id(param))
    param = 5
    print("After reassignment -> ", id(param))

num =45
print("Num--> ", id(num))
function(num)


def add(a: int, b: int) -> bool:
    return a+b
print(add(2,3))


def add(a: int, b: int) -> int:
    return a > b
print(add(2,3))



def add(a: int = 2, b: str = "colour") -> Tuple[int, str]:
    return a, b
# print(add(3,"3"))
# print(add(3))
# print(add())
print(add(b ="Your score"))


def mutatable_ish(a = None):
    if a is None:
        a= []
    a.append("python")
    return a
print(mutatable_ish())
print(mutatable_ish())
print(mutatable_ish([1,2,3]))
print(mutatable_ish())



def add(*numbers):
    total = 0
    for num in numbers:
        total+= num
    return total
lst = [7.9,3,10,34]

print(add(*[1,2,3,4,5,6,77,8]))
print(add(*lst))

def add(a, *numbers):
    total = 0
    for num in numbers:
        total+= num
    return total
print(add(1,2,3,4,5,6,77,8))


def dict_pack_unpack(**kwargs):
    print(kwargs)

dict_pack_unpack(name = "shola", age = 45, sex = "Male")


def dict_pack_unpack( *args, **kwargs):
    print("kwargs", kwargs)
    print("Args", args)

dict_pack_unpack( 4,5, "goal", name= "shola", age = 45, sex = "Male")



d = dict(a = 1, b = 2, c = 3, d= 4)
print(d)

dict_pack_unpack(**d)



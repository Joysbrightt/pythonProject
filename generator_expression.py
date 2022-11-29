import sys

# generator expression
list = [num for num in range(1, 11)]
gen = (num for num in range(1, 11))
# dictionary comprehension
dict_comp = {k: v for k, v in zip(range(5), range(5))}

# set comprehension
set = {}


def get_first(s: str) -> str:
    return s[0]


l = [get_first(val) for val in ["Hello", "How", "are", "you"]]
print(l)

print(sum(list))
print(sum(gen))
print(sys.getsizeof(gen))
print(dict_comp)

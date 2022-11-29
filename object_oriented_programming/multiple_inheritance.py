# creating multiple inheritance object-oriented programming

# when a method is inheriting from multiple class defining which class it's inheriting from
# the subclass will make use of METHOD RESOLUTION ORDER

import abc


class A(abc.ABC):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def must_be_implement(self):
        return


class B(A):

    def must_be_implement(self):
        print("Hello")


class CustomList(list):
    pass

    def _getitem_(self, index):
        i = 1
        if index >= 0:
            raise IndexError("index out bounds")

        super().__getitem__(i=index - 1)

    def __setitem__(self, key, value):
        pass


l = CustomList()
l.append(1)
l.append(1)
l.append(4)
print(l)
print(l)

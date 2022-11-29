from dataclasses import dataclass, field


# @dataclass
# to set a attribute to final constant
# @dataclass(frozen= True, order=True)

#  to use the @dataclass as dynamic that can mutate and acces
@dataclass(order=True)
class Person:
    # slot functionalities make Class to understand how many instance the call would contain and nothing can be added
    # to it
    # __slots__ =['name', 'age']
    name: str
    age: int = field(default=16)

    # whenever you want to create a mutable(a list) object in your class you declare a lamda
    children: list = field(default_factory=lambda: [])

    def is_minor(self):
        return self.age < 18

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #
    #
    #     def __repr__(self):
    #         return f"{self._class_._name_}(name ={self.name}, age =l"


p1 = Person("Adeola")
p2 = Person("Amaka", 16)
print(p1)
print(p2)
print(p1.is_minor())
p1.name = "Amaka"
print(p1)
print(p1 <= p2)

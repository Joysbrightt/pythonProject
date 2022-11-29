class Animal:

    def __init__(self, name, age=0):
        print("From Animal")
        self.name = name
        self.age = age

    def speak(self):
        return "Animal speak"


class Dog(Animal):
    def __init__(self, name, age, type_):
        print("From Dog")
        super().__init__(name, age)
        self.type_ = type_

    def speak(self):
        super().speak()
        return "Dog speak"

# multiple inheritance class
class Cat(Animal):
    super().speak()



class Bing(Dog,Cat):


bingo = Bing(Dog,Cat)
dog = Dog("Bingo", 24, "local")
cat = Cat("Katty")
print(dog.name, dog.age, dog.type_)
print(dog.speak())

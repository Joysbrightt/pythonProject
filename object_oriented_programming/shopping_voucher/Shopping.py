class playground:

    @property
    def __init__(self, age, name):
        self._age = age
        self._name = name

    def  __repr__(self):
        return f"<playground: {self._name}>"
    
    # def __str__(self, name=None):
    #     return f"<playground: {name ={self._name}, age ={self._age}}>"
    #
        
        

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age


p1 = playground("funmi", "bob", 70)
print(p1.name)

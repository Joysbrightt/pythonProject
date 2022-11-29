class Player:
    pass

    def __init__(self, nameless: str, age: int) -> None:
        self.name = nameless
        self.age = age

    def say_my_name(self):
        print()


player1 = Player("Messi", 45)
print(player1.name)
print(player1.age)

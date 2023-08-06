# class attribute
"""
class Player:  # this creates a simple class with the name Player
    max_hp = 4000  # max_hp is a class attribute


player1 = Player()
print(player1.max_hp)
player2 = Player()
print(player2.max_hp)

# changed the value of the class, changed the value of the objects
Player.max_hp = 5000
print(player1.max_hp)
print(player2.max_hp)

"""
# instance attributes


class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0

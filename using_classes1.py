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


player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)

print("P1:", player1.name, " -- HP:", player1.hp, "-- SCORE: ", player1.score)
print("P2:", player2.name, " -- HP:", player2.hp, "-- SCORE: ", player2.score)

player1.hp += 500
player1.score += 10
print("P1:", player1.name, " -- HP:", player1.hp, "-- SCORE: ", player1.score)
print("P2:", player2.name, " -- HP:", player2.hp, "-- SCORE: ", player2.score)

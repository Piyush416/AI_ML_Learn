# Concept: Instance & Class Attributes
''' Q8. Create a class Player with:
• a class variable player_count
• instance variables name and level
Track how many players were created. '''

class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1
    
    @classmethod
    def show_player(cls):
        print(cls.player_count)


p1 = Player("piyush", "beginner")
p2 = Player("shree", "intermediate")
p3 = Player("Neha", "advance")

Player.show_player()
    
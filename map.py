import random
from entities import Pokemon

class Map:
    def __init__(self, name):
        self.name = name
        self.enemies = [
            Pokemon("Wild Pidgey", 5, 10),
            Pokemon("Wild Rattata", 4, 8),
            # Add more Pokémon as needed
        ]

    def draw(self, surface):
        # Load and draw the map background
        pass

    def get_random_enemy(self):
        return random.choice(self.enemies)

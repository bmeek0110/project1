import pygame
from entities import Player
from battle import Battle
from map import Map

class Game:
    def __init__(self):
        self.player = Player(100, 100)
        self.state = "exploring"
        self.battle = None
        self.current_map = Map("town")

    def update(self, keys):
        if self.state == "exploring":
            self.player.move(keys)
            self.check_encounter()

    def draw(self, surface):
        self.current_map.draw(surface)
        self.player.draw(surface)

        if self.state == "battling":
            self.draw_battle(surface)

    def check_encounter(self):
        if pygame.time.get_ticks() % 5000 < 100:  # Random encounter logic
            self.start_battle()

    def start_battle(self):
        enemy_pokemon = self.current_map.get_random_enemy()
        self.battle = Battle(self.player.current_pokemon, enemy_pokemon)
        self.state = "battling"

    def draw_battle(self, surface):
        # Implement battle UI rendering here
        pass

    def end_battle(self):
        self.state = "exploring"
        self.battle = None

import pygame
import random

class Move:
    def __init__(self, name, damage, move_type):
        self.name = name
        self.damage = damage
        self.move_type = move_type  # e.g., "physical", "special"

    def calculate_damage(self, attacker):
        # Simple damage calculation logic
        base_damage = self.damage + (attacker.level // 2)
        return base_damage

class Pokemon:
    def __init__(self, name, level, health, evolution=None):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = health
        self.evolution = evolution

    def level_up(self):
        self.level += 1
        if self.level == 16 and self.evolution:  # Example evolution level
            self.evolve()

    def evolve(self):
        self.name = self.evolution
        print(f"{self.name} has evolved!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/sprites/player.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5
        self.current_pokemon = Pokemon("Starter Pokémon", 5, 20)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

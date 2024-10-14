import pygame
import os

def load_image(file_name):
    return pygame.image.load(os.path.join('assets', file_name))

def load_sound(file_name):
    return pygame.mixer.Sound(os.path.join('assets', 'sounds', file_name))

def play_sound(sound_name):
    sound = load_sound(sound_name)
    sound.play()

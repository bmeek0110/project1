import pygame
from game import Game

def main():
    # Initialize Pygame
    pygame.init()

    # Set up display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Professional Pokémon Game")

    # Create game instance
    game = Game()

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        game.update(keys)
        screen.fill((255, 255, 255))  # Clear screen
        game.draw(screen)               # Draw game elements

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

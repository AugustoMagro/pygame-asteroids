import pygame
from constants import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        self.main()

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.screen.fill((0, 0, 0, 0.5), rect=None, special_flags=0)
            pygame.display.flip()

if __name__ == "__main__":
    Game()

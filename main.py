import pygame
from constants import *
from player import Player

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        
        self.clock = pygame.time.Clock()
        self.dt = 0
        x = SCREEN_WIDTH/2
        y = SCREEN_HEIGHT/2
        self.player = Player(x,y)
        self.main()

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.screen.fill((0, 0, 0, 0.5), rect=None, special_flags=0)
            self.player.draw(self.screen)
            self.player.update(self.dt)
            pygame.display.flip()
            self.dt = self.clock.tick(60)/1000

if __name__ == "__main__":
    Game()

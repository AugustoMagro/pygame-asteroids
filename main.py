import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        self.clock = pygame.time.Clock()
        x = SCREEN_WIDTH/2
        y = SCREEN_HEIGHT/2


        self.updatable = pygame.sprite.Group() 
        self.drawable = pygame.sprite.Group() 
        self.asteroids = pygame.sprite.Group()

        Asteroid.containers = (self.updatable, self.drawable, self.asteroids)
        AsteroidField.containers = self.updatable
        self.asteroidField = AsteroidField()

        Player.containers = (self.updatable, self.drawable)
        self.player = Player(x,y)

        self.dt = 0

        self.main()

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.updatable.update(self.dt)

            for asteroid in self.asteroids:
                if asteroid.collides_with(self.player):
                    print("Game over!")
                    sys.exit()

            self.screen.fill("black")

            for obj in self.drawable:
                obj.draw(self.screen)

            pygame.display.flip()

            self.dt = self.clock.tick(144)/1000

if __name__ == "__main__":
    Game()

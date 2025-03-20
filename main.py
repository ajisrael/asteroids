# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    AsteroidField()

    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.kill()
                    shot.kill()
        
        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # limit frame rate to 60 fps
        time_passed = clock.tick(60)
        dt = time_passed / 1000


# This line ensures the main() function is only called when this file is run directly;
# it won't run if it's imported as a module. It's considered the "pythonic" way to structure
# an executable program in Python. Technically, the program will work fine by just calling
# main(), but you might get an angry letter from Guido van Rossum if you don't.
if __name__ == "__main__":
    main()

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from player import Player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        
        screen.fill("black")
        player.draw(screen)
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

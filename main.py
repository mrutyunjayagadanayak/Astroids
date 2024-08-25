# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (astroids,updatable,drawable)
    AsteroidField.containers = updatable
    astroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for i in updatable:
            i.update(dt)
        
        for astroid in astroids:
            if astroid.collision(player):
                print("Game Over")
                sys.exit()

        for astroid in astroids:
            for shot in shots:
                if astroid.collision(shot):
                    astroid.kill()
                    shot.kill()

        screen.fill("black")

        for i in drawable:
            i.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) /1000


if __name__ == "__main__":
    main()
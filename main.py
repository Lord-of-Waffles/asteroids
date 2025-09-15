import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 #delta time
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatables.update(dt)
        #player.update(dt)
        for thing in drawables:
            thing.draw(screen)
        #player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                sys.exit("Game over!")

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_check(asteroid) == True:
                    asteroid.split()
                    shot.kill()





if __name__ == "__main__":
    main()

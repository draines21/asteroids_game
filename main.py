import sys 
import pygame 
from constants import *
from player import *
from asteroid import Asteroid 
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock  = pygame.time.Clock()
    dt = 0 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField() 
   
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    print("Starting Asteroids!")
    print("Screen width:",  SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
        screen.fill("black")
        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.collision_check(asteroids):
                print("Game Over!")
                sys.exit() 
            


        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000.0



if __name__ == "__main__":
    main()

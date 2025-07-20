import pygame 
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock  = pygame.time.Clock()
    dt = 0 
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    Player.containers = (updateable, drawable)
    
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting Asteroids!")
    print("Screen width:",  SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
        screen.fill((0, 0, 0))
        updateable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000.0



if __name__ == "__main__":
    main()

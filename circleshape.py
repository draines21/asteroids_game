import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, asteroids):
        for asteroid in asteroids:
            if self is asteroid:
                continue
            distance = self.position.distance_to(asteroid.position) 
            if distance <= self.radius + asteroid.radius: 
                return True 
        return False
    



class Shot(CircleShape):
    SHOT_RADIUS = 5

    def __init__(self, x, y, radius):
        super.__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,self.position, self.SHOT_RADIUS)


    def update(self, dt):
        self.position += self.velocity * dt

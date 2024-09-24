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


    # other is anothher CircleShape class object (we named it other, there is no 'other' object)
    # every CircleShape's position property is a pygame.Vector2 - we using its distance_to method to calculate distances between the two
    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

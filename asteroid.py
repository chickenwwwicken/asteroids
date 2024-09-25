import pygame
import random 
from constants import *
from circleshape import CircleShape


# new class for the asteroids
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    # overriding draw() method from CircleShape class
    def draw(self, screen):
        pygame.draw.circle(screen, ("orange"), self.position, self.radius, 2)


    # overriding update() method from CircleShape
    def update(self, dt):
        self.position += self.velocity * dt


    # split method when shot collides with asteroid
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2

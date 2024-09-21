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

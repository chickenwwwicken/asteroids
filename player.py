import pygame

from constants import *
from circleshape import CircleShape


# new class for the player inherits from CircleShape
class Player(CircleShape):
    def __init__(self, x, y):

        # adding three parameters in super init cuz CircleShape has three parameters
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 


    # overriding the draw() method from CircleShape class
    # pygame.draw.polygon takes four parameters:
    # surface - (screen) surface to draw on
    # color - (white) color to paint it
    # points - (self.triangle()) list of points to draw with
    # width - (2) (optional) default is to fill it
    def draw(self, screen):
        pygame.draw.polygon(screen, ("green"), self.triangle(), 2)


    # method copied from lane
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    # method for rotation 
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    # method for moving forward/backward
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    # method copied from lane
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # rotate left
        if keys[pygame.K_a]:
            self.rotate(-dt)

        # rotate right
        if keys[pygame.K_d]:
            self.rotate(dt)

        # move forward
        if keys[pygame.K_w]:
            self.move(dt)

        # move backward
        if keys[pygame.K_s]:
            self.move(-dt)


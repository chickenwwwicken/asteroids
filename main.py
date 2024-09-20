import pygame

# constants is another python file
from constants import *


def main():
    # initializing pygame
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # creating a GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Creating a pygame.time.Clock object
    # and a dt variable set to 0
    clock = pygame.time.Clock()

    # creating a delta time variable 
    dt = 0

    # Infinite while loop for Game Loop
    while True:

        # added this code cuz lane tol me to
        # assume its a quit function for quiting w event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # pygame fill method to fill the GUI Window we created with a solid "black" color (0,0,0)
        pygame.Surface.fill( screen , (0,0,0) )
        # this also works: (it's what lane did)
        # screen.fill("black") 
        
        
        # this will update the full display Surface to the screen
        pygame.display.flip()

        # adding .tick() method to set limit of 60fps 
        # dt (delta time) 
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

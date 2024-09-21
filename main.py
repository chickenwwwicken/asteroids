import pygame

# constants is another python file
from constants import *
from player import Player


def main():

    # initializing pygame
    pygame.init()
    print("Starting asteroids!")

    # creating a GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Creating a pygame.time.Clock object
    # and a dt variable set to 0
    clock = pygame.time.Clock()

    # creating groups of sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # creating a delta time variable 
    dt = 0

    # creating our player object with Player class attributes (x,y)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Infinite while loop for Game Loop
    while True:

        # added this code cuz lane tol me to
        # assume its a quit function for quiting w event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        # iterating over groups to update them easier
        for object in updatable:
            object.update(dt)

       
        # player rotation method from player.py
        # this next line was removed because added to Group above
        # player1.update(dt)


        # pygame fill method to fill the GUI Window we created with a solid "black" color (0,0,0)
        pygame.Surface.fill( screen , (0,0,0) )
        # this also works: (it's what lane did)
        # screen.fill("black") 

        
        # iterating over groups to update them easier
        for object in drawable:
            object.draw(screen)
        

        # adding a method from player.py to render the player on screen
        # this next line was removed because added to Group above             #player1.draw(screen)
        
        
        # this will update the full display Surface to the screen
        pygame.display.flip()

        # adding .tick() method to set limit of 60fps 
        # dt (delta time) 
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()

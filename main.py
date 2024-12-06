# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main ():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame
    pygame.init()
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Game logic (update game state, etc.)
        # ...

        # Drawing (render graphics)
        screen.fill("black")

        # Update the display
        pygame.display.flip()    
        
    # Quit Pygame
    pygame.quit()       

if __name__ == "__main__":
    main()
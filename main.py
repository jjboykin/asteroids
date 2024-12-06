import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main ():
    print("Starting asteroids!")
    print(f"Display Mode: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up the display
    clock = pygame.time.Clock()
    dt = 0

    # Setup the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    # Set up the player
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Set up the field
    asteroid_field = AsteroidField()

    # Game loop
    running = True
    while running:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Game logic (update game state, etc.)
        

        # Drawing (render graphics)
        screen.fill("black")
        
        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        # Update the display
        pygame.display.flip()
        
        # Limit the framerate
        dt = clock.tick(SCREEN_FPS) / CONVERT_MILLISECONDS_TO_SECONDS    
        
    # Quit Pygame
    pygame.quit()       

if __name__ == "__main__":
    main()
import sys

import pygame

class Settings():
    """A class to store all settings for Alien Invasion."""
def __init__(self, screen):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    #Start the main loop for the game.
    while True:

        #Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
		

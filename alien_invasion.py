import sys
import pygame

from settings import Settings
from ship import Ship




class AlienInvasion:
    """A class for the overall game."""

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")
        self.screen.fill(self.settings.bg_color)
        self.ship = Ship(self)



    def run_game(self):
        """The main game loop."""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #make th emost recently drawn screen visible.
            pygame.display.flip()
            self.ship.blit_me()


    

if __name__ == '__main__':
    
    ai = AlienInvasion()
    ai.run_game()
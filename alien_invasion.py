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




    def check_event(self, event):
        
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_RIGHT:
                self.ship.moving_right = True

        elif event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = False
            elif event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
                

    def run_game(self):
        """The main game loop."""

        while True:
            for event in pygame.event.get():
                self.check_event(event)

            # redraw the screen during each pass through the loop.
            self.ship.update()
            self.ship.blit_me()

            #make the emost recently drawn screen visible.
            pygame.display.flip()
            
            


    

if __name__ == '__main__':
    
    ai = AlienInvasion()
    ai.run_game()
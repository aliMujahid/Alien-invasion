import sys
import pygame

from settings import Settings
from ship import Ship
from  bullet import Bullet




class AlienInvasion:
    """A class for the overall game."""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        

        self.ship = Ship(self)
        self.bullets  = []



    def fire_bullets(self):
        new_bullet = Bullet(self)
        self.bullets.append(new_bullet)

    def check_event(self):

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)



    def check_keydown_events(self, event):
        """manage presses"""
        if event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullets()
            



    def check_keyup_events(self, event):
        """manage key releases"""
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False


    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.update()
        self.ship.blit_me()
        
        for bullet in self.bullets:
            bullet.update()
            bullet.draw()
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)

    
        #make the emost recently drawn screen visible.
        pygame.display.flip()



    def run_game(self):
        """The main game loop."""

        while True:

            self.check_event()

            # redraw the screen during each pass through the loop.
            self.update_screen()


            
            


    

if __name__ == '__main__':
    
    ai = AlienInvasion()
    ai.run_game()
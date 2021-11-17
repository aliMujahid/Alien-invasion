import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien




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
        self.bullets  = pygame.sprite.Group()
        self.ailens = pygame.sprite.Group()

        self._create_fleet()




    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x//(2*alien_width)

        #find the number of rows.
        alien_height = alien.rect.height
        available_space_y = self.settings.screen_height - (3*alien_height) - self.ship.rect.height
        number_alien_row = available_space_y // (2*alien_height)  

        for row_number in range(number_alien_row):
            for alien_number in range(number_alien_x):
            
                self._create_alien(row_number, alien_number)




    def _create_alien(self, row_number, alien_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.ailens.add(alien)




    def fire_bullets(self):
        """Create a new bullet and add it to the bullets group."""
        
        if len(self.bullets) < self.settings.bullets_allowed:

            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)




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




    def _update_bullets(self):
        self.bullets.update()
        
        for bullet in self.bullets:
            bullet.draw()
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)




    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_me()
        self._update_bullets()
        self.ailens.draw(self.screen)
        
        #make the emost recently drawn screen visible.
        pygame.display.flip()



    def run_game(self):
        """The main game loop."""

        while True:

            self.check_event()
            self.ship.update()
            
            # redraw the screen during each pass through the loop.
            self.update_screen()


            
            


    

if __name__ == '__main__':
    
    ai = AlienInvasion()
    ai.run_game()
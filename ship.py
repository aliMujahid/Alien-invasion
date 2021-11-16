import pygame


class Ship:
    """A class for the ship."""

    def __init__(self, ai_game):
        #init the ship and set its starting position.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Load the ships image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #movment flag
        self.moving_right = False
        self.moving_left = False

        #store a decimal value of x for movement
        self.x = float(self.rect.x)



    def update(self):
        if self.moving_left and self.x>0 :
            self.x -= self.settings.ship_speed
        elif self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.ship_speed

        self.rect.x = self.x



    def blit_me(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)
import pygame

class Ship:
    """A class for the ship."""

    def __init__(self, ai_game):
        #init the ship and set its starting position.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ships image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom




    def blit_me(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)
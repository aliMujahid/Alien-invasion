from typing import Tuple
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the alien image and get its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alien at the topleft corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y  = self.rect.height

        #store a decimal value of the y coordinate
        self.y = float(self.rect.y)

    def update(self):
        """move the alien left and right."""
        self.x = self.rect.x
        self.x += self.settings.alien_speed*self.settings.fleet_direction
        self.rect.x = self.x



    def check_edge(self):
        """check if the aliens colide with the sides."""
        self.screen_rect = self.screen.get_rect()

        if self.rect.right >= self.screen_rect.width or self.rect.left <=0:
            return True
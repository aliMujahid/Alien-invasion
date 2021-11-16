import pygame 


class Settings:
    """A class for ai_game settings"""

    def __init__(self):

        #display settings
        self.screen_width = 800
        self.screen_height = 1200
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed = 1

        # bullet settings
        self.bullet_speed = 0.5
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60,60,60)
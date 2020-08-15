import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):

        """Initialize the ship & set starting postion"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load the ship image & get its rect
        self.image = pygame.image.load("../image/ship.bmp")
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # move flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        """center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """update the ship postion based on the movenent flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # self.rect.x+=1 old code
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

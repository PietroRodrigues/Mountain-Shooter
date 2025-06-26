from Class.Entity import Entity
import pygame
from Class.Const import *

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        
        press_keys = pygame.key.get_pressed()

        if press_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if press_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.left < WIN_WIDTH - self.rect.width:
            self.rect.centerx += ENTITY_SPEED[self.name]
        if press_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if press_keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]


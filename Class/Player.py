from Class.Entity import Entity
from Class.PlayerShot import PlayerShot
import pygame
from Class.Const import *

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.health = ENTITY_HEALTH[self.name]
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
        self.score = 0

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
        
    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay <= 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            press = pygame.key.get_pressed()
            if press[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(f"{self.name}Shot", self.rect.center)
           
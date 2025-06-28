from Class.Const import *
import pygame
from Class.Entity import Entity

class EnemyShot (Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.damage = ENTITY_SHOOT_DAMAGE[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

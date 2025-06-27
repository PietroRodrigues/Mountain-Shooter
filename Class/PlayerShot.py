from Class.Entity import Entity
import pygame
from Class.Const import *

class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]


from Class.Entity import Entity
from Class.Const import *
import random

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH 
            self.rect.top = random.randint(40, WIN_HEIGHT - 40)

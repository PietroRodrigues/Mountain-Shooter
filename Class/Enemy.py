
from Class.Entity import Entity
from Class.Const import *
from Class.EnemyShot import EnemyShot
import random

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.health = ENTITY_HEALTH[self.name]
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
        self.last_damage = ""
        self.score = ENTITY_SCORE[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        

    def shoot(self):
       self.shoot_delay -= 1
       if self.shoot_delay <= 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            return EnemyShot(f"{self.name}Shot", self.rect.center)

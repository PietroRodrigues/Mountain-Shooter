from Class.Const import *
from Class.Entity import Entity
from Class.Enemy import Enemy
from Class.Player import Player
from Class.PlayerShot import PlayerShot
from Class.EnemyShot import EnemyShot

class EntityMediator:

    @staticmethod
    def __verity_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                return True
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                return True
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                return True
        
        return False

    @staticmethod
    def verify_colision(entity_list: list[Entity]):
        for ent in entity_list:
            if EntityMediator.__verity_collision_window(ent):
                entity_list.remove(ent)

        

    @staticmethod
    def verify_health(entity_list: list[Entity]):
            for ent in entity_list:
                if isinstance(ent, (Player, Enemy)):
                    if ent.health <= 0:
                        entity_list.remove(ent)

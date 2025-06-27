from Class.Const import *
from Class.Entity import Entity
from Class.Enemy import Enemy

class EntityMediator:

    @staticmethod
    def __verity_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

            

    @staticmethod
    def verify_colision(emtity_list: list[Entity]):
        for i in range(len(emtity_list)):
            entity_test = emtity_list[i]
            EntityMediator.__verity_collision_window(entity_test)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)

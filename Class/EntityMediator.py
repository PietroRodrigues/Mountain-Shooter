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
    def __verity_collision_entity(ent: Entity, ent2: Entity, entity_list: list[Entity]):
        valid_interaction = False
        if isinstance(ent, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True
      
        if valid_interaction:
            if (ent.rect.right >= ent2.rect.left and
                ent.rect.left <= ent2.rect.right and 
                ent.rect.top <= ent2.rect.bottom and 
                ent.rect.bottom >= ent2.rect.top):

                if isinstance(ent, (Player, Enemy)):
                    if (isinstance(ent2, (PlayerShot, EnemyShot))):
                        ent.health -= ent2.damage
                        entity_list.remove(ent2)
                        if isinstance(ent, Enemy):
                            ent.last_damage = ent2.name
    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        for i in range(1,3):
            if enemy.last_damage == f'Player{i}Shot':
                for ent in entity_list:
                    if ent.name == f'Player{i}':
                        if isinstance(ent, Player):
                            ent.score += enemy.score

    @staticmethod
    def verify_colision(entity_list: list[Entity]):
        for ent in entity_list:
            if EntityMediator.__verity_collision_window(ent):
                entity_list.remove(ent)
            for ent2 in entity_list:
                if ent == ent2:
                    continue
                EntityMediator.__verity_collision_entity(ent, ent2, entity_list)
        

    @staticmethod
    def verify_health(entity_list: list[Entity]):
            for ent in entity_list:
                if isinstance(ent, (Player, Enemy)):
                    if ent.health <= 0:
                        if isinstance(ent, Enemy):
                            EntityMediator.__give_score(ent,entity_list)
                        entity_list.remove(ent)


from Class.Background import Background
import random
from Class.Entity import Entity
from Class.Const import *
from Class.Player import Player
from Class.Enemy import Enemy
class EntityFactory:

    @staticmethod
    def get_entity(entity_name:str, position:tuple = (0, 0)):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH,0)))
                return list_bg
            case "Level2Bg":
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case "Player1":
                return Player("Player1", (10, WIN_HEIGHT/2))
            case "Player2":
                return Player("Player2", (10, WIN_HEIGHT/2 - 30))
            case "Enemy1":
                return Enemy("Enemy1", (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case "Enemy2":
                return Enemy("Enemy2", (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

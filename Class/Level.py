import pygame
from Class.Entity import Entity
from Class.EntityFactory import EntityFactory

class Level :
    def __init__(self, window: pygame.Surface, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        listBgs = EntityFactory.get_entity('Level1Bg')

        if isinstance(listBgs, list):
            self.entity_list.extend(listBgs)
        elif isinstance(listBgs, Entity):
            self.entity_list.append(listBgs)


    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()

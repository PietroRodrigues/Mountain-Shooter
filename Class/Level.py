import pygame
import random
from Class.Entity import Entity
from Class.Player import Player
from Class.Enemy import Enemy
from Class.EntityFactory import EntityFactory
from Class.Const import *
import sys
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect
from Class.EntityMediator import EntityMediator


class Level:
    def __init__(self, window: pygame.Surface, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.timeout = 20000  # 20 seconds)
        listBgs = EntityFactory.get_entity('Level1Bg')
        player = EntityFactory.get_entity('Player1')

        pygame.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN_RATE)

        if isinstance(listBgs, list):
            self.entity_list.extend(listBgs)
        elif isinstance(listBgs, Entity):
            self.entity_list.append(listBgs)

        if(self.game_mode == MENU_OPTION[1] or self.game_mode == MENU_OPTION[2]):  # Player vs Player
            player2 = EntityFactory.get_entity('Player2')
            if isinstance(player2, Entity):
                self.entity_list.append(player2)

        if isinstance(player, Entity):
            self.entity_list.append(player)

    def run(self):
        pygame.mixer_music.load(f"./asset/{self.name}.mp3")
        pygame.mixer_music.set_volume(VOLUME["music"])
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shot = ent.shoot()
                    if shot:
                        self.entity_list.append(shot)
                    if (ent.name == 'Player1'):
                        self.Level_text(18, f'Player1 - Health:{ent.health} | Score:{ent.score}' , C_GREEN, (10, 25))
                    if (ent.name == 'Player2'):
                        self.Level_text(18, f'Player2 - Health:{ent.health} | Score:{ent.score}', C_CYAN, (10, 45))
                       
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(['Enemy1', 'Enemy2'])
                    enemy = EntityFactory.get_entity(choice)
                    if isinstance(enemy, Entity):
                        self.entity_list.append(enemy)

            self.Level_text(18, f'{self.name} - Timeout : {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.Level_text(18, f'FPS: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.Level_text(18, f'Entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            #Colision and Health Verification
            EntityMediator.verify_colision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

    def Level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf,dest=text_rect)

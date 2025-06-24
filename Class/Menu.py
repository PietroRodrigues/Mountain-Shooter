import pygame
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect
from Class.Const import *


class Menu:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    
    def run(self):
        menu_opition = 0
        pygame.mixer_music.load("./asset/Menu.mp3")
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(self.surf, self.rect)
            self.Menu_text(70, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.Menu_text(70, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_opition:
                    self.Menu_text(30, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + (i * 25)))
                else:
                    self.Menu_text(30, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + (i * 25)))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_opition = menu_opition + 1 if menu_opition < len(MENU_OPTION) - 1 else 0
                    if event.key == pygame.K_UP:
                        menu_opition = menu_opition - 1 if menu_opition > 0 else len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_opition]
            
            pygame.display.flip()


    def Menu_text(self, text_size:int, text:str, text_color:tuple, text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
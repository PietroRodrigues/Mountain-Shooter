import pygame
from Class.Menu import Menu
from Class.Level import Level

from Class.Const import *

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0] or menu_return == MENU_OPTION[1] or menu_return == MENU_OPTION[2]:
                level = Level(self.window, 'Level1', menu_return)
                level.run()
            elif menu_return == MENU_OPTION[3]:
                pass
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()


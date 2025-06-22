import pygame


class Game:
    def __init__(self):
        self.wundow = None

    
    def run(self):

        pygame.init()

        self.window = pygame.display.set_mode((600, 480))

        while True:        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


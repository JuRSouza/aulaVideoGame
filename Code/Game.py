import pygame
from Code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events (Verifique todos os eventos)
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # Close window (fechar janela)
            #         quit()  # end pygame(encerrar a ainicialização do pygame)





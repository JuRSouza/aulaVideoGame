import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup Start')

print('Loop Start')
while True:
   # Check for all events (Verifique todos os eventos)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit() # Close window (fechar janela)
           quit() #end pygame(encerrar a ainicialização do pygame)







import pygame
import os
def display_state(state,screen):
    state
    img="C:\\Users\\Anis\\Desktop\\HangMan\\"+"hang"+str(state)+'.png'
    imp = pygame.image.load(img).convert()
    imp=pygame.transform.rotozoom(imp, 0, 0.5)

    screen.blit(imp, (280,150))
    pygame.display.flip()
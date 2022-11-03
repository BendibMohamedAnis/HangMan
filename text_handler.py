import pygame
def draw_text(text,color_rec,color_text,screen,size,posx,posy): 
            display_rect = pygame.Rect(posy, posx, 0, 32)    
            display_font = pygame.font.Font(None, size) 

            pygame.draw.rect(screen, pygame.Color(color_rec), display_rect)
            display_surface = display_font.render(text, True, color_text)
            screen.blit(display_surface, (display_rect.x+5, display_rect.y+5))
            pygame.display.flip()
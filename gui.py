from dis import dis
import pygame
import hang
import pygame.locals
import sys
from time import sleep
import text_handler
import hanged_image_handler
import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

words=["test","lol","reeee","lmso"]
word=random.choice(words)

pygame.display.set_caption('HangMan Game')
programIcon = pygame.image.load('C:\\Users\\Anis\\Desktop\\HangMan\\hangman.png')
pygame.display.set_icon(programIcon)
# Initialize pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0, 0, 0))

running = True
life = 5
display=[None] * len(word)
for i in range(len(word)):
        display[i]=" [ _ ] "

color_active = pygame.Color('red')
color_passive = pygame.Color('chartreuse4')
    
input_rect = pygame.Rect(200, 500, 480, 32)        
base_font = pygame.font.Font(None, 32)        
user_text = ''

display_rec= pygame.Rect(250, 10, 400, 32)    
display_font = pygame.font.Font(None, 32) 


hanged_image_handler.display_state(life,screen)

while running:
    if life>0:
        
        #text_handler.draw_text(str(display),color_active,'white',screen,32,100,100)
        pygame.draw.rect(screen, 'black', display_rec)
        display_surface = display_font.render(str(display), True, 'white')
        screen.blit(display_surface, (SCREEN_WIDTH/3.2, SCREEN_HEIGHT/30))
        pygame.display.flip()



        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                else:
                        user_text += event.unicode
                        user_text= user_text.lower()

                        if len(user_text)==1:
                            res,pos=hang.exist(user_text,word)
                            if res:
                                        text='You got the letter "'+ str(user_text) + '" Right ! on '+str(len(pos))+" position(s)"
                                        color=color_passive
                                        print(bcolors.OKGREEN +'You got the letter "', user_text , '" Right ! on ',len(pos)," position(s)" +bcolors.ENDC)
                                        dispay = hang.fillDisplay(display,user_text,pos)
                                        print(display)
                            else:
                                        life=life-1
                                        text='Wrong letter , lifes left: '+str(life)
                                        color=color_active
                                        print(bcolors.FAIL+'Wrong letter , lifes left: '+bcolors.ENDC,life)
                                        print(display)
                                        
                            if hang.checkEnd(display)==True:
                                        text='Game Concluded , YOU WON ! '
                                        print(bcolors.WARNING+'Game Concluded , YOU WON ! '+bcolors.ENDC)
                                        
                        else:
                                text='No no no , only 1 letter at a time'
                                print(bcolors.FAIL+'No no no , only 1 letter at a time'+bcolors.ENDC)
                        
                        pygame.draw.rect(screen, color, input_rect)
                        text_surface = base_font.render(text, True, (255, 255, 255))
                        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                        pygame.display.flip()
                        user_text=''
                        hanged_image_handler.display_state(life,screen)
    else:
            end_rec = pygame.Rect(150, 100, 0, 32)    
            base_font = pygame.font.Font(None, 62) 
            pygame.draw.rect(screen, 'white', end_rec)
            text_surface = base_font.render('GAME OVER ! YOU LOST', True, (255, 255, 255))
            screen.blit(text_surface, (end_rec.x+5, end_rec.y+5))
            pygame.display.flip()
            sleep(3)
            break
            

                            
    


        


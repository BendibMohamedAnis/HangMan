from operator import truediv
import turtle
import sys
from time import sleep


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


def fillDisplay(display,letter,pos):
    for i in range(len(pos)):
            display[pos[i]]=str('[ ')+str(letter)+str(' ] ')
            i=i+1
    return display
        


def exist(letter,word):
    pos = []
    res = False
    for i in range(len(word)):
        if word[i]==letter:
            res=True
            pos.append(i)
    return res,pos

def checkEnd(display):
    state = True
    for i in range(len(display)):
        if display[i]==" [ _ ] ":
            state=False
    return state       
            

        

if __name__ == "__main__":

    word="Test"
    life=8
    display=[None] * len(word)

    for i in range(len(word)):
        display[i]=" [ _ ] "
    
    while True:
        if life>0:
            res=False
            pos=[]
            guess=input(bcolors.HEADER+" GUESS ONE LETTER: "+bcolors.ENDC )
            if len(guess)==1:
                res,pos=exist(guess,word)
                
                if res:
                    print(bcolors.OKGREEN +'You got the letter "', guess , '" Right ! on ',len(pos)," position(s)" +bcolors.ENDC)
                    dispay = fillDisplay(display,guess,pos)
                    print(display)
                else:
                    life=life-1
                    print(bcolors.FAIL+'Wrong letter , lifes left: '+bcolors.ENDC,life)
                    print(display)

                if checkEnd(display)==True:
                    print(bcolors.WARNING+'Game Concluded , YOU WON ! '+bcolors.ENDC)
                    break
            else:
                print(bcolors.FAIL+'No no no , only 1 letter at a time'+bcolors.ENDC)
        else:
            print(bcolors.WARNING+'Game Ended , You lost!'+bcolors.ENDC)
            break
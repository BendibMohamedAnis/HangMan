from operator import truediv
import turtle
import sys
from time import sleep
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
            guess=input(" GUESS ONE LETTER: ")
            if len(guess)==1:
                res,pos=exist(guess,word)
                
                if res:
                    print('You got the letter "', guess , '" Right ! on ',len(pos)," position(s)" )
                    dispay = fillDisplay(display,guess,pos)
                    print(display)
                else:
                    life=life-1
                    print('Wrong letter , lifes left: ',life)
                    print(display)

                if checkEnd(display)==True:
                    print('Game Concluded , YOU WON ! ')
                    break
            else:
                print('No no no , only 1 letter at a time')
        else:
            print('Game Ended , You lost!')
            break
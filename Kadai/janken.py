#hand = 0 : Rock, 1 : Scissors, 2 : Paper
import random
from random import randrange

def janken(A,B):

    Ahand = randrange(3)
    Bhand = randrange(3)

    Awin = False
    Bwin = False

    if Ahand == 0:
        if Bhand == 1:
            Awin = True
        elif Bhand == 2:
            Bwin = True
        else:
            pass
    elif Ahand == 1:
        if Bhand == 0:
            Bwin = True
        elif Bhand == 2:
            Awin = True
        else:
            pass
    else:
        if Bhand == 0:
            Awin = True
        elif Bhand == 1:
            Bwin = True
        else:
            pass

    if Awin:
        print("AHand : ",hand(Ahand),"BHand : ",hand(Bhand)," Awin!")
        A += 1
        if A < 2:
            janken(A,B)
        else:
            print("Finish Awin!")
    elif Bwin:
        print("AHand : ",hand(Ahand),"BHand : ",hand(Bhand)," BWin!")
        B += 1
        if B < 2:
            janken(A,B)
        else:
            print("Finish Bwin!")
    else:
        print("AHand : ",hand(Ahand),"BHand : ",hand(Bhand)," Drow!")
        janken(A,B)
    
    return

def hand(h):
    if h == 0:
        return "Rock"
    elif h == 1:
        return "Scissors"
    else:
        return "Paper"
    
janken(0,0)

#RPS.py | a program that plays rock-paper-scissors
from random import randint

compList = ['r','p','s'] # list of possible moves for the comp
returnTable = {'r':'p', 'p':'s', 's':'r'} # a 'bias-list', returns the opposite of a move
pScore = 0
cScore = 0

def playMove():
    # Collects and checks the players move to ensure it's correct
    while True:
        move = input("Play (R)ock, (P)aper, or (S)cissors: ")

        if move.lower() == 'r' or move.lower() == 'p' or move.lower() == 's':
            break
        else:
            print("Write only the first letter of what you want play")
    print()
    return move


def compMove():
    # Decides the computer's move
    global compList

    return compList[randint(0, len(compList) - 1)]


def decideWinner():
    # Decides the winner for the round and adds bias to the computer
    global MOVE, cMOVE, pScore, cScore, compList
    
    if MOVE == cMOVE:
        print("It's a draw!\n\n")
        # The computer stores what the player played and is more likely to play
        # the opposite of what the player plays, i.e, predicting the player's move        
        compList += returnTable[MOVE]  

    elif (MOVE == 'r' and cMOVE == 's') or (MOVE == 's' and cMOVE == 'p') or (MOVE == 'p' and cMOVE == 'r'):
        print("The player wins!\n\n")
        pScore += 1
        compList += returnTable[MOVE]

    else:
        print("The computer wins!\n\n")
        cScore += 1
        compList += returnTable[MOVE]
        
gameOver = False

while not gameOver:
    # Game loop
    print("SCORE:", pScore, "-", cScore, '\n')
    MOVE = playMove()
    cMOVE = compMove()
    
    print("The computer plays:", cMOVE)

    decideWinner()

    if pScore == 5:
        print("~/The player wins the game!\~")
        gameOver = True
    elif cScore == 5:
        print("\~The computer wins the game!~/")
        gameOver = True
        



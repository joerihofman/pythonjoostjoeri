from random import randint
BOARD_SIZE = 4
NR_GUESSES = 0
turn = 4

userXList = []
userYList = []
checklist = [0,1,2,3]

#initializing board
board = []

for x in range(BOARD_SIZE):
    board.append(["O"] * BOARD_SIZE)

def print_board(board):
    for row in board:
        print (" ".join(row))


#start the game and printing the board
print ("Let's play Battleship!")
print_board(board)

#define where the ship is
ship_row = randint(0, BOARD_SIZE-1)
ship_col = randint(0, BOARD_SIZE-1)
print(ship_row)
print(ship_col)

"""
here your code :
*-ask the user for a guess
*-warn if the guess is out of the board
-warn if the guess was already made > Gebruik functie intersect in een lijst met alle die al geweest zijn.
-if the guess is wrong, mark the point with an X and start again
*-print turn and board again here
*-if the user's right, the game ends
"""
#User input

def userRow ():
    try:
        userx = int(input('Welke plek in de rij? (0 tot 4)'))
    except ValueError:
        print("Voer een getal in!")
        userRow()
    global checklist
    if not userx in checklist:
        print("Getal niet tussen 0 en 4!")
        userRow()
    else:
        global userXList
        #if not userXList:
        userXList.append(userx)

def userColumn ():
    try:
        usery = int(input('Welke kolom? (0 tot 4)'))
    except ValueError:
        print("Voer een getal in!")
        userColumn()
    if not usery in checklist:
        print("Getal niet tussen 0 en 4!")
        userColumn()
    else:
        global turn
        turn -= 1
        global userYList
        userYList.append(usery)

def guessedSpot():
    if turn == 3:
        #userXList[0]
        #userYList[0]
        print("Je invoer: X",userXList[0],"Y:",userYList[0])
        return(userXList[0], userYList[0])
    elif turn == 2:
        #userXList[1]
        #userYList[1]
        return(userXList[1],userYList[1])
    elif turn == 1:
        #userXList[2]
        #userYList[2]
        return(userXList[2],userYList[2])
    elif turn == 0:
        #userYList[3]
        #userXList[3]
        return(userXList[3],userYList[3])
    else:
        print('Er ging iets heel fout')


while turn > NR_GUESSES:
    userRow()
    userColumn()
    x0,x1 = guessedSpot()
    if x0==ship_row and x1==ship_col:
        print("fucking raak")
        break
    else:
        print_board(board)
        #print(guessedSpot())
        print("Beurt ",turn)
print("Game Over")
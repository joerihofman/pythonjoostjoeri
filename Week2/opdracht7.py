from random import randint
BOARD_SIZE = 4
NR_GUESSES = 4
turn = 4
userx = None
usery = None
userXList = []
userYList = []
checklist = [0,1,2,3]
userinputlist = []
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
"""
def userRow ():
    global userx
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
        userinputlist.append(userx)

def userColumn ():
    global usery
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
        global NR_GUESSES
        NR_GUESSES += 1
        global userYList
        userYList.append(usery)
        userinputlist.append(usery)

def guessedSpot():
    if turn == 3:
        print("Je invoer: X",userXList[0],"Y:",userYList[0])
        return(userXList[0], userYList[0])
    elif turn == 2:
        return(userXList[1],userYList[1])
    elif turn == 1:
        return(userXList[2],userYList[2])
    elif turn == 0:
        return(userXList[3],userYList[3])
    else:
        print('Er ging iets heel fout')

#deze functie controleerd de invoer van de gebruiker middels een lijst. niet af,checkt nu alleen de invoer waarde.

def prevturncheck():
    global userXList
    global userYList
    localx,localy = guessedSpot()
    x4 = NR_GUESSES-1
    print(localx,localy,x4,NR_GUESSES)
    print(userXList[x4],userYList[x4])
   # userXList[x4], userYList[x4]
    if localx == userXList[x4] and localy == userYList[x4] and x4 > 0:
        print("deze positie is al ingevoerd")
    for localx in userXList:
        print("plekinlijstx", userXList.index(localx))
    for localy in userYList:
        print("plekinlijsty", userYList.index(localy))

while turn > 0:
    userRow()
    userColumn()
    prevturncheck()
    localx,localy = guessedSpot()
    if localx==ship_row and localy==ship_col:
        print("fucking raak")
        break
    else:
        print_board(board)
        #print(guessedSpot())
        print("Beurt ",turn)
print("Game Over")

Deze functie controleerd de invoer van de gebruiker middels een lijst. Niet af en werkt niet helemaal.
Checkt nu alleen de ingevoerde waarde.


"""

for turn in range(NR_GUESSES):
        guessrow = int(input('..row'))
        guescolumn = int(input('..column'))

        if (guessrow == ship_row) and (guescolumn == ship_col):
            print('you won')
            break
        else:
            if((guessrow) not in range(BOARD_SIZE)) or (guescolumn not in range(BOARD_SIZE)):
                print('out of range')
            elif board[guessrow][guescolumn]=='x':
                print('you done this')
            else:
                board[guescolumn][guessrow] = 'x'
                print_board(board)
print('finished')
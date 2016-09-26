from random import randint
BOARD_SIZE = 4
NR_GUESSES = 0
turn = 4

userXList = []
userYList = []

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

"""
here your code :
*-ask the user for a guess
-warn if the guess is out of the board
-warn if the guess was already made > Gebruik functie intersect in een lijst met alle die al geweest zijn.
-if the guess is wrong, mark the point with an X and start again
-print turn and board again here
-if the user's right, the game ends
"""
#User input

def userRow ():
    try:
        userx = int(input('Welke plek in de rij? (0 tot 4)'))
    except ValueError:
        print("Voer een getal in!")
        userRow()
    global userXList
    userXList.append(userx)

def userColumn ():
    try:
        usery = int(input('Welke kolom? (0 tot 4)'))
    except ValueError:
        print("Voer een getal in!")
        userColumn()
    global turn
    turn -= 1
    global userYList
    userYList.append(usery)


while turn > NR_GUESSES:
    userRow()
    userColumn()
    print(userXList)
    print(userYList)
    print(turn)
print("Game Over")
from random import randint
BOARD_SIZE = 4
NR_GUESSES = 4

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
-if the user's right, the game ends
-warn if the guess is out of the board
-warn if the guess was already made
-if the guess is wrong, mark the point with an X and start again
-print turn and board again here
"""
#User input
def userRow (Y):
    try:
        int(input('Welke plek in de rij? (0 tot 4)'))
    except ValueError
        print("Voer een getal in!")

def userColumn (X):
    try:
        int(input('Welke kolom? (0 tot 4)'))
    except ValueError
        print("Voer een getal in!")


if turn == NR_GUESSES-1:
    print("Game Over")

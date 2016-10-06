NONE = '.'
RED = 'R'
YELLOW = 'Y'
FOUR = 4

class Game:
    def __init__ (self, cols = 7, rows = 6):
        self.cols = cols
        self.rows = rows
        self.board = [[NONE] * rows for _ in range(cols)]
        self.four_red = [RED] * FOUR
        self.four_yellow = [YELLOW] * FOUR

    def insert(self, column, color):
        c = self.board[column]
        if c[0] != NONE:
             raise Exception

        i = -1
        while c[i] != NONE:
            i -= 1
        c[i] = color

    def print_board(self):
        print(' '.join(map(str, range(self.cols))))
        for y in range(self.rows):
            print(' '.join(str(self.board[x][y]) for x in range(self.cols)))
        print()

if __name__ == '__main__':
    g = Game()
    turn = RED
    try:
        while True:
            error = False
            g.print_board()
            row = input('{}\'s turn: '.format('Red' if turn == RED else 'Yellow'))
            g.insert(int(row), turn)
            turn = YELLOW if turn == RED else RED
    except Exception:
        print("Deze kolom zit vol")
        g
"""
a) Wat is de bedoeling van de statement if __name__ == '__main__': ?


b) In de constructor staat [[NONE] * rows for _ in range(cols)]. Wat is de betekenis van de underscore '_' ?


c) Waarom moet NONE tussen [ ] ?
Dan wordt de lijst gevuld met punten

d) In insert() staat :
i = -1
while c[i] != NONE:
Waarom wordt begonnen met i = -1 ?


e) Wat is de betekent in print_board map(str, range(self.cols)) ? Hoe zou je dit ook kunnen bereiken met list
comprehension ?
Met list comprehension kan een lijst gemaakt worden door een formule tussen vierkanten haken te zetten, hier door
wordt de lijst automatisch gevuld als het programma wordt uitgevoerd
"""
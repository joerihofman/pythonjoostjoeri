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
    while True:
        error = False
        g.print_board()
        row = input('{}\'s turn: '.format('Red' if turn == RED else 'Yellow'))
        g.insert(int(row), turn)
        turn = YELLOW if turn == RED else RED

"""
a) Wat is de bedoeling van de statement if __name__ == '__main__': ?
De functie van __main__ wordt in de __name__ gezet

b) In de constructor staat [[NONE] * rows for _ in range(cols)]. Wat is de betekenis van de underscore '_' ?
Een soort weggooi variabele om aan te geven welk gedeelte van een functie negeerd wordt

c) Waarom moet NONE tussen [ ] ?


d) In insert() staat :
i = -1
while c[i] != NONE:
Waarom wordt begonnen met i = -1 ?


e) Wat is de betekent in print_board map(str, range(self.cols)) ? Hoe zou je dit ook kunnen bereiken met list
comprehension ?

"""
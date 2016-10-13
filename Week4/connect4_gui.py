from tkinter import Tk, Button, Frame, Canvas, font
 
class Board:
    def __init__(self):
        self.player = 'X'
        self.opponent = 'O'
        self.empty = '.'
        self.width = 7
        self.height = 6
        self.fields = {}
        for y in range(self.height):
            for x in range(self.width):
                self.fields[x,y] = self.empty

    def move(self,x):
        pass
    
    def won(self):
        return False

class GUI:
 
  def __init__(self):
    self.app = Tk()
    self.app.title('Connect4')
    self.app.resizable(width=False, height=False)
    self.board = Board()
    self.buttons = {}
    self.frame = Frame(self.app, borderwidth=1, relief="raised")
    self.tiles = {}
    for x in range(self.board.width):
      handler = lambda x=x: self.move(x)
      button = Button(self.app, command=handler, font=font.Font(family="Helvetica", size=14), text=x+1)
      button.grid(row=0, column=x, sticky="WE")
      self.buttons[x] = button
    self.frame.grid(row=1, column=0, columnspan=self.board.width)
    for x,y in self.board.fields:
      tile = Canvas(self.frame, width=60, height=50, bg="SkyBlue1", highlightthickness=0)
      tile.grid(row=self.board.height-1-y, column=x)
      self.tiles[x,y] = tile
    handler = lambda: self.reset()
    self.restart = Button(self.app, command=handler, text='new game')
    self.restart.grid(row=2, column=0, columnspan=self.board.width, sticky="WE")
    self.update()
 
  def reset(self):
    self.board = Board()
    self.update()
 
  def move(self,x):
    self.app.config(cursor="watch")
    self.app.update()
    self.board = self.board.move(x)
    self.update()
    move = self.board.best()
    if move!=None:
      self.board = self.board.move(move)
      self.update()
    self.app.config(cursor="")
 
  def update(self):
    for (x,y) in self.board.fields:
      text = self.board.fields[x,y]
      if (text=='.'):
        self.tiles[x,y].create_oval(10, 5, 50, 45, fill="gray", width=1)
      if (text=='X'):
        self.tiles[x,y].create_oval(10, 5, 50, 45, fill="yellow", width=1)
      if (text=='O'):
        self.tiles[x,y].create_oval(10, 5, 50, 45, fill="red", width=1)
    for x in range(self.board.width):
      if self.board.fields[x,self.board.height-1]==self.board.empty:
        self.buttons[x]['state'] = 'normal'
      else:
        self.buttons[x]['state'] = 'disabled'
    winning = self.board.won()
    if winning:
      for x,y in winning:
        self.tiles[x,y].create_oval(25, 20, 35, 30, fill="gray")
      for x in range(self.board.width):
        self.buttons[x]['state'] = 'disabled'
 
  def mainloop(self):
    self.app.mainloop()
 
if __name__ == '__main__':
  GUI().mainloop()
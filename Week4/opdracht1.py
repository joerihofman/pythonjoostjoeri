"""

a) Bekijk de code. Op regel 22 staat een global-statement. Is deze wel noodzakelijk? Motiveer je antwoord
Ja, anders worden verschillende variabelen gebruikt

b) De code is niet erg mooi. Vorm de code om in een maak een class Plot met constructor en een functie step().


c) Voeg bij de horizontale en verticale as labels toe, bijvoorbeeld "step" en "value".


d) Voeg een pauzeknop toe, zodat je het plotten even kan stoppen.
e) Voeg twee velden "max" en "min" met een "set"-knop toe, waarmee de gebruiker kan aangeven waartussen
de y-waarden kunnen variëren (dus 0 <= min_value < value < max_value <= 100). Teken ook twee horizontale
lijnen die deze grenzen aangeven.
f) Demonstreer het resultaat aan de docent

"""
from tkinter import*
from random import randint
import time

def value_to_y(val):
    return 550-5*val

s = 1
x2 = 50
y2 = value_to_y(randint(0,100))

class Plot:
    def __init__(self):
        self.root = Tk()
        self.root.title('Simple Plot')
        self.canvas = Canvas(Tk(), width=1200, height=600, bg='white')#0,0 =topleftcorner
        self.canvas.pack(expand=YES, fill=BOTH)
        Button(self.root, text='Quit', command=self.root.quit).pack()
        self.canvas.create_line(50,550,1150,550, width=2)
        self.canvas.create_line(50,550,50,50, width=2)
        for i in range(23): #x-axis
            x = 50+(i*50)
            self.canvas.create_line(x, 550, x, 50, width=1, dash=(2, 5))
            self.canvas.create_text(x, 550, text='%d' % (10 * i), anchor=N)
        for i in range(11):
            y = 550 - (i * 50)
            self.canvas.create_line(50, y, 1150, y, width=1, dash=(2, 5))
            self.canvas.create_text(40, y, text='%d' % (10 * i), anchor=E)



    def step(self):
        global s, x2, y2
        if s == 23:
            # new frame
            s = 1
            x2 = 50
            self.canvas.delete('temp')  # only delete items tagged as temp
        x1 = x2
        y1 = y2
        x2 = 50 + s * 50
        y2 = value_to_y(randint(0, 100))
        self.canvas.create_line(x1, y1, x2, y2, fill='blue', tags='temp')
        # print(s, x1, y1, x2, y2)
        s = s + 1


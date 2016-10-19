from tkinter import *
from random import randint
from Week4.opdracht1 import Plot
import time

plot = Plot()

canvas = Canvas(root, width=1200, height=600, bg='white') # 0,0 is top left corner
canvas.pack(expand=YES, fill=BOTH)

Button(root, text='Quit', command=root.quit).pack()

canvas.create_line(50,550,1150,550, width=2) # x-axis
canvas.create_line(50,550,50,50, width=2)    # y-axis

# x-axis
for i in range(23):
    x = 50 + (i * 50)
    canvas.create_line(x,550,x,50, width=1, dash=(2,5))
    canvas.create_text(x,550, text='%d'% (10*i), anchor=N)
    
# y-axis
for i in range(11):
    y = 550 - (i * 50)
    canvas.create_line(50,y,1150,y, width=1, dash=(2,5))
    canvas.create_text(40,y, text='%d'% (10*i), anchor=E)

canvas.after(300, step) 
root.mainloop()

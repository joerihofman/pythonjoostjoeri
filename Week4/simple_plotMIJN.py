from tkinter import *
from random import randint
from Week4.opdracht1 import Plot
import time

plot = Plot


plot.canvas.after(300, plot.step())
plot.root.mainloop()

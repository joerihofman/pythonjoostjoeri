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

class Plot:
    def __init__(self):
        self.canvas =

    def step(self):
        global s, x2, y2
        if s == 23:
            # new frame
            s = 1
            x2 = 50
            canvas.delete('temp')  # only delete items tagged as temp
        x1 = x2
        y1 = y2
        x2 = 50 + s * 50
        y2 = value_to_y(randint(0, 100))
        canvas.create_line(x1, y1, x2, y2, fill='blue', tags='temp')
        # print(s, x1, y1, x2, y2)
        s = s + 1
        canvas.after(300, step)
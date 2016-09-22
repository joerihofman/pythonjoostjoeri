#OPGAVE 2 : DICTIONARY UPDATES
#Gegeven dictionary
d = {"red":4, "blue":1, "green":14, "yellow":2}
#Wat is de waarde van d na de volgende
#statements (waarbij d na elke statement weer is als aan het begin).

#a) d['red'] = d['blue']
#de waardes van d zijn: ['yellow': 2, 'blue': 1, 'red': 1, 'green':14]

#b) d['blue'] += 10
#de uitkomst van d is: ['blue':11, 'yellow':2, 'red':4, 'green':14]]

#c) d['yellow'] = len(d)
#de uitkomst is: ['yellow': 4, 'blue': 1, 'green': 14, 'red': 4]

#d) d['green'] = {'orange' : 6}
#de dictionary is nu: {'blue': 1, 'green': {'orange: 6}, 'red': 4, 'yellow': 2}

#e)d = dict(zip(d.keys(), d.values()))
#de uitkomst is: {'blue': 1, 'yellow': 2, 'red': 4, 'green': 14}

#g) d.pop('black', None)
#de dictionary is nu: {'red': 4, 'green': 14, 'yellow': 2, 'blue': 1}

#h) d.get('black', None)
#de uitkomst is: {'green': 14, 'yellow': 2, 'blue': 1, 'red': 4}

#i)d.setdefault('black', None)
#uitkomst: {'green': 14, 'blue': 1, 'red': 4, 'yellow': 2, 'black': None}

#j)d = {k : 0 for k in d.keys()}
#uitkomst: {'yellow': 0, 'red': 0, 'blue': 0, 'green': 0}

#f)d = dict.fromkeys(d, 0)
#uitkomst: {'yellow':0,'blue':0,'red':0,'green':0}

#k)d = {}
#uitkomst: {}

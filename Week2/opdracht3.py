#OPGAVE 3 : TWEE DICTIONARY OPGAVEN
#a) Gegeven een dictionary
d = {'red':'#FF0000',
     'green':'#008000',
     'black':'#000000',
     'white':'#FFFFFF'}
# Schrijf een programma dat d sorteert op key. Dus d wordt afgedrukt als 'black':'#000000', 'green':'#008000','red':'#FF0000', 'white':'#FFFFFF'.
x = sorted(d.items())
x
print(x)


#b) Gegeven
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
#Schrijf een programma dat d1 en d2 samenvoegt tot {'x': 300, 'y': 200, 'a': 100, 'b': 200}.
d3 = {**d1, **d2}
print(d3)
#uitkomst is x,a,y,b....!
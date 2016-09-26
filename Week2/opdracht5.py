#OPGAVE 5 : FUNCTIES
#Geef voor onderstaande programma's aan wat er wordt afgedrukt.
#A

#def function1(n, m):
#    function2(3.4)

#function1(2, 3)

#def function2(n):
#    if n > 0:
#         return 1
#    elif n == 0:
#         return 0
#    elif n < 0:
#         return -1

#OUTPUT: Functie 2 bestaat niet omdat die eerder wordt aangeroepen dan gederclareerd, er komt dus een foutmelding

#B
#def main():
#    print(min('Jan', 'jan'))
#def min(n1, n2):
#     smallest = n1
#     if n2 < smallest:
#        smallest = n2
#main()

#OUTPUT: None. Dit komt, denken wij, omdat je strings niet kan vergelijken, of omdat ze even groot zijn. Daarnaast wordt smallest niet gebruikt in de een na laatste regel.

#C
def intersect(seq1, seq2):
    res = set()
    for x in seq1:
        if x in seq2:
            res.add(x)
    return res
print(intersect('beer', 'burger'))
print(intersect((1,2,3,4),(1,4,2,5)))
#OUTPUT: met de functie intersect worden karakters en cijfers met elkaar vergeleken. Degene die overeenkomen worden geprint.

#D
#v = 42
#def do():
#    v = 0
#    v += 1
#    print (v)
#def da():
#    global v
#    v += 1
#    print (v)
#do()
#da()
#print(v)
#OUTPUT: In 'do' wordt een variabele gebruikt die alleen bekend is binnen de functie, daar wordt 1 bijop getelt. In 'da' wordt de v=42 gelezen van buiten de functie en daar wordt 1 bij op getelt.
#Met print(v) wordt de v die door functie da is gegaan gelezen, dus is het geen 42 maar 43.

#E
"""
def make(N):
    return lambda x: x**N
square = make(2)
cube = make(3)
hyper = make(4)

print(square(3))
print(cube(3))
print(hyper(3))
"""
#DEZE
#MOET
#NOG
#
#
#
#
#
##
#
#
#
#
#
###
#
#
#
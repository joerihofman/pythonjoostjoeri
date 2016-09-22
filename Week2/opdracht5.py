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
def main():
    print(min('Jan', 'jan'))
def min(n1, n2):
     smallest = n1
     if n2 < smallest:
         smallest = n2
main()

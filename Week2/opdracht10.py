cnummer = None

def userinput():
    try:
        invoer = int(input('Wat is je creditcard nummer?'))
    except ValueError:
        print("Voer een getal in!")
        userinput()
    if not (15 < len(str(invoer)) < 17):
        print("Voer een getal in van 16 cijfers!")
        userinput()
    else:
        global cnummer
        cnummer = invoer

def nummers(number):
    return list(map(int, str(number)))

def luhn_check(kaart_nummer):
    digits = nummers(kaart_nummer)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(nummers(2 * digit))
    return total % 10

def bereken(gedeeltelijkNummer):
    check_getal = luhn_check(int(gedeeltelijkNummer) * 10)
    return check_getal if check_getal == 0 else 10-check_getal

userinput()
if luhn_check(cnummer) == 0:
    print("dit nummer is geldig")
else:
    print("dit nummer is ongeldig")

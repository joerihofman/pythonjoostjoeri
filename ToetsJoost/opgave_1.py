# convert an integer to a hex digit (a character)
hexnumber = []

def hex_char(value):
    if value <= 9 and value >= 0:
        return chr(value + ord('0'))
    else:
        return chr(value - 10 + ord('A'))

# convert a decimal to a hex as a string 
def to_hex(decimal):
    global hexnumber
    while decimal > 0:
        if decimal > 15:
            hexnumber.append('F')
            decimal -= 15
        else:
            hexnumber.append(hex_char(decimal))
            decimal -=decimal

    return hexnumber


def main():
    global hexnumber
    var = int(input('Voer een integer waarde in'))
    to_hex(var)
    print(str(hexnumber).strip('[]'))


    #assert to_hex(12345) == '3039', 'functie werkt'
    #assert to_hex(0) == '0', 'niet ok'

main()

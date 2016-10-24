# convert an integer to a hex digit (a character)
def hex_char(value):
    if value <= 9 and value >= 0:
        return chr(value + ord('0'))
    else:
        return chr(value - 10 + ord('A'))

# convert a decimal to a hex as a string 
def to_hex(decimal):
    hex_char(decimal)

def main():
    getal = int(input('Wat is het getal?: '))
    print(to_hex(getal))
    #assert to_hex(12345) == '3039', 'Error'
    #assert to_hex(0) == '0', 'Error'
    #assert to_hex(10) == 'A', 'Error'
    #assert to_hex(20) == '14', 'Error'
    #assert to_hex(255) == 'FF', 'Error'

main()

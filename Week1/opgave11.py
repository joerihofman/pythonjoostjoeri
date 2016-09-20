gegevens = open('station_vl.txt', 'r')
regels = []

for regel in gegevens:
    if regel[0].isdigit():
        regels.append(regel)

print(regels)
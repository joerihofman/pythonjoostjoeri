gegevens = open('station_vl.txt', 'r')
regels = []

for regel in gegevens:
    if regel[0].isdigit():
        split = regel.split()
        #dag = int(split[0])
        #uur = int(split[1])
        temp = int(split[2])
        regels.append(regel)
    #while len(regels)<dag:
    #    regels.append(regel)
    #    regels[dag-1].append(temp)

print(regels)
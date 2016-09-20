gegevens = open('station_vl.txt', 'r')
regels = []

for regel in gegevens:
    if regel[0].isdigit():
        split = regel.split()
        dag = int(split[0][:1])
        #uur = int(split[1])
        temp = int(split[2])
        regels.append(regel)
    #while len(regels)<dag:
    #    regels.append(regel)
    #    regels[dag-1].append(temp)
for dag in regels:
    for temp in regels:
        temp += temp
    print('dag:', dag, ' temperatuur:', temp)

#print(regels)
gegevens = open('station_vl.txt', 'r')
# print(gegevens.readline())

for line in gegevens:
    segmentedLine = line.split("\t")
    print(segmentedLine)
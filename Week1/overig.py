text = 'ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCT' \
       'CCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCC' \
       'CACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAA' \
       'GGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGA' \
       'CCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGA' \
       'GGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCC' \
       'GGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCT' \
       'GCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA'  # text = genstring

list1 = []
index = 0

while index < len(text):  # zoek de locatie van 'TAG' zolang de index < lengte s2
    index = text.find('ATG', index)  # index is de locatie van 'TAG'
    if index == -1:  # Als er geen 'ATG' invoor komt stopt de loep
        break

    begin = text.find('ATG', 0)
    list1.append(text.find('TAA', index + 3))
    list1.append(text.find('TAG', index + 3))
    list1.append(text.find('TGA', index + 3))
    list1.sort()

    for end in list1:
        if end > 0:
            break
        else:
            end = -1
    if end == -1:
        break
    list1 = []
    sub = text[index + 3:end]
    rest = len(sub) % 3
    if rest > 0:
        sub = sub[0:len(sub) - rest]
    while True:
        if 'ATG' in sub:
            sub = sub.replace('ATG', '')
        elif 'TGA' in sub:
            sub = sub.replace('TGA', '')
        elif 'TAG' in sub:
            sub = sub.replace('TAG', '')
        elif 'TAA' in sub:
            sub = sub.replace('TAA', '')
        else:
            break
    print(sub)
    index = index + end

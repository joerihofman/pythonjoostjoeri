L1,L2 = [1,5,16,61,111], [2,4,5,6]
L3 = L1+L2

L4 = []

while L3:
    minimum = L3[0]  # arbitrary number in List
    for x in L3:
        if x < minimum:
            minimum = x
    L4.append(minimum)
    L3.remove(minimum)

print(L4)
students = { 0: "Nynke", 1: "Lolle", 2: "Jikke", 3: "Popke", 4: "Teake",
             5: "Lieuwe", 6: "Tsjabbe", 7: "Klaske", 8: "Ypke", 9: "Lobke"}

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5),
               (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#lijstVrienden = []
#for index in students:
#    lijstVrienden.append(index)
#print(lijstVrienden)
lengte = len(students)
i = 0
vrienden = []

while i < lengte:
    vrienden.append([])
    friends = 0
    for n in friendships:
        if n[0] == i:
            vrienden[i].append(n[1])
        elif n[1] == i:
            vrienden[i].append(n[0])
    i += 1
print(vrienden)


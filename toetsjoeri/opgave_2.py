test = ''
with open('message.txt', 'r') as f:
    test = f.read()


found = 0
start = -1
begin = '0000'
eind = '1111'
bericht = ''
#Bericht % 2

for i in range(len(test) - 3):
    x = 0
    if i[x] == begin:
        split = i.split()
        letters = []
        letters.append(i)
        print(letters)
        found += 1
        x =+ 1
        if i[x] == eind and i%2==0:
            break

if test == begin:
    print(test)

#if bericht%2==0:
#    pass
#else:
#    pass

print('aantal 0', test.count(begin))

if not found:
    print("No message was found")
else:
    print("%s messages were found" % found)

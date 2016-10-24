test = ''
with open('message.txt', 'r') as f:
    test = f.read()


found = 0
start = -1
zero = '0000'
one = '1111'
var0 = 1

for i in range(len(test) - 3):
    if str.count(zero) == var0 and str.count(one) == var0:
        found += 1
        var0 +=1

    else:
        print('hier gaat iets fout')

    
if not found:
    print("No message was found")
else:
    print("%s messages were found" % found)

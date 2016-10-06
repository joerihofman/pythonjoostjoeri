
try:
    lst = 10 * [0]
    x = lst[10]
    print("Done ")
except IndexError:
    print("Index out of bound")
else:
    print("Nothing is wrong")
finally:
    print("Finally we are here")

print("Continue")

#a) Wat wordt afgedrukt door het onderstaande programma ?
#Done
#Nothing is wrong
#Finally we are hele
#Continue

#b En wat wordt afgedrukt als lst[9] verandert in lst[10] ?
#Nothing is wrong wordt niet afgedrukt

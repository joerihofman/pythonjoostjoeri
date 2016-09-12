L = [2, 3, 5, 2, 33, 21];
#a
print(L[1:-3])
#result: [3, 5]

#b
print(L[-4:-2])
#result: [5,2]

#c
print(L[:2] + L[2:])
#result: [2, 3, 5, 2, 33, 21]

#d
print(L[42:])
#result: []



#It's pretty simple really:

#a[start:end] # items start through end-1
#a[start:]    # items start through the rest of the array
#a[:end]      # items from the beginning through end-1
#a[:]         # a copy of the whole array
#There is also the step value, which can be used with any of the above:

#a[start:end:step] # start through not past end, by step
#The key point to remember is that the :end value represents the first value that is not in the selected slice. So, the difference beween end and start is the number of elements selected (if step is 1, the default).

#The other feature is that start or end may be a negative number, which means it counts from the end of the array instead of the beginning. So:

#a[-1]    # last item in the array
#a[-2:]   # last two items in the array
#a[:-2]   # everything except the last two items
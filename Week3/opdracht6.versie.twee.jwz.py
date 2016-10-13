from sys import exit
from itertools import chain
import numpy as np

#matrix = np.arange(9).reshape(3, 3)

matrix = np.array([[1,2,3],
                   [4,3,5],
                   [3,6,7]]
                 )
def column(matrix, i):
    return [row[i] for row in matrix]

matrix.tolist()
posdiag = [list(np.diagonal(matrix, i)) for i in range(-2,3)]
negdiag = [list(np.diagonal(matrix, i)) for i in range(2,-3)]
rows = [list(matrix) for i in range(-2, 3)]
cols = [list(column(matrix, i)) for i in range(-2, 3)]
n = 3
c = (rows, cols, posdiag, negdiag)
for lst in chain(*c):
    for i in range(len(lst)-n+1):
        None

print(matrix)

"""
.cseg:
word > int = word, dus dw
db = bytes dus 8d wordt d: gb 'comp9032'
"""
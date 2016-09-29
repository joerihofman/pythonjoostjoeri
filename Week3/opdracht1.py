"""
A:
class A:
    def __init__(self, i = 0):
        self.i = i
    def m1(self):
        self.i += 1
class B(A):
    def __init__(self, j = 0):
        super().__init__(3)
        self.j = j
    def m1(self):
        self.i += 1

def main():
    b = B()
    print(b.i, b.j)
    b.m1()
    print(b.i, b.j)

main()
"""
#output: 3 0
#        4 0

class A:
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return "I am class A"

class B(A):
    def __init__(self, i, j):
        super().__init__(i)
        self.j = j
    def __str__(self):
        return "I am class B"

def main():
    a = A(1)
    b = B(1, 2)
    print(a)
    print(b)
    print(a.__dict__)
    print(b.__dict__)
main()

"""
OUTPUT:
I am class A
I am class B
{'i': 1}
{'j': 2, 'i': 1}
"""
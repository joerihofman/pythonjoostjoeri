class Stack:
    def __init__(self, stack = None):
        if stack is None:
            self.stack = []
        else:
            self.stack = stack

    def is_empty(self):
        if not self:
            return True
        else: return False

    def peek(self):
        if self:
            return len(self)
        else:
            print("Er zit niks in de lijst")

    def push(self, val):
        self.append(val)

    def pop(self):

        return self[-len(self)]

    def getSize(self):
        return len(self)

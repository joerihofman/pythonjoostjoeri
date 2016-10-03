class Stack:
    def __init__(self, stack = None):
        if stack is None:
            self.stack = []
        else:
            self.stack = stack

    def is_empty(stack):
        if not stack:
            return True
        else: return False

    def peek(stack):
        if stack:
            return stack[-len(stack)]
        else: print("Er zit niks in de lijst")

    def push(stack, val, obj):
        stack.append(val, obj)

    def pop(stack):

        return stack[-len(stack)]

    def getSize(stack):
        return len(stack)

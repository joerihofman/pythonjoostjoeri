from Week3.stack import Stack

stack = Stack()

for i in range(10):
     stack.push(i)

while not stack.is_empty():
     print(stack.pop(), end = " ")


"""
De Stack class maakt het mogelijk om objecten in een stapel te bewaren en biedt operaties om de stack te
bewerken. De class Stack bevat het volgende :

fields         elements: list
                    (private)       list to store the elements in the stack
me   thods
constructor              creates an empty stack
is_empty(): bool         returns True if the stack is empty
peek(): object           returns the element at the top of the stack without
                            removing it from the stack
push(value: object): None    stores an element at the top of the stack
pop(): object                removes the element at the top of the stack and returns it
getSize(): int               returns the number of elements in the stack

"""
from typing import Any, Optional

class Node:
    def __init__(self, value):
        self.value = value 
        self.next: Optional["Node"] = None

class Stack:
    def __init__(self):
        self.top: Optional["Node"] = None
        self.size = 0

    def push(self, value):
        """Adds an item to the top of the stack in O(1) time."""
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """Removes and returns the top item in O(1) time."""
        if self.top is None:
            raise IndexError("Pop from a empty stack")
        
        popped_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return popped_value
    
    def peek(self):
        """Returns the top item without removing it."""
        if self.top is None:
            raise IndexError("Peek from empty stack")

        return self.top.value

    def display(self):
        elems = []
        this_node = self.top
        
        while this_node is not None:
            elems.append(this_node.value)
            this_node = this_node.next

        return elems

    
myStack = Stack()



myStack.push("Behnam")
myStack.push("Bahar")
myStack.push(10)
myStack.push(12)

print(myStack.display())

print(myStack.peek())
print(myStack.pop())

print(myStack.display())
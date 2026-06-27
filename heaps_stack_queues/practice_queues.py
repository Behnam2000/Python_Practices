from typing import Any, Optional

class Node:
    def __init__(self, value):
        self.value = value 
        self.next: Optional["Node"] = None

class Queue:
    def __init__(self):
        self.head: Optional["Node"] = None
        self.tail: Optional["Node"] = None
        self.size = 0

    def enqueue(self, value):
        """Adds an item to the back of the queue in O(1) time."""
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        
        elif self.tail is not None:
            self.tail.next = new_node
            self.tail = new_node
            
        self.size += 1

    def dequeue(self):
        """Removes and returns the front item in O(1) time."""
        if self.head is None:
            raise IndexError("Pop from a empty stack")
        
        dequeue_value = self.head.value
        self.head = self.head.next
        self.size -= 1
        
        # If the queue is now empty, ensure the tail is also reset
        if self.head is None:
            self.tail = None

        return dequeue_value
    

    def display(self):
        elems = []
        this_node = self.head
        
        while this_node is not None:
            elems.append(this_node.value)
            this_node = this_node.next

        return elems

    
myQueue = Queue()

myQueue.enqueue("Behnam")
myQueue.enqueue("Bahar")
myQueue.enqueue(10)
myQueue.enqueue(12)

print(myQueue.display())

print(myQueue.dequeue())

print(myQueue.display())
class Node:
	def __init__(self, data, node=None):
        
	    self.data = data
	    self.next_node = node


	def get_next(self):
	    return self.next_node

	def set_next(self, node):
	    self.next_node = node

	def get_data(self):
	    return self.data


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self) -> int:
        return self.size

    # Challenge 1: Prepend (Add to the front)
    def prepend(self, data) -> None:
        new_node = Node(data)
        
        if self.head is None:
            # Point the node to itself to create the initial circle!
            new_node.set_next(new_node)
            self.head = new_node
        else:
            # TODO Step A: Find the last node (the tail) that currently points to self.head
            # Hint: Keep going until node.get_next() == self.head
            tail = self.head
            while tail.get_next() != self.head:
                tail = tail.get_next()
                
            # TODO Step B: Point the new_node's 'next' to the current head
            new_node.set_next(self.head)
            
            # TODO Step C: Point the tail's 'next' to the new_node
            tail.set_next(new_node)
            
            # TODO Step D: Reassign self.head to be the new_node
            self.head = new_node 
            
        self.size += 1

    # Challenge 2: Append (Add to the back)
    def append(self, data) -> None:
        new_node = Node(data)
        
        if self.head is None:
            new_node.set_next(new_node)
            self.head = new_node
        else:
            # TODO Step A: Find the last node (the tail)
            tail = self.head
            while tail.get_next() != self.head:
                tail = tail.get_next()
                
            # TODO Step B: Point the tail's 'next' to the new_node
            tail.set_next(new_node)
            
            # TODO Step C: Point the new_node's 'next' back to self.head (to complete the loop)
            new_node.set_next(self.head)
            
        self.size += 1

    # Helper method to display the circular elements safely
    def display(self) -> list:
        if self.head is None:
            return []
            
        elements = []
        this_node = self.head
        
        while True:
            elements.append(this_node.get_data())
            this_node = this_node.get_next()
            if this_node == self.head:
                break
                
        return elements


# --- Test Space ---
cll = CircularLinkedList()

# Once implemented, testing prepend and append should output loops correctly:
cll.append(10)
cll.append(20)
cll.prepend(5)
print(cll.display()) # Expected: [5, 10, 20]
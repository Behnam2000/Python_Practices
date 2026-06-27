class DLLNode:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node

    def get_prev(self):
        return self.prev_node

    def set_prev(self, node):
        self.prev_node = node

    def get_data(self):
        return self.data


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self) -> int:
        return self.size

    # Challenge 1: Prepend (Insert at the Front)
    def prepend(self, data) -> None:
        new_node = DLLNode(data)
        
        if self.head is None:
            # Self-pointing loop in both directions
            new_node.set_next(new_node)
            new_node.set_prev(new_node)
            self.head = new_node
        else:
            # Get the tail instantly without any loops!
            tail = self.head.get_prev()
            
            # TODO: Point new_node's 'next' to the current head
            new_node.set_next(self.head)
            
            # TODO: Point new_node's 'prev' to the tail
            new_node.set_prev(tail)
            
            # TODO: Point the current head's 'prev' back to the new_node
            self.head.set_prev(new_node)
            
            # TODO: Point the tail's 'next' forward to the new_node
            tail.set_next(new_node)
            
            # TODO: Move self.head to the new_node
            self.head = new_node
            
        self.size += 1

    # Challenge 2: Append (Insert at the Back)
    def append(self, data) -> None:
        new_node = DLLNode(data)
        
        if self.head is None:
            new_node.set_next(new_node)
            new_node.set_prev(new_node)
            self.head = new_node
        else:
            # Get the tail
            tail = self.head.get_prev()
            
            # TODO: Connect the new_node to head (next) and tail (prev)
            new_node.set_next(self.head)
            new_node.set_prev(tail)
            
            # TODO: Connect head's 'prev' and tail's 'next' to the new_node
            self.head.set_prev(new_node)
            self.head.set_next(new_node)
            
            # Note: Do NOT change self.head here!
            
        self.size += 1

    def display_forward(self) -> list:
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

    def display_backward(self) -> list:
        if self.head is None:
            return []
            
        elements = []
        # Tail is instantly head's previous node!
        this_node = self.head.get_prev()
        while True:
            elements.append(this_node.get_data())
            this_node = this_node.get_prev()
            # Stop when we wrap back around past the tail to the start of backward traversal
            if this_node == self.head.get_prev():
                break
        return elements


# --- Test Space ---
cdll = CircularDoublyLinkedList()

# Once implemented, tests should produce clean loops in both directions:
cdll.append(20)
cdll.append(30)
cdll.prepend(10)
print("Forward: ", cdll.display_forward())  # Expected: [10, 20, 30]
print("Backward:", cdll.display_backward()) # Expected: [30, 20, 10]
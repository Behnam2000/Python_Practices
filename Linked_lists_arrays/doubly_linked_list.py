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

    def set_data(self, data):
        self.data = data


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self) -> int:
        return self.size

    # 1. Prepend: Adds to the very front of the list
    def prepend(self, data) -> None:
        new_node = DLLNode(data)
        
        if self.head is None:
            # If empty, this new node is both the head and the tail
            self.head = new_node
            self.tail = new_node
        else:
            # Link new node to the current head
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            # Make the new node the new head
            self.head = new_node
            
        self.size += 1

    # 2. Append: Adds to the very back of the list (Challenge!)
    def append(self, data) -> None:
        new_node = DLLNode(data)
        
        if self.head is None:
            # If empty, treat it exactly like prepend
            self.head = new_node
            self.tail = new_node
        else:
            # TODO: Link the current tail to the new_node
            self.tail.set_next(new_node)
            # TODO: Link the new_node back to the current tail
            new_node.set_prev(self.tail)
            # TODO: Update the list's tail pointer to be this new node
            self.tail.set_next(new_node)
            
            
        self.size += 1

    # 3. Remove: Deletes a node by its value (Challenge!)
    def remove(self, data) -> bool:
        this_node = self.head

        while this_node:
            if this_node.get_data() == data:
                # We found the node! Now update the surrounding pointers.
                
                # Step A: Update the pointer of the node BEFORE this_node
                if this_node.get_prev() is not None:
                    this_node.set_next(this_node.get_prev())
                else:
                    # If there is no previous node, we are removing the head!
                    self.head = this_node.get_next()

                # Step B: Update the pointer of the node AFTER this_node
                if this_node.get_next() is not None:
                    # TODO: Make the next node's 'prev' point to this_node's 'prev'
                    this_node.set_prev(this_node.get_prev())
                else:
                    # If there is no next node, we are removing the tail!
                    self.tail = this_node.get_prev()

                self.size -= 1
                return True
            
            this_node = this_node.get_next()
            
        return False

    # Display starting from the head and going forward
    def display_forward(self) -> list:
        elements = []
        this_node = self.head
        while this_node:
            elements.append(this_node.get_data())
            this_node = this_node.get_next()
        return elements

    # Display starting from the tail and going backward (proves the prev links work!)
    def display_backward(self) -> list:
        elements = []
        this_node = self.tail
        while this_node:
            elements.append(this_node.get_data())
            this_node = this_node.get_prev()
        return elements


# --- Test Space ---
dll = DoublyLinkedList()

# Prepend test
dll.prepend(20)
dll.prepend(10)

dll.remove(10)

print("Prepended 10, then 20:")
print("Forward: ", dll.display_forward())  # Expected: [10, 20]
print("Backward:", dll.display_backward()) # Expected: [20, 10]

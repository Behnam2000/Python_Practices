class MinHeap:
    def __init__(self):
        # We use an underlying list to store the complete binary tree
        self.heap = []

    def push(self, value):
        """Adds a value to the heap in O(log n) time."""
        self.heap.append(value)

        # Bubble the new value up to its correct position
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        """Removes and returns the smallest value in O(log n) time."""
        if not self.heap:
            raise IndexError("Pop from an empty heap")
        
        # If there's only one element, just pop and return it
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Save the minimum value (the root)
        min_value = self.heap[0]

        # Move the last element to the root and shrink the array
        self.heap[0] = self.heap.pop()

        # Shift the new root down to its correct position
        self._shift_down(0)
        
        return min_value

    
    def _bubble_up(self, index):
        """Helper to move a node up the tree."""
        parent_index = (index - 1) // 2
        
        # Keep swapping while we haven't reached the root 
        # and the current node is smaller than its parent
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            # Swap
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

            # Update indices to continue bubbling up
            index = parent_index
            parent_index = (index - 1) // 2

    def _shift_down(self, index):
        """Helper to move a node down the tree."""
        length = len(self.heap)

        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            # Check if left child exists and is smaller than current smallest
            if left_child_index < length and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            # Check if right child exists and is smaller than current smallest
            if right_child_index < length and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            # If the smallest is still the current index, the heap property is restored
            if smallest == index:
                break

            # Otherwise, swap and continue sifting down
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest


myHeap = MinHeap()

myHeap.push(97)
myHeap.push(13)
myHeap.push(16)
myHeap.push(44)
myHeap.push(78)
myHeap.push(3)
myHeap.push(63)
myHeap.push(21)
myHeap.push(39)

print(myHeap.pop())



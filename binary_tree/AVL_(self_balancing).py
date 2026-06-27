from typing import Optional, Any

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None
        self.height = 1 # AVL nodes must track their height

class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def insert(self, value):
        """Public insert method that manages the root state internally."""
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, root, value):
        # 1. Perform standard BST insertion
        if not root:
            return AVLNode(value)
        elif value < root.value:
            root.left = self._insert_recursive(root.left, value)
        else:
            root.right = self._insert_recursive(root.right, value)

        # 2. Update the height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get the balance factor to check if it became unbalanced
        balance = self.get_balance(root)

        # 4. If unbalanced, execute one of the 4 rotations:

         ## Case 1: Left-Left Heavy
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)
        
         ## Case 2: Right-Right Heavy
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

         ## Case 3: Left-Right Heavy
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root 

    # --- Helper Methods for Height and Rotations ---

    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y # Return new root

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation 
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y # Return new root


    def print_in_order(self):
        """Prints elements in ascending sorted order"""
        elements = []
        self._in_order_recursive(self.root, elements)
        print("In-order Traversal (Sorted):", elements)
    
    def _in_order_recursive(self, node, elements):
        if node:
            self._in_order_recursive(node.left, elements)
            elements.append(node.value)
            self._in_order_recursive(node.right, elements)

    def display_visually(self):
        """Prints a visual, text-based representaion of the balanced structure"""
        print("\n--- Visual AVL Tree Structure ---\n")
        self._display_recursive(self.root, level=0, prefix="Root: ")
        print("------------------------------------------")

    def _display_recursive(self, node, level, prefix):
        if node is not None:
            self._display_recursive(node.right, level + 1, "R: ")
            indent = "    " * level
            print(f"{indent}{prefix}{node.value} (h={node.height})")
            self._display_recursive(node.left, level + 1, "L: ")



avl = AVLTree()

for i in [30, 22, 12, 25, 55, 51, 13, 7, 47, 37]:
    avl.insert(i)

# Displaying elements and balanced structure
avl.print_in_order()
avl.display_visually()
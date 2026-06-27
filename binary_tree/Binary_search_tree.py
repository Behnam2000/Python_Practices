from typing import Optional, Any

class BSTNode:
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        
        # if the value is less , go left
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(value)
            else:
                self._insert_recursive(current_node.left, value)

        # if the value is greater, go right 
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self._insert_recursive(current_node.right, value)
    
    
    
    # ===========================================
    # Display Methods
    # ===========================================

    def print_in_order(self):
        """Prints elements in ascending sorted order (Left -> Root -> Right)."""

        elements = []

        self._in_order_recursive(self.root, elements)
        print('In-order Traversal (sorted): ', elements)

    def _in_order_recursive(self, node, elements):
        if node:
            self._in_order_recursive(node.left, elements)
            elements.append(node.value)
            self._in_order_recursive(node.right, elements)

    def print_pre_order(self):

        elements = []

        self._pre_order_recursive(self.root, elements)
        print("Pre-order Traversal: ", elements)
    
    def _pre_order_recursive(self, node, elements):
        if node:
            elements.append(node.value)
            self._pre_order_recursive(node.left, elements)
            self._pre_order_recursive(node.right, elements)

    def print_post_order(self):
        
        elements = []

        self._post_order_recursive(self.root, elements)
        print("Post-order Traversal: ", elements)

    def _post_order_recursive(self, node, elements):
        if node:
            self._post_order_recursive(node.left, elements)
            self._post_order_recursive(node.right, elements)
            elements.append(node.value)

    def display_visually(self):

        print("\n----- Visual Tree Structure -----")
        self._display_recursive(self.root, level=0, prefix="Root: ")
        print("---------------------------------------------")

    def _display_recursive(self, node, level, prefix):
        if node is not None:

            self._display_recursive(node.right, level + 1, "R: ")


            indent = "    " * level
            print(f"{indent}{prefix}{node.value}")


            self._display_recursive(node.left, level + 1, "L ")



# Building the BST
bst = BinarySearchTree()

for num in [10, 5, 15, 2, 7]:
    bst.insert(num)


# Displaying the elements
bst.print_in_order()    # Outputs sorted order: [2, 5, 7, 10, 15]
bst.print_pre_order()   # Outputs: [10, 5, 2, 7, 15]
bst.print_post_order()  # Outputs: [2, 7, 5, 15, 10]

# Display the physical structure
bst.display_visually()
        


# The tree automatically organizes itself like this:
#        10
#      /    \
#     5      15
#    / \
#   2   7

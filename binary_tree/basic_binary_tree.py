from typing import Optional

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    
# 1. Create the nodes
root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")

# 2. Link them together manually
root.left = node_b
root.right = node_c
node_b.left = node_d
node_b.right = node_e

# The tree now looks like this:
#        A
#      /   \
#     B     C
#    / \
#   D   E        
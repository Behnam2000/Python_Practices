class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build a small tree:
#         10
#        /  \
#       5    15
#      / \     \
#     3   7    20

root = TreeNode(10,
    TreeNode(5, TreeNode(3), TreeNode(7)),
    TreeNode(15, None, TreeNode(20))
)


# ----------------------------------------------------
# The three fundamental recursive tree traversals:
# -----------------------------------------------------

def inorder(node):
    """Left -> Root -> Right (produces sorted order for a BST)"""

    if node is None:
        return
    
    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)

def preorder(node):
    """Root -> Left -> Right (useful for copying/serializing a tree)"""

    if node is None:
        return
    
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)

def postorder(node):
    """Left -> Right -> Root (useful for deleting a tree)"""

    if node is None:
        return
    
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=" ")

print("Inorder:  ", end=""); inorder(root);   print()  # 3 5 7 10 15 20
print("Preorder: ", end=""); preorder(root);  print()  # 10 5 3 7 15 20
print("Postorder:", end=""); postorder(root); print()  # 3 7 5 20 15 10


# ----------------------------------------------------------
# Other useful tree operations that are naturally recursive:
# ----------------------------------------------------------

def tree_height(node):
    """Height = longest path from root to a leaf"""

    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def tree_sum(node):
    if node is None:
        return 0
    return node.val + tree_sum(node.left) + tree_sum(node.right)

print(tree_height(root))
print(count_nodes(root))
print(tree_sum(root))
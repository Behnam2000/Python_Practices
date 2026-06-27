def traverse_in_order(node):
    """in-order traversal: Left, Root, Right"""

    if node is not None:
        traverse_in_order(node.left)
        print(node.element, end=' ')
        traverse_in_order(node.right)
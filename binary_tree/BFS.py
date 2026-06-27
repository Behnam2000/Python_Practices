from collections import deque

def traverse_level_order(root_node):
    """BFS traversal: Level by level, Left to Right"""

    if root_node in None:
        return
    
    queue = deque([root_node])
    
    while queue:
        current = queue.popleft()
        print(current.element, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    
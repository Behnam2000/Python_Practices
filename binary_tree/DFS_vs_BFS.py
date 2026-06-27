from collections import deque

# DFS (Recursive) - Dives down the left side first
def traverse_dfs(node):
    if not node:
        return
    print(node.value)        # Visit node
    traverse_dfs(node.left)  # Dive left
    traverse_dfs(node.right) # Dive right

# BFS (Iterative) - Reads level by level
def traverse_bfs(root):
    if not root: return
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        print(current.value)
        
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
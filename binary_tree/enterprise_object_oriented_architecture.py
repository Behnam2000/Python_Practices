from abc import ABC, abstractmethod
from typing import Optional, Any

class Node:
    """Lightweight, non-public class for storing a node in a binary tree."""
    def __init__(self, element: Any, parent: Optional['Node'] = None, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.element = element
        self.parent = parent
        self.left = left
        self.right = right

class BinaryTree(ABC):
    """Abstract base class representing a binary tree structure."""

    @abstractmethod
    def root(self)-> Optional[Node]:
        """Return the root position of the tree (or None if empty)."""
        pass

    @abstractmethod
    def left(self, p)-> Optional[Node]:
        """Return the position of p's left child (or None if empty)."""
        pass

    @abstractmethod
    def right(self, p)-> Optional[Node]:
        """Return the position of p's right child (or None if empty)."""
        pass

    def sibling(self, p)-> Optional[Node]:
        """Return the position of p's sibling (or None if no sibling)."""

        parent = p.parent

        if parent is None:
            return None     # p is the root
        
        if p is parent.left:
            return parent.right
        else:
            return parent.left
        
class LinkedBinaryTree(BinaryTree):
    """Concrete implementation of a binary tree using a linked structure."""

    def __init__(self):
        self._root: Optional[Node] = None
        self._size = 0

    def root(self)-> Optional[Node]:
        return self._root
    
    def left(self, p: Node)-> Optional[Node]:
        return p.left
    
    def right(self, p: Node)-> Optional[Node]:
        return p.right
    
    def add_root(self, element: Any):
        """Insert a root node into an empty tree."""
        if self._root is not None:
            raise ValueError("Root already exists")
        self._size = 1
        self._root = Node(element)
        return self._root

    def insert_left(self, p: Node, element: Any):
        """Create a new left child for the given node."""

        if p.left is not None:
            raise ValueError("left child already exists")
        self._size += 1
        p.left = Node(element, parent=p)
        return p.left
    
    def insert_right(self, p: Node, element: Any):
        """Create a new right child for the given node."""
        
        if p.right is not None:
            raise ValueError("Right child already exists")
        self._size += 1
        p.right = Node(element, parent=p)
        return p.right
    
from typing import Any, Optional

class Node:

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional["Node"] = None

class Ll:

    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def display(self) -> list:
        elements = []
        current_node = self.head

        while current_node is not None:
            elements.append(current_node.data)
            current_node = current_node.next

        return elements

    def length(self) -> int:
        current_node = self.head
        total = 0

        while current_node is not None:
            total += 1
            current_node = current_node.next

        return total

    def getData(self, index: int) -> Optional[str]:
        if index >= self.length():
            print('index out of range')
            return None
        current_index = 0
        current_node = self.head

        while current_node is not None:
            if current_index == index:
                return f"Here is your data: {current_node.data}"
            current_node = current_node.next
            current_index += 1

        return None

    def erase(self, index: int) -> None:
        if index >= self.length() or self.head is None:
            print("index out of range")
            return

        if index == 0:
            self.head = self.head.next
            return

        current_index = 0
        current_node = self.head

        while current_node is not None and current_node.next is not None:
            if current_index == index - 1:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            current_index += 1



myli = Ll()

myli.append('behnam')
myli.append(32)
myli.append('Nana')
myli.append('peugeot')
myli.append('Ferrari')
myli.append(140)

print(myli.display())

print(myli.length())

print(myli.getData(5))

myli.erase(2)

print(myli.display())

print(myli.length())





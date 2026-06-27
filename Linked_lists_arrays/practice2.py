from __future__ import annotations


class Node:
	def __init__(self, data, node=None):
		self.data = data
		self.next_node = node	 

	def get_next(self):
		return self.next_node

	def set_next(self, node):
		self.next_node = node

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data

class LinkedList:
	def __init__(self, root = None):
		self.root = root
		self.size = 0

	def get_size(self) -> int:
		return self.size

	def add(self, data) -> None:
		new_node = Node(data, self.root)
		self.root = new_node
		self.size += 1

	def append(self, data) -> None:
		new_node = Node(data)

		if self.root is None:
			self.root = new_node
		
		else:
			this_node = self.root
			while this_node and this_node.get_next() is not None:
				next_node = this_node.get_next()
				if next_node is None:
					break
				this_node = new_node
			this_node.set_next(new_node)

		# Linter Pylance Error
		# else:
		# 	this_node = self.root
		# 	while this_node.get_next() is not None:
		# 		this_node = this_node.get_next()
		# 	this_node.set_next(new_node)

		self.size += 1


	def remove(self, data) -> bool:
		this_node = self.root
		prev_node = None

		while this_node:
			if this_node.get_data() == data:
				if prev_node:
					prev_node.set_next(this_node.get_next())
				else:
					self.root = this_node.get_next()
				self.size -= 1
				return True
			else:
				prev_node = this_node
				this_node = this_node.get_next()
		return False

	def remove_by_index(self, index):
		if index >= self.size or index < 0:
			return False

		this_node = self.root
		this_idx = 0
		prev_node = None

		while this_node:
			if this_idx == index:
				if prev_node:
					prev_node.set_next(this_node.get_next())
				else:
					self.root = this_node.get_next()
				self.size -= 1
				return True
			
			prev_node = this_node
			this_node = this_node.get_next()
			this_idx += 1
		return False

	def find(self, data) -> bool:
		this_node = self.root

		while this_node:
			if this_node.get_data() == data:
				return data
			else:
				this_node = this_node.get_next()

		return False

	def find_lowest(self) -> int | None:
		if self.root is None:
			return None
		this_node = self.root
		min_value = this_node.get_data()

		while this_node:
			if this_node.get_data() < min_value:
				min_value = this_node.get_data()
			this_node = this_node.get_next()
		return min_value

	def display(self) -> list:
		elements = []
		this_node = self.root

		while this_node:
			elements.append(this_node.get_data())
			this_node = this_node.get_next()

		return elements

	def insert(self, data, index):
		if index == 0:
			return self.add(data)
		if index >= self.size:
			return self.append(data)

		new_node = Node(data)
		this_node = self.root
		prev_node = None
		this_idx = 0

		while this_node:
			if this_idx == index:
				
				new_node.set_next(this_node)	
				# Linter Pylance Error
				# prev_node.set_next(new_node)
				if prev_node is not None:
					prev_node.set_next(new_node)

				self.size += 1
				return

			else:
				prev_node = this_node
				this_node = this_node.get_next()
				this_idx += 1

	def reverse(self):
		if self.root is None or self.root.get_next() is None:
			return False

		this_node = self.root
		prev_node = None

		while this_node:
			next_node = this_node.get_next()
			this_node.set_next(prev_node)
			prev_node = this_node
			this_node = next_node

		self.root = prev_node

		return prev_node

	def find_middle(self):

		if self.root is None:
			return None

		slow_pointer = self.root
		# Linter Pylance Error
		# fast_pointer = self.root
		fast_pointer: Node | None =  self.root  


		while fast_pointer is not None and fast_pointer.get_next() is not None:

			# Linter Pylance Error
			# slow_pointer = slow_pointer.get_next()
			# fast_pointer = fast_pointer.get_next().get_next()

			fast_next = fast_pointer.get_next()
			if fast_next is None:
				break


			# Advance slow pointer safely
			slow_next = slow_pointer.get_next()
			if slow_next is not None:
				slow_pointer = slow_next
			
			# Advance fast pointer two steps safely
			fast_pointer = fast_next.get_next()

		return slow_pointer.get_data()



mylist = LinkedList()

mylist.append(350)
mylist.append(911)
mylist.append(250)
mylist.append(405)
mylist.append(33)
mylist.append(140)

print(mylist.get_size())
print(mylist.display())
print(mylist.find(405))
print(mylist.find_lowest())

mylist.remove_by_index(3)
print(mylist.display())

mylist.insert(458, 4)
mylist.insert('Behnam', 3)
print(mylist.display())

mylist.reverse()
print(mylist.display())

print(mylist.find_middle())




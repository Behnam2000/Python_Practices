class Node(object):
	def __init__(self, d=None, n=None):
		self.data = d
		self.next_node = n

	def get_data(self):
		return self.data

	def set_data(self, d):
		self.data = d

	def get_next(self):
		return self.next_node

	def set_next(self, n):
		self.next_node = n

class Linked(object):
	def __init__(self, r=None):
		self.root = r
		self.size = 0

	def add(self, d):
		new_node = Node(d, self.root)
		self.root = new_node
		self.size += 1

	def append(self, d):
		new_node = Node(d)

		if self.root is None:
			self.root = new_node
			self.size += 1

		else:
			this_node = self.root

			while this_node.get_next() is not None:
				this_node = this_node.get_next()
			this_node.set_next(new_node)
		
		self.size += 1


	def get_size(self):
		return self.size

	def display(self):
		this_node = self.root
		result = []

		while this_node:
			result.append(this_node.get_data())
			this_node = this_node.get_next()
			
		
		return result

	def delete(self, data):
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



myL = Linked()

myL.add(12)
myL.add(20)
myL.add(10)
myL.add(18)
myL.add(13)
myL.add(23)
myL.add(31)

myL.append(100)
myL.append(230)
myL.append(670)


print(myL.get_size())
myL.delete(18)
myL.delete(10)
myL.delete(100)
print(myL.display())

class node:

	def __init__(self,item):
		if item == None:
			self.item = None
			self.next = None
		else:
			self.item = item
			self.next = node(None)

class ll:

	def __init__(self):
		self.head = node(None)
		self.count = 0

	def add(self,item):
	# add to beginning
		if self.head.next == None:
			self.head = node(item)
			self.count = 1
		else:
			n = self.head.next
			self.head = node(item)
			self.head.next = n
			self.count += 1

	def remove(self,item):
	# remove first matching item
		n = self.head
		p = node(None)
		while n.item != item and n.next.next != None:
			p = n
			n = n.next
		if n.next != None:
			p.next = n.next
		else:
			p.next = node(None)
		self.count -= 1

	def search(self,item):
	# return boolean if exists
		n = self.head
		while n.item != item and n.next.next != None:
			n = n.next
		if n == node(None):
			return(False)
		else:
			return(True)

	def isEmpty(self):
	# return true if empty, false otherwise
		if self.head.next == None:
			return(True)
		else:
			return(False)

	def size(self):
	# return size of ll
		return(self.count)

	def index(self,item):
	# return how far into the ll matching item is (search with count)
		n = self.head
		# counter
		c = 0
		while n.item != item and n.next.next != None:
			n = n.next
			c += 1
		if n == node(None):
			return(False)
		else:
			return(c)

	def insert(self,pos,item):
	# insert at position
		n = self.head
		for f in range(pos):
			n = n.next
		# inserted node's next
		a = n.next
		n.next = node(item)
		n.next.next = a

	def append(self,item):
	# add to end
		n = self.head
		while n.next.next != None:
			n = n.next
		n.next = node(item)
		self.count += 1

	def pop(self):
	# delete and return last item
		n = self.head
		p = node(None)
		while n.next.next != None:
			p = n
			n = n.next
		p.next = node(None)
		return(n.item)

	def peek(self):
		n = self.head
		while n.next.next != None:
			n = n.next
		return(n.item)

	def delete(self,item):
	# delete and return matching item
		n = self.head
		while n.item != item and n.next.next != None:
			p = n
			n = n.next
		if n.item == item:
			p.next = n.next
			return(n.item)
		else:
			return(False)

# doubly linked node class
class node:

	def __init__(self,item,last):
		if item == None:
			self.item = None
			self.last = None
			self.next = None
		else:
			self.item = item
			self.last = last
			self.next = node(None,None)

# doubly linked list class
class dll:

	def __init__(self):
		self.head = node(None,None)
		self.count = 0

	def add(self,item):
	# add to beginning
		if self.head.next == None:
			self.head = node(item,None)
			self.count = 1
		else:
			n = self.head
			self.head = node(item,None)
			self.head.next = n
			n.last = self.head
			self.count += 1

	def remove(self,item):
	# remove first matching item
		n = self.head
		p = node(None,None)
		while n.item != item and n.next.next != None:
			p = n
			n = n.next
		if n.next != None:
			p.next = n.next
		else:
			p.next = node(None,None)
		self.count -= 1

	def search(self,item):
	# return boolean if exists
		n = self.head
		while n.item != item and n.next.next != None:
			n = n.next
		if n == node(None,None):
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
	# return size of dll
		return(self.count)

	def append(self,item):
	# add to end
		n = self.head
		while n.next.next != None:
			n = n.next
		n.next = node(item,n)
		self.count += 1

	def index(self,item):
	# return how far into the dll matching item is (search with count)
		n = self.head
		# counter
		c = 0
		while n.item != item and n.next.next != None:
			n = n.next
			c += 1
		if n == node(None,None):
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
		n.next = node(item,n)
		n.next.next = a

	def pop(self):
	# delete and return last item
		n = self.head
		while n.next.next != None:
			n = n.next
		n.last.next = node(None,None)
		self.count -= 1
		return(n.item)

	def delete(self,item):
	# delete and return matching item
		n = self.head
		while n.item != item and n.next.next != None:
			n = n.next
		if n.item == item:
			n.last.next = n.next
			return(n.item)
		else:
			return(False)

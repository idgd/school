from ll import ll

class stack:

	def __init__(self):
		self.s = ll()

	def push(self,item):
		if self.s.isEmpty():
			self.s.add(item)
		else:
			self.s.append(item)
		# linear time

	def pop(self):
		return(self.s.pop())
		# linear time

	def peek(self):
		return(self.s.peek())
		# linear time

	def isEmpty(self):
		return(self.s.isEmpty())
		# constant time

	def size(self):
		return(self.s.size())
		# constant time

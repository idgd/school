from dll import dll

class queue:

	def __init__(self):
		self.q = dll()

	def enqueue(self,item):
		self.q.add(item)
		# constant time

	def dequeue(self):
		return(self.q.pop())
		# linear time

	def isEmpty(self):
		return(self.q.isEmpty())
		# constant time

	def size(self):
		return(self.q.size())
		# linear time

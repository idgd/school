from Node import Node

class DirectedGraph:
	def __init__(self,first):
		self.first = Node(first)

	def add(self,node,relatives = None,index = None):
		if index:
			n = self.first
			for f in index[:-1]:
				n = n.relatives[f]
			n.relatives.insert(index[-1],Node(node))
			n.relatives[index[-1]].relatives = relatives
		else:
			self.first.relatives.append(Node(node))

	def search(self,data,node):

		node.seen = True

		if node.data == data:
			return(True)

		if data in [f.data for f in node.relatives]:
			return(True)
		else:
			for f in [f for f in node.relatives if not f.seen]:
				return(self.search(data,f))

		return(False)

# running time of search:
# best case is constant
# worst case is n, where n is the number of nodes in the graph
# in all true cases, the runtime is the number of relatives the node has
# in all maybe cases, it simply does this linear check over each relative
# in the false case, it has checked every node once, thus, n

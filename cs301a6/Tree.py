from Node import Node

class Tree:
	def __init__(self,root):
		self.root = Node(root)

	def add(self,node,index = None):
		if index:
			n = self.root
			for f in index[:-1]:
				n = n.relatives[f]
			n.relatives.insert(index[-1],Node(node))
		else:
			self.root.relatives.append(Node(node))

	def search(self,node,tree):
		if tree.data == node:
			return(True)

		if node in [f.data for f in tree.relatives]:
			return(True)
		else:
			for f in tree.relatives:
				return(self.search(node,f))

		return(False)

# running time of search:
# best case is constant
# worst case is n, where n is the number of nodes in the tree
# in all true cases, the runtime is the number of relatives the node has
# in all maybe cases, it simply does this linear check over each relative
# in the false case, it has checked every node once, thus, n

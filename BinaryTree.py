# Simple binary tree along with traversing

# class to create a tree node object
class tree_node():
	def __init__(self, value):
		self.node_value = value
		self.left_node = None
		self.right_node = None

class binarytree():
	def __init__(self):
		self.root_node = None

	#Create a root node 
	def root_node_create(self, value):
		self.root_node = tree_node(value)

    # Add node
	def add_node(self,value):
		if self.root_node == None:
			self.root_node_create(value)
		else:
			self.node_create(value,self.root_node)


	#Create a leafnode
	def node_create(self, value, node):
        # Traversing through the tree to find spot
        # Assigning the address of self.tree_node to temp		
	    # looping through the tree	
		print("Adding the node")	
		if node.node_value > value:
			if node.left_node is not None:
				self.node_create(value, node.left_node)
			else:
				node.left_node = tree_node(value)
					
		else:
			if node.right_node is not  None:
				self.node_create(value, node.right_node)
			else:
				node.right_node = tree_node(value)
					
				
	#Print Values in tree
	def print(self):
		if self.root_node is not None:
			self.traverse_tree(self.root_node)

	#Traverse the tree
	def traverse_tree(self, node):
		#Inorder traversal
		if node is not None:
			self.traverse_tree(node.left_node)
			print(node.node_value)
			self.traverse_tree(node.right_node)

bt = binarytree()
bt.add_node(12)
bt.add_node(9)
bt.add_node(6)
bt.add_node(43)
bt.add_node(10)
bt.add_node(73)
bt.add_node(22)
bt.print()





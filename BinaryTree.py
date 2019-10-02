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

	#Create a leafnode
	def node_create(self, value):
		if self.root_node == None:
		    return  self.root_node_create(value)
		else:
        # Traversing through the tree to find spot
        # Assigning the address of self.tree_node to temp
			temp = self.root_node
			print(temp)
	        # looping through the tree
			while temp:
				if temp.node_value > value:
					temp = temp.left_node
				else:
					temp = temp.right_node
				if temp == None:
					temp = tree_node(value)
					break


  

bt = binarytree()
bt.node_create(10)
bt.node_create(9)
bt.node_create(11)







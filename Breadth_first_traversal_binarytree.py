# Breadth first traversal 
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

		print("Breadth first Traversal")
		if self.root_node is not None:
			self.breadth_first_traversal(self.root_node)
	#Traverse the tree
	def traverse_tree(self, node):
		#Inorder traversal
		if node is not None:
			self.traverse_tree(node.left_node)
			print(node.node_value)
			self.traverse_tree(node.right_node)
	# Breadth first traversal / Level traversal
	# algorithm uses queue to track the nodes

	def breadth_first_traversal(self, node):

		queue_of_node = []

		queue_of_node.append(node)
		ans = []
		while len(queue_of_node) > 0:
			node = queue_of_node[0]
			print("for node : {}, left = {}, right = {}".format(node.node_value,  node.left_node, node.right_node))
			if node.left_node:
				print("Adding left")
				queue_of_node.append(node.left_node)
			else:
				print("left not present")		
			if node.right_node:
				print("Adding Right")
				queue_of_node.append(node.right_node)
			else:
				print("right not present")
			#Adding the value of node to ans and popping it
			ans.append(queue_of_node[0].node_value)
			print(ans)
			if len(queue_of_node) > 0:
				queue_of_node.pop(0)







bt = binarytree()
bt.add_node(12)
bt.add_node(9)
bt.add_node(6)
bt.add_node(43)
bt.add_node(10)
bt.add_node(73)
bt.add_node(22)
bt.print()





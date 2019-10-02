class Node():
	def __init__(self, value):
		self.value = value
		self.next_node = None 


class LinkedList():

	def __init__(self):
		self.start_node = None

	def create_first_node(self, value):
		print("Creating the first node")
		self.start_node = Node(value)
		return self.start_node

	def insert_node(self, value):
		if(self.start_node == None):
			return self.create_first_node(value)
		elif(self.start_node!= None):
			
            # Travesing the tree to find the last node
			temp = self.start_node

			while temp:
				# Traversing the tree
				
				if temp.next_node == None:
					print("Adding node")
					temp.next_node = Node(value)
					break
				else:
					temp = temp.next_node     
			#self.start_node = temp

	def traverse_linked_list(self):
		temp_node = self.start_node
		while temp_node.value != None:

			print(temp_node.value)
			temp_node = temp_node.next_node
			if temp_node == None:
				break





ll = LinkedList()
ll.insert_node(10)
ll.insert_node(20)
ll.insert_node(30)
ll.insert_node(40)
ll.insert_node(45) 
ll.traverse_linked_list()






#In this program we will implement graph data structure using dictionary in python


class graph:
	graph = {}

	# Adding the node 
	def add_edge(self, node, neighbour):
		if  node not in self.graph:
			self.graph[node] = [neighbour]
		else:
			self.graph[node].append(neighbour)

	def show_node(self):
		for key in self.graph:
			#for value in self.graph[key]:
				print("key :{} , vertex: {}".format(key, self.graph[key]) )


#	def depth_first_search(self):


g = graph()

g.add_edge(2,3)
g.add_edge(2,1)
g.add_edge(2,3)
g.add_edge(3,4)
#g.add_edge('a','f')
print(g)
g.show_node()


